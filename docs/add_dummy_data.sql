USE deeplift;

INSERT INTO DeepliftUser (firstName, lastName, email, bodyweight, age, dateJoined) VALUES
('Joe', 'Mama', 'joewho@gmail.com', 180, 21, '2021-02-4'),
('Skinny', 'Mike', 'twig@hotmail.com', 23, 18, '2021-02-4'),
('Fat', 'John', 'massiveguy@gmail.com', 645, 37, '2021-02-4');

INSERT INTO Exercise (exerciseName) VALUES
('Squat'),
('Bench'),
('Deadlift');

INSERT INTO Workout (userID, reps, weight, exerciseID, dateRecorded, difficulty) VALUES
(1, 10, 135, 1, '2021-02-4', 4),
(2, 12, 225, 2, '2021-02-4', 7),
(2, 8, 225, 2, '2021-02-4', 9),
(3, 8, 95, 3, '2021-02-4', 5);