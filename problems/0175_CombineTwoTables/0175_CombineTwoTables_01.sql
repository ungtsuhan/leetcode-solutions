/*
Date        : 9 August 2021
Runtime     : 852 ms, faster than 88.33% of MS SQL Server online submissions for Combine Two Tables.
Memory Usage: 0B, less than 100.00% of MS SQL Server online submissions for Combine Two Tables.
*/

SELECT 
    p.FirstName,
    p.LastName,
    a.City,
    a.State
FROM Person p
LEFT JOIN Address a ON p.PersonId = a.PersonId