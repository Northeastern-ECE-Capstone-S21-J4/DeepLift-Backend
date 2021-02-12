from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime

def get_user(db: Session, user_id: int):
    return db.query(models.DeepliftUser).filter(models.DeepliftUser.userID == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DeepliftUser).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.DeepliftUserCreate):
    join_date = datetime.now().isoformat()
    db_user = models.DeepliftUser(
        email=user.email, 
        firstName=user.firstName,
        lastName=user.firstName,
        bodyweight=user.bodyweight,
        age=user.age,
        dateJoined=join_date,
        workouts=[])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.DeepliftUser).filter(models.DeepliftUser.email == email).first()


def create_workout(db: Session, workout: schemas.WorkoutCreate, user_id: int):
    workout_date = datetime.now().isoformat()
    db_item = models.Workout(**workout.dict(), dateRecorded=workout_date, userID=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
