# Write your MySQL query statement below
-- select id from Weather
-- where Temperature 

-- previous_temp = temp

-- select ( CASE WHEN Temperature


-- for every id,   
-- see if temp[id] > previous_temp   
-- if yes then return id 
-- previous_temp = temp[id] 


select p1.Id as "Id" from Weather p1, Weather p2
WHERE DATEDIFF(p1.Date,p2.Date) = 1 AND p2.Temperature < p1.Temperature