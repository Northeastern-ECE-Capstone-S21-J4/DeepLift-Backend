from typing import List

from pydantic import BaseModel
from datetime import date


class ExcerciseBase(BaseModel):
    exerciseName: str


class Exercise(ExcerciseBase):
    excerciseID: int

    class Config:
        orm_mode = True