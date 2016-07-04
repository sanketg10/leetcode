# Write your MySQL query statement below
-- SELECT p1.Num as ConsecutiveNums from Logs p1, Logs p2, Logs p3 WHERE p1.Num = p2.Num = p3.Num 

SELECT DISTINCT(p1.Num) as ConsecutiveNums from Logs p1, Logs p2, Logs p3 where (p2.Id = p1.Id + 1 and p2.Num = p1.Num) and (p3.Id = p1.Id + 2 and p3.Num = p1.Num) 