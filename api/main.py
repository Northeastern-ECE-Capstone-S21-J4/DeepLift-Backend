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

# -----------------------------------------------------------------------------------------------------
# /users


# [GET] Return the names of all users in the db (only names).
# USES: Friends list, search users
@app.get("/users", response_model=List[schemas.user.DeepliftUserBase])
def get_user_names(db: Session = Depends(get_db)):
    users = crud.get_user_names(db)
    return users


# [GET] Return all profile information relevant to a specific user (not workouts)
# USES: User profile page
@app.get("/users/{user_name}", response_model=schemas.user.DeepliftUserProfile)
def get_user_profile(user_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_profile(db, user_name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# [POST] Create a new user
# USES: Create new user on sign-up
#@app.post("/users", dependencies=[Depends(JWTBearer())], response_model=schemas.user.DeepliftUserCreate)
@app.post("/users", response_model=schemas.user.DeepliftUserCreate)
def create_user(user: schemas.user.DeepliftUserCreate, db: Session = Depends(get_db)):
    if crud.user_email_exists(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud.user_username_exists(db, user.userName):
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

# -----------------------------------------------------------------------------------------------------
# /workouts


# [GET] Return a workout with the given workoutID
# USES: Click on a certain workout
@app.get("/workouts/{workout_id}", response_model=schemas.workout.Workout)
def get_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = crud.get_workout(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="User or User workouts not found")
    return db_workout


# [GET] Return all workouts linked to a specific user
# USES: See all past workouts
@app.get("/workouts/user/{user_name}", response_model=List[schemas.workout.Workout])
def get_user_workouts(user_name: str, db: Session = Depends(get_db)):
    db_user_workouts = crud.get_user_workouts(db, user_name=user_name)
    if db_user_workouts is None:
        raise HTTPException(status_code=404, detail="User or User workouts not found")
    return db_user_workouts


# [GET] Return all workouts linked to a specific user and exercise
# USES: See all past workouts by exercise
@app.get("/workouts/user/{user_name}/ex/{ex_id}", response_model=List[schemas.workout.Workout])
def get_user_ex_wo(user_name: str, ex_id: int, db: Session = Depends(get_db)):
    db_user_workouts = crud.get_user_ex_wo(db, user_name=user_name, ex_id=ex_id)
    if db_user_workouts is None:
        raise HTTPException(status_code=404, detail="User or User workouts not found")
    return db_user_workouts


# [GET] Return all workouts linked to a specific user on a given date
# USES: See all past workouts by date
@app.get("/workouts/user/{user_name}/date/{date_recorded}", response_model=List[schemas.workout.Workout])
def get_user_date_wo(user_name: str, date_recorded: str, db: Session = Depends(get_db)):
    db_user_workouts = crud.get_user_date_wo(db, user_name=user_name, date_recorded=date_recorded)
    if db_user_workouts is None:
        raise HTTPException(status_code=404, detail="User or User workouts not found")
    return db_user_workouts


# [POST] Create a new workout
# USES: Create new workout
#@app.post("/users", dependencies=[Depends(JWTBearer())], response_model=schemas.user.DeepliftUserCreate)
@app.post("/workouts/{user_name}", response_model=schemas.workout.WorkoutCreate)
def create_workout(user_name: str, workout: schemas.workout.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db=db, user_name=user_name, workout=workout)

# -----------------------------------------------------------------------------------------------------
# /exercises


# [GET] Return all information in the Exercise table
# USES: Front-end for workouts by exercise, exercise list for creating workout
@app.get("/exercises", response_model=List[schemas.exercise.Exercise])
def get_exercises(db: Session = Depends(get_db)):
    db_exercises = crud.get_exercises(db)
    return db_exercises


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
# -----------------------------------------------------------------------------------------------------
# /token

@app.get("/token/{user_name}/{user_pw}")
def get_token(user_name: str, user_pw: str):
    if check_pw(user_name, user_pw):
        return signJWT(user_name)

    return {"error": "Invalid credentials"}
