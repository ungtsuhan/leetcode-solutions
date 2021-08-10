/*
Date        : 10 August 2021
Runtime     : 1698 ms, faster than 44.39% of MySQL online submissions for Delete Duplicate Emails.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
*/

DELETE p1 FROM Person p1, Person p2 -- join table with itself on Email Column
WHERE p1.Email = p2.Email AND p1.Id > p2.Id