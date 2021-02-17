from pydantic import BaseModel
from datetime import date

# Schemas for Workout table endpoints
# -------------------------------------------------------------------------------------------------------
# [BASE]


class WorkoutBase(BaseModel):
    reps: int
    weight: int
    exerciseName: str
    difficulty: int

# -------------------------------------------------------------------------------------------------------
# [GET]


class Workout(WorkoutBase):
    workoutID: int
    dateRecorded: date

    class Config:
        orm_mode = True

# -------------------------------------------------------------------------------------------------------
# [POST]


# class WorkoutCreate(WorkoutBase):
#     reps: int
#     weight: int
#     difficulty: int
