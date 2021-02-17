from pydantic import BaseModel


class ExerciseBase(BaseModel):
    exerciseName: str


class Exercise(ExerciseBase):
    exerciseID: int

    class Config:
        orm_mode = True