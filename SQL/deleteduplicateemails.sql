DELETE FROM Person 
WHERE Id NOT IN (select min_id from (select min(Id) as min_id FROM Person GROUP BY Email) as xyz)