from typing import List, Optional

from pydantic import BaseModel
from datetime import date


class WorkoutBase(BaseModel):
    exerciseID: int


class WorkoutCreate(WorkoutBase):
    reps: int
    weight: int
    difficulty: int 


class Workout(WorkoutBase):
    workoutID: int
    userID: int
    dateRecorded: date

    class Config:
        orm_mode = True


class DeepliftUserBase(BaseModel):
    email: str


class DeepliftUserCreate(DeepliftUserBase):
    firstName: str
    lastName: str
    bodyweight: int
    age: int


class DeepliftUser(DeepliftUserBase):
    userID: int
    dateJoined: date
    workouts: List[Workout] = []

    class Config:
        orm_mode = True


class ExcerciseBase(BaseModel):
    exerciseName: str


class Exercise(ExcerciseBase):
    excerciseID: int

    class Config:
        orm_mode = True