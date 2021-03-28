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
    username: str
    exerciseID: int
    reps: int
    weight: int
    difficulty: int


class WorkoutReturn(BaseModel):
    video_with_path: str
    video_without_path: str

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
