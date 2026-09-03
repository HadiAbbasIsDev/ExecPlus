"""Use case: Exposes deployment health endpoints.

What it does: Separates process liveness from dependency-aware readiness.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from pydantic import BaseModel, ConfigDict

from execplus.application.services.health import HealthService
from execplus.presentation.dependencies import get_health_service


class ComponentStatusResponse(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    healthy: bool
    detail: str


class HealthResponse(BaseModel):
    model_config = ConfigDict(frozen=True)

    status: str
    components: tuple[ComponentStatusResponse, ...] = ()


router = APIRouter(tags=["health"])


@router.get("/health/live", response_model=HealthResponse)
async def liveness() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/health/ready", response_model=HealthResponse)
async def readiness(
    response: Response,
    service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    healthy, components = await service.readiness()
    if not healthy:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return HealthResponse(
        status="ready" if healthy else "not_ready",
        components=tuple(
            ComponentStatusResponse(
                name=component.name,
                healthy=component.healthy,
                detail=component.detail,
            )
            for component in components
        ),
    )
