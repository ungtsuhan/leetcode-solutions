/*
Date        : 12 August 2021
Runtime     : 763 ms, faster than 99.80% of MS SQL Server online submissions for Rising Temperature.
Memory Usage: 0B, less than 100.00% of MS SQL Server online submissions for Rising Temperature.
*/

SELECT w1.id AS Id FROM Weather w1
JOIN Weather w2 ON w1.recordDate = DATEADD(DAY, 1, w2.recordDate)
WHERE w1.temperature > w2.temperature