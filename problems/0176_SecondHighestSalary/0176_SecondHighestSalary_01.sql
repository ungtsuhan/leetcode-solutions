/*
Date        : 9 August 2021
Runtime     : 852 ms, faster than 73.50% of MS SQL Server online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MS SQL Server online submissions for Second Highest Salary.
*/

SELECT MAX(Salary) AS SecondHighestSalary 
FROM Employee
WHERE ((Salary) < (SELECT Max(Salary) From Employee))
