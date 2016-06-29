# Write your MySQL query statement below
select Max(Salary) as SecondHighestSalary from Employee where Salary < (select max(Salary) from Employee) 

-- select(select Salary as SecondHighestSalary from Employee Order by Salary DESC limit 1,1) 