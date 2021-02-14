from pydantic import BaseModel
from datetime import date


# Schemas for DeepliftUser table endpoints
# -------------------------------------------------------------------------------------------------------
# [BASE]


class DeepliftUserBase(BaseModel):
    firstName: str
    lastName: str

# -------------------------------------------------------------------------------------------------------
# [GET]


# Model for UserNames. Stores First and Last Name for a user
class DeepliftUserNames(DeepliftUserBase):
    userID: int

    # Allow for lists
    class Config:
        orm_mode = True


# Model for a UserProfile. Stores all user information in DeepliftUser table
class DeepliftUserProfile(DeepliftUserNames):
    bodyweight: int
    age: int
    dateJoined: date
    email: str


class DeepliftUserCreate(DeepliftUserBase):
    email: str
    bodyweight: int
    age: int