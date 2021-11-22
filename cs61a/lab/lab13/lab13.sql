.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';
  

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest AS temp FROM students GROUP BY temp HAVING COUNT (temp) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b WHERE a.pet = b.pet AND a.song = b.song AND a.time != b.time;


CREATE TABLE sevens AS
  SELECT seven FROM students, numbers WHERE students.number = 7 AND numbers.'7' = 'True' AND students.time = numbers.time;


CREATE TABLE avg_difference AS
  SELECT ROUND(AVG(ABS(number - smallest))) FROM students;

