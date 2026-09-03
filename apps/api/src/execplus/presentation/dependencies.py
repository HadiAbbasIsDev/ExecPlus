"""Use case: Builds application dependencies for HTTP handlers.

What it does: Centralizes provider composition outside route implementations.
"""

from functools import lru_cache

from execplus.application.services.health import HealthService


@lru_cache
def get_health_service() -> HealthService:
    return HealthService()
