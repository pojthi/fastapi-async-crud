from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from uuid import UUID


class UserBaseSchema(BaseModel):

    id: UUID | None = None
    name: str = Field(
        ..., description="The name of the user", example="Poj"
    )
    description: str | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class Status(Enum):
    Success = "Success"
    Failed = "Failed"


class UserResponse(BaseModel):
    Status: Status
    User: UserBaseSchema


class GetUserResponse(BaseModel):
    Status: Status
    User: UserBaseSchema


class ListUserResponse(BaseModel):
    status: Status
    results: int
    users: List[UserBaseSchema]


class DeleteUserResponse(BaseModel):
    Status: Status
    Message: str
