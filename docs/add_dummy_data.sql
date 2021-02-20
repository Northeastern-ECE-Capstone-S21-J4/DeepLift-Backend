USE deeplift;

INSERT INTO DeepliftUser (userName, firstName, lastName, email, bodyweight, age, dateJoined) VALUES
('joemama', 'Joe', 'Mama', 'joewho@gmail.com', 180, 21, '2021-02-4'),
('skinnymike', 'Skinny', 'Mike', 'twig@hotmail.com', 23, 18, '2021-02-4'),
('bigjohn', 'Big', 'John', 'massiveguy@gmail.com', 645, 37, '2021-02-4');

INSERT INTO Exercise (exerciseName) VALUES
('Squat'),
('Bench'),
('Deadlift');

INSERT INTO Workout (userName, reps, weight, exerciseID, dateRecorded, difficulty) VALUES
('joemama', 10, 135, 1, '2021-02-4', 4),
('skinnymike', 12, 225, 2, '2021-02-4', 7),
('skinnymike', 8, 225, 2, '2021-02-4', 9),
('bigjohn', 8, 95, 3, '2021-02-4', 5);
