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