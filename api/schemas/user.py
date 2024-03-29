from pydantic import BaseModel
from datetime import date


# Schemas for DeepliftUser table endpoints
# -------------------------------------------------------------------------------------------------------
# [BASE]


class DeepliftUserBase(BaseModel):
    userName: str
    firstName: str
    lastName: str

    # Allow for lists
    class Config:
        orm_mode = True

# -------------------------------------------------------------------------------------------------------
# [GET]


# Model for a UserProfile. Stores all user information in DeepliftUser table
class DeepliftUserProfile(DeepliftUserBase):
    bodyweight: int
    age: int
    dateJoined: date
    email: str


class CurrentlyLifting(BaseModel):
    currentlyLifting: bool
    difficulty: int

    # Allow for lists
    class Config:
        orm_mode = True

# -------------------------------------------------------------------------------------------------------
# [POST]


class DeepliftUserCreate(DeepliftUserBase):
    bodyweight: int
    age: int
    email: str
    pw: str

# -------------------------------------------------------------------------------------------------------
# [PUT]


class DeepliftUserUpdate(DeepliftUserBase):
    bodyweight: int
    age: int


class DeepliftUserLogin(BaseModel):
    userName: str
    pw: str
