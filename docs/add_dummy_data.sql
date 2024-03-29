USE deeplift;

INSERT INTO DeepliftUser (userName, pw, firstName, lastName, email, bodyweight, age, dateJoined) VALUES
('joemama', '5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8', 'Joe', 'Mama', 'joewho@gmail.com', 180, 21, '2021-02-4'),
('skinnymike', '5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8', 'Skinny', 'Mike', 'twig@hotmail.com', 23, 18, '2021-02-4'),
('bigjohn', '5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8', 'Big', 'John', 'massiveguy@gmail.com', 645, 37, '2021-02-4'),
('yajingwang1022', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'Yajing', 'Wang', 'yajingwang1022@gmail.com', 120, 23, '2021-03-28');

INSERT INTO UserLifting (userName, currentlyLifting, difficulty) VALUES
('joemama', FALSE, -1),
('skinnymike', FALSE, -1),
('bigjohn', FALSE, -1),
('yajingwang1022', FALSE, -1);

INSERT INTO Exercise (exerciseName) VALUES
('Squat'),
('Bench'),
('Deadlift');

INSERT INTO Workout (userName, reps, weight, exerciseID, dateRecorded, difficulty) VALUES
('joemama', 10, 135, 1, '2021-02-4', 4),
('skinnymike', 12, 225, 2, '2021-02-4', 7),
('skinnymike', 8, 225, 2, '2021-02-4', 9),
('bigjohn', 8, 95, 3, '2021-02-4', 5);
