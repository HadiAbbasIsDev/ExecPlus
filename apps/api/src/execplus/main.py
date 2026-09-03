"""Use case: Creates the ExecPlus HTTP application.

What it does: Configures API metadata and mounts operational routes.
"""

from fastapi import FastAPI

from execplus import __version__
from execplus.presentation.routes.health import router as health_router


def create_app() -> FastAPI:
    application = FastAPI(
        title="ExecPlus API",
        summary="Verified conversational analytics",
        version=__version__,
    )
    application.include_router(health_router)
    return application


app = create_app()
