from pydantic import BaseModel
from datetime import date

# Schemas for Workout table endpoints
# -------------------------------------------------------------------------------------------------------
# [BASE]


class WorkoutBase(BaseModel):
    reps: int
    weight: int
    difficulty: int

# -------------------------------------------------------------------------------------------------------
# [GET]


class Workout(WorkoutBase):
    workoutID: int
    exerciseName: str
    dateRecorded: date

    class Config:
        orm_mode = True

# -------------------------------------------------------------------------------------------------------
# [POST]


class WorkoutCreate(WorkoutBase):
    exerciseID: int

    # Allow for lists
    class Config:
        orm_mode = True