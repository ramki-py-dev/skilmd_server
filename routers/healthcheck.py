import uvicorn
from fastapi import FastAPI
from schemas.common import APIResponse
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(tags=[{"name": "Healthcheck"}])

@router.get("/", response_model=APIResponse)
async def read_root():
    """
    Root endpoint to check if the API is running.

    Returns:
        APIResponse: success=True if the service is healthy, or success=False if an error occurs.
    """
    try:
        health_check = APIResponse(
            success=True,
            message="Service is healthy",
            data={
                "status": "ok",
                "timestamp": datetime.utcnow()
            },
            error=None
        )
        return health_check

    except Exception as e:
        un_health = APIResponse(
            success=False,
            message="Service is unhealthy",
            data={"status": "error"},
            error=str(e)
        )
        return un_health
