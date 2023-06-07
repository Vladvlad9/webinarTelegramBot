from datetime import datetime
from pydantic import BaseModel, Field


class UsersSchema(BaseModel):
    user_id: int = Field(ge=1)


class UsersInDBSchema(UsersSchema):
    id: int = Field(ge=1)
