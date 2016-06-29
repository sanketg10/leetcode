SELECT E.Name as "Employee" FROM Employee as E inner join Employee as M on E.ManagerId=M.Id WHERE E.Salary>M.Salary
