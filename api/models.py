from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class DeepliftUser(Base):
    __tablename__ = "DeepliftUser"

    userName = Column(String, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    bodyweight = Column(Integer)
    age = Column(Integer)
    dateJoined = Column(Date)

    workouts = relationship("Workout", back_populates="user")


class Workout(Base):
    __tablename__ = "Workout"

    workoutID = Column(Integer, primary_key=True)
    userName = Column(String, ForeignKey("DeepliftUser.userName"))
    reps = Column(Integer)
    weight = Column(Integer)
    exerciseID = Column(Integer, ForeignKey("Exercise.exerciseID"))
    dateRecorded = Column(Date)
    difficulty = Column(Integer)

    user = relationship("DeepliftUser", back_populates="workouts")
    exercise = relationship("Exercise")


class Exercise(Base):
    __tablename__ = "Exercise"

    exerciseID = Column(Integer, primary_key=True)
    exerciseName = Column(String, unique=True)
