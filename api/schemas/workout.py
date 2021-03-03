from pydantic import BaseModel
from datetime import date

# Schemas for Workout table endpoints
# -------------------------------------------------------------------------------------------------------
# [BASE]


class WorkoutBase(BaseModel):
    reps: int
    weight: int
    difficulty: int

    # Allow for lists
    class Config:
        orm_mode = True

# -------------------------------------------------------------------------------------------------------
# [GET]


class Workout(WorkoutBase):
    workoutID: int
    exerciseName: str
    dateRecorded: date
    video_path: str
    keypoints_path: str
    analytics_path: str

# -------------------------------------------------------------------------------------------------------
# [POST]


class WorkoutCreate(WorkoutBase):
    exerciseID: int
    userName: str


# -------------------------------------------------------------------------------------------------------
# [PUT]


class WorkoutUpdate(WorkoutBase):
    exerciseID: int
    workoutID: int
