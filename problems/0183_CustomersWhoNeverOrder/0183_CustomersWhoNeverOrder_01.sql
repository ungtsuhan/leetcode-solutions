/*
Date        : 10 August 2021
Runtime     : 919 ms, faster than 62.67% of MS SQL Server online submissions for Customers Who Never Order.
Memory Usage: 0B, less than 100.00% of MS SQL Server online submissions for Customers Who Never Order.
*/

SELECT c.Name AS Customers FROM Customers c
LEFT JOIN Orders o ON c.Id = o.CustomerId
WHERE o.Id IS NULL