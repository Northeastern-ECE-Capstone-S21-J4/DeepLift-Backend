CREATE PROCEDURE reset_workout_autoincrement()
BEGIN
      PREPARE stmt FROM 'ALTER TABLE Workout AUTO_INCREMENT = 1;';
      EXECUTE stmt;
      DEALLOCATE PREPARE stmt;
END