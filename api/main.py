from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud
import models
import schemas.user, schemas.workout, schemas.exercise
from database import SessionLocal, engine

from auth import signJWT, JWTBearer

import hashlib

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
@app.post("/users", dependencies=[Depends(JWTBearer())], response_model=schemas.user.DeepliftUserCreate)
def create_user(user: schemas.user.DeepliftUserCreate, db: Session = Depends(get_db)):
    if crud.user_email_exists(db, email=user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud.user_username_exists(db, user.userName):
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


# [PUT] Update a current User's profile information
# USES: Update User information from profile page
@app.put("/users/update", dependencies=[Depends(JWTBearer())], response_model=schemas.user.DeepliftUserProfile)
def update_user(user: schemas.user.DeepliftUserUpdate, db: Session = Depends(get_db)):
    if not crud.user_username_exists(db, user.userName):
        raise HTTPException(status_code=400, detail="Username not registered!")
    return crud.update_user(db=db, user=user)


# [DELETE] Delete a current User from the db
# USES: Delete account
@app.delete("/users/delete/{user_name}", dependencies=[Depends(JWTBearer())])
def delete_user(user_name: str, db: Session = Depends(get_db)):
    if not crud.user_username_exists(db, user_name):
        raise HTTPException(status_code=400, detail="Username not registered!")
    crud.delete_user(db=db, user_name=user_name)
    return str(not crud.user_username_exists(db, user_name))
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
@app.post("/workouts", dependencies=[Depends(JWTBearer())], response_model=schemas.workout.WorkoutCreate)
def create_workout(workout: schemas.workout.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db=db, workout=workout)


# [PUT] Update a current Workout's information
# USES: Edit a past Workout
@app.put("/workouts/update", dependencies=[Depends(JWTBearer())], response_model=schemas.workout.WorkoutCreate)
def update_workout(workout: schemas.workout.WorkoutUpdate, db: Session = Depends(get_db)):
    if not crud.workout_exists(db, workout.workoutID):
        raise HTTPException(status_code=400, detail="Workout doesn't exist!")
    return crud.update_workout(db=db, workout=workout)


# [DELETE] Delete a current Workout from the db
# USES: Delete specific workout
@app.delete("/workouts/delete/{workout_id}", dependencies=[Depends(JWTBearer())])
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    if not crud.workout_exists(db, workout_id):
        raise HTTPException(status_code=400, detail="Workout not in the DB!")
    crud.delete_workout(db=db, workout_id=workout_id)
    return str(not crud.workout_exists(db, workout_id))

# -----------------------------------------------------------------------------------------------------
# /exercises


# [GET] Return all information in the Exercise table
# USES: Front-end for workouts by exercise, exercise list for creating workout
@app.get("/exercises", response_model=List[schemas.exercise.Exercise])
def get_exercises(db: Session = Depends(get_db)):
    db_exercises = crud.get_exercises(db)
    return db_exercises

# -----------------------------------------------------------------------------------------------------
# /token


@app.post("/login")
async def login(login_payload: schemas.user.DeepliftUserLogin, db: Session = Depends(get_db)):
    if(login_payload.pw == crud.get_user_password(db, login_payload.userName)[0].lower()):
        return signJWT(login_payload.userName)
    return {"Error": "Invalid credentials"}
