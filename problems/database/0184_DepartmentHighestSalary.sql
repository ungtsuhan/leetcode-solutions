WITH max_salary_by_dept AS
(
    SELECT departmentId, MAX(salary) as salary FROM Employee
    GROUP BY departmentId
)
SELECT 
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
FROM Employee e
JOIN max_salary_by_dept m ON m.salary = e.salary AND m.departmentId = e.departmentId
LEFT JOIN Department d ON e.departmentId = d.id