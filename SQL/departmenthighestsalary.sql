# Write your MySQL query statement below
Select d.Name as Department, e.Name as Employee, e.Salary as Salary from Employee e inner join Department d on e.DepartmentId = d.Id where (d.Id, e.Salary) IN (Select e.DepartmentId, max(e.Salary) from Employee e group by e.DepartmentId) order by d.Name