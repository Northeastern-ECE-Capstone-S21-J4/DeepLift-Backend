from sqlalchemy.orm import Session, load_only
import models
import schemas.user, schemas.workout, schemas.exercise
from datetime import date

# -----------------------------------------------------------------------------------------------------
# /users


# Query the DeepliftUser table and return a list of First and Last Names of all users in DB
def get_user_names(db: Session):
    return db.query(models.DeepliftUser.userName, models.DeepliftUser.firstName, models.DeepliftUser.lastName).all()


# Query the DeeplistUser table and return all information for a specific userName
def get_user_profile(db: Session, user_name: str):
    return db.query(models.DeepliftUser).filter(models.DeepliftUser.userName == user_name).first()


# Create a user with the given information
def create_user(db: Session, user: schemas.user.DeepliftUserCreate):
    join_date = date.today().isoformat()
    db_user = models.DeepliftUser(
        userName=user.userName,
        pw=user.pw,
        email=user.email,
        firstName=user.firstName,
        lastName=user.lastName,
        bodyweight=user.bodyweight,
        age=user.age,
        dateJoined=join_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_password(db: Session, user_name: str):
    return db.query(models.DeepliftUser.pw).filter(models.DeepliftUser.userName == user_name).first()


# Update a User with the new information
def update_user(db: Session, user: schemas.user.DeepliftUserCreate):
    user_instance = get_user_profile(db, user.userName)
    user_instance.firstName = user.firstName
    user_instance.lastName = user.lastName
    user_instance.bodyweight = user.bodyweight
    user_instance.age = user.age
    db.commit()
    return user_instance


# Delete a User
def delete_user(db: Session, user_name: str):
    user_instance = db.query(models.DeepliftUser).filter(models.DeepliftUser.userName == user_name)
    user_instance.delete()
    db.commit()
    return user_instance

# -----------------------------------------------------------------------------------------------------
# /workouts


# Query the Workout table and return all information for a specific workoutID
def get_workout(db: Session, workout_id: int):
    out = db.query(models.Workout).filter(
        models.Workout.workoutID == workout_id
    ).join(
        models.Exercise, models.Workout.exerciseID == models.Exercise.exerciseID
    ).first()

    out.exerciseName = out.exercise.exerciseName

    return out


# Query the Workout table and get all workouts for a specific userID
def get_user_workouts(db: Session, user_name: str):
    out = db.query(models.Workout).filter(
        models.Workout.userName == user_name
    ).join(
        models.Exercise, models.Workout.exerciseID == models.Exercise.exerciseID
    ).all()

    for e, i in enumerate(out):
        out[e].exerciseName = i.exercise.exerciseName

    return out


# Query the Workout table and get all workouts for a specific userID and exercise_id
def get_user_ex_wo(db: Session, user_name: str, ex_id: int):
    out = db.query(models.Workout).filter(
        models.Workout.userName == user_name
    ).filter(
        models.Workout.exerciseID == ex_id
    ).join(
        models.Exercise, models.Workout.exerciseID == models.Exercise.exerciseID
    ).all()

    for e, i in enumerate(out):
        out[e].exerciseName = i.exercise.exerciseName

    return out


# Query the Workout table and get all workouts for a specific userID and exercise_id
def get_user_date_wo(db: Session, user_name: str, date_recorded: str):
    out = db.query(models.Workout).filter(
        models.Workout.userName == user_name
    ).filter(
        models.Workout.dateRecorded == date_recorded
    ).join(
        models.Exercise, models.Workout.exerciseID == models.Exercise.exerciseID
    ).all()

    for e, i in enumerate(out):
        out[e].exerciseName = i.exercise.exerciseName

    return out


# Create a new workout for a user
def create_workout(db: Session, workout: schemas.workout.WorkoutCreate):
    workout_date = date.today().isoformat()
    db_workout = models.Workout(
        userName=workout.userName,
        reps=workout.reps,
        weight=workout.weight,
        exerciseID=workout.exerciseID,
        dateRecorded=workout_date,
        difficulty=workout.difficulty)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


# Update a workout with the new information
def update_workout(db: Session, workout: schemas.workout.WorkoutCreate):
    workout_instance = get_workout(db, workout.workoutID)
    workout_instance.exerciseID = workout.exerciseID
    workout_instance.reps = workout.reps
    workout_instance.weight = workout.weight
    workout_instance.difficulty = workout.difficulty
    db.commit()
    return workout_instance


# Delete a Workout
def delete_workout(db: Session, workout_id: int):
    workout_instance = db.query(models.Workout).filter(models.Workout.workoutID == workout_id)
    workout_instance.delete()
    db.commit()
    return workout_instance
# -----------------------------------------------------------------------------------------------------
# /exercises


# Query the Exercise table and return all information
def get_exercises(db: Session):
    return db.query(models.Exercise).all()

# -----------------------------------------------------------------------------------------------------
# Helper Functions


# Check if a user with the given email exists in the database
def user_email_exists(db: Session, email: str):
    user = db.query(models.DeepliftUser.userName).filter(
        models.DeepliftUser.email == email
    ).first()

    return user is not None


# Check if a user with the given username exists in the database
def user_username_exists(db: Session, user_name: str):
    user = db.query(models.DeepliftUser.userName).filter(
        models.DeepliftUser.userName == user_name
    ).first()

    return user is not None


# Check if a workout exists with the given workoutID
def workout_exists(db: Session, workoutID: int):
    workout = db.query(models.Workout.workoutID).filter(
        models.Workout.workoutID == workoutID
    ).first()

    return workout is not None
