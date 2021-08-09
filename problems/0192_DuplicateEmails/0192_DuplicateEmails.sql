/*
Date        : 9 August 2021
Runtime     : 717 ms, faster than 5.03% of MySQL online submissions for Duplicate Emails
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.
*/

SELECT Email FROM Person
GROUP BY Email
HAVING Count(Email) > 1