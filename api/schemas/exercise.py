from pydantic import BaseModel


class ExcerciseBase(BaseModel):
    exerciseName: str


class Exercise(ExcerciseBase):
    excerciseID: int

    class Config:
        orm_mode = True