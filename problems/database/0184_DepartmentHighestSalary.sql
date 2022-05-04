WITH max_salary_by_dept AS
(
    SELECT departmentId, MAX(salary) AS salary FROM Employee
    GROUP BY departmentId
)
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN max_salary_by_dept m ON m.salary = e.salary AND m.departmentId = e.departmentId
LEFT JOIN Department d ON e.departmentId = d.id