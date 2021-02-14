from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas.user, schemas.workout, schemas.exercise
from database import SessionLocal, engine

from auth import signJWT, check_pw, JWTBearer

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Base root of API
@app.get("/")
def read_root():
    return "Hello DeepLift!"


# [GET] Return the names of all users in the db (only names).
# USES: Friends list, search users
@app.get("/users", response_model=List[schemas.user.DeepliftUserNames])
def get_user_names(db: Session = Depends(get_db)):
    users = crud.get_user_names(db)
    return users


# [GET] Return all profile information relevant to a specific user (not workouts)
# USES: User profile page
@app.get("/users/{user_id}", response_model=schemas.user.DeepliftUserProfile)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_profile(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# [GET] Return all workouts linked to a specific user
# USES: See all past workouts
# @app.get("/workouts/user/{user_id}", response_model=schemas.workouts.UserProfile)
# def get_user_workouts(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user_workouts(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.post("/users", dependencies=[Depends(JWTBearer())], response_model=schemas.user.DeepliftUserCreate)
# def create_user(user: schemas.user.DeepliftUserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @app.post("/users/{user_id}/add_workout", dependencies=[Depends(JWTBearer())], response_model=schemas.workout.Workout)
# def add_workout(user_id: int, workout: schemas.workout.WorkoutCreate, db: Session = Depends(get_db)):
#     return crud.create_workout(db=db, workout=workout, user_id=user_id)


@app.get("/token/{user_name}/{user_pw}")
def get_token(user_name: str, user_pw: str):
    if(check_pw(user_name, user_pw)):
        return signJWT(user_name)

    return { "error" : "Invalid credentials"}
