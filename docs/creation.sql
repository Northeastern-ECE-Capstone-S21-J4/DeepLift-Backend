CREATE DATABASE IF NOT EXISTS deeplift;
USE deeplift;

DROP TABLE IF EXISTS Workout;
DROP TABLE IF EXISTS DeepliftUser;
DROP TABLE IF EXISTS Exercise;

# A table representing a user of our application
CREATE TABLE DeepliftUser (
userName VARCHAR(50) NOT NULL PRIMARY KEY,
pw CHAR(64) NOT NULL,
firstName VARCHAR(50) NOT NULL,
lastName VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL UNIQUE,
bodyweight INT NOT NULL,
age INT NOT NULL,
dateJoined DATE NOT NULL,
CHECK (bodyweight > 0),
CHECK (age >= 18)
);

CREATE TABLE UserLifting (
userName VARCHAR(50) NOT NULL PRIMARY KEY,
currentlyLifting BOOLEAN NOT NULL,
difficulty INT NOT NULL,
CHECK ((difficulty > 0 AND difficulty <= 10) OR difficulty = -1),
FOREIGN KEY (userName) REFERENCES DeepliftUser(userName) ON DELETE CASCADE ON UPDATE CASCADE
);

# A table representing an exercise that can be performed
CREATE TABLE Exercise (
exerciseID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
exerciseName VARCHAR(25) NOT NULL UNIQUE
);

# A table representing a user's set (1)
CREATE TABLE Workout (
workoutID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
userName VARCHAR(50) NOT NULL,
reps INT NOT NULL,
weight INT NOT NULL,
exerciseID INT NOT NULL,
dateRecorded DATE NOT NULL,
difficulty INT NOT NULL,
CHECK ((difficulty > 0 AND difficulty <= 10) OR difficulty = -1),
CHECK (reps > 0),
CHECK ((weight > 0) OR weight IS NULL),
FOREIGN KEY (exerciseID) REFERENCES Exercise(exerciseID) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (userName) REFERENCES DeepliftUser(userName) ON DELETE CASCADE ON UPDATE CASCADE
);
