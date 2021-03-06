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


class WorkoutCreate(BaseModel):
    userName: str
    exerciseID: int
    reps: int
    weight: int


class WorkoutReturn(BaseModel):
    video_path: str
    keypoints_path: str
    analytics_path: str
    workoutID: int

# -------------------------------------------------------------------------------------------------------
# [PUT]


class WorkoutUpdate(BaseModel):
    workoutID: int
    difficulty: int
    weight: int


class LatestUpdate(BaseModel):
    user_name: str
    difficulty: int


class WorkoutUpdateReturn(WorkoutBase):
    workoutID: int
    userName: str
    exerciseID: int
