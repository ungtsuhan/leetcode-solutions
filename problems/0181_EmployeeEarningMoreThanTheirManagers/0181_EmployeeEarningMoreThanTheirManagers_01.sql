/*
Date        : 9 August 2021
Runtime     : 894 ms, faster than 90.77% of MS SQL Server online submissions for Employees Earning More Than Their Managers.
Memory Usage: 0B, less than 100.00% of MS SQL Server online submissions for Employees Earning More Than Their Managers.
*/

SELECT te.Name AS Employee
FROM Employee te
LEFT JOIN Employee tm ON te.ManagerId = tm.Id
WHERE 
    te.ManagerId IS NOT NULL
    AND te.Salary > tm.Salary