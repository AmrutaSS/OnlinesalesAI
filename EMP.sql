""" Task-1 SQL """

SELECT d.DEPT_NAME, AVG(s.MONTHLY_SALARY) AS AVG_MONTHLY_SALARY
FROM departments d
JOIN employees e ON d.DEPT_ID = e.DEPT_ID
JOIN salaries s ON e.EMP_ID = s.EMP_ID
GROUP BY d.DEPT_NAME
ORDER BY AVG_MONTHLY_SALARY DESC
LIMIT 3;