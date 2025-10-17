import datetime
from typing import Optional
from pydantic import BaseModel, Field

class BaseRequestModel(BaseModel):
    class Config:
        str_strip_whitespace = True

class APIResponse(BaseRequestModel):
    """
    Standard API response format for all endpoints.

    Attributes:
        success (bool): Indicates if the request was successful.
        message (str): A human-readable message describing the result.
        data (Optional[Any]): The actual response data (can be any type or model).
        error (Optional[str]): Error details if the request failed.
    """
    success: bool
    message: str
    data: Optional[object] = None
    error: Optional[str] = None