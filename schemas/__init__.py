from datetime import datetime
from functools import partial
from uuid import UUID

import pytz
from pydantic import BaseModel, EmailStr
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

from utils.string import validate_email

CustomEmailStr = Annotated[EmailStr, BeforeValidator(partial(validate_email))]


class BaseSchema(BaseModel):
    class Config:
        json_encoders = {
            UUID: lambda uuid_value: str(uuid_value) if uuid_value else None,
            datetime: lambda dt: dt.replace(tzinfo=pytz.UTC).isoformat() if dt else None,
        }
