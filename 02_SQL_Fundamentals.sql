/*
================================================================================
                    SQL - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive SQL examples for Data Engineering interviews
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. BASIC QUERIES & FILTERING
2. JOINS (INNER, LEFT, RIGHT, FULL, CROSS, SELF)
3. AGGREGATIONS & GROUP BY
4. WINDOW FUNCTIONS (RANK, ROW_NUMBER, LAG, LEAD)
5. COMMON TABLE EXPRESSIONS (CTEs) & RECURSIVE QUERIES
6. SUBQUERIES & NESTED QUERIES
7. DATA MANIPULATION (INSERT, UPDATE, DELETE, MERGE/UPSERT)
8. DATA DEDUPLICATION
9. INCREMENTAL LOADS & WATERMARKING
10. DATE & TIME FUNCTIONS
11. STRING FUNCTIONS
12. ADVANCED PATTERNS & INTERVIEW QUESTIONS
13. DATABASE CONCEPTS (ACID, NORMALIZATION, INDEXES)
================================================================================
*/

-- ============================================================================
-- 1. BASIC QUERIES & FILTERING
-- ============================================================================

/* SQL Execution Order: FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT */

-- Basic SELECT
SELECT column1, column2 FROM table_name;

-- WHERE clause
SELECT * FROM employees WHERE salary > 50000;

-- Multiple conditions
SELECT * FROM employees 
WHERE salary > 50000 AND department = 'Sales' AND status = 'Active';

-- IN operator
SELECT * FROM employees WHERE department IN ('Sales', 'Marketing', 'IT');

-- BETWEEN operator
SELECT * FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

-- LIKE pattern matching
SELECT * FROM customers WHERE name LIKE 'A%';  -- Starts with A
SELECT * FROM customers WHERE email LIKE '%@gmail.com';  -- Ends with @gmail.com
SELECT * FROM customers WHERE name LIKE '%son%';  -- Contains 'son'

-- IS NULL / IS NOT NULL
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE email IS NOT NULL;

-- DISTINCT
SELECT DISTINCT department FROM employees;

-- ORDER BY
SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- LIMIT / TOP
SELECT * FROM employees ORDER BY salary DESC LIMIT 10;
SELECT TOP 10 * FROM employees ORDER BY salary DESC;  -- SQL Server

-- ============================================================================
-- 2. JOINS
-- ============================================================================

/* INNER JOIN - Returns matching rows from both tables */
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;

/* LEFT JOIN - Returns all rows from left table and matching rows from right */
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

/* RIGHT JOIN - Returns all rows from right table and matching rows from left */
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id;

/* FULL OUTER JOIN - Returns all rows from both tables */
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.department_id;

/* CROSS JOIN - Cartesian product */
SELECT * FROM table1 CROSS JOIN table2;

/* SELF JOIN - Join table with itself */
-- Find employee and their manager
SELECT e1.emp_name AS Employee, e2.emp_name AS Manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.emp_id;

/* Multiple JOIN conditions */
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id AND o.region = c.region;

/* LEFT ANTI JOIN - Rows in left table not in right table */
SELECT e.*
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE d.department_id IS NULL;

-- ============================================================================
-- 3. AGGREGATIONS & GROUP BY
-- ============================================================================

/* Basic Aggregations */
SELECT 
    COUNT(*) AS total_employees,
    COUNT(DISTINCT department) AS unique_departments,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary
FROM employees;

/* GROUP BY */
SELECT department, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

/* HAVING - Filter after aggregation */
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;

/* GROUP BY with multiple columns */
SELECT department, job_title, COUNT(*) AS count
FROM employees
GROUP BY department, job_title;

/* GROUP_CONCAT / STRING_AGG - Concatenate values */
-- MySQL
SELECT department, GROUP_CONCAT(name SEPARATOR ', ') AS employee_names
FROM employees
GROUP BY department;

-- PostgreSQL / SQL Server
SELECT department, STRING_AGG(name, ', ') AS employee_names
FROM employees
GROUP BY department;

/* Count NULL values */
SELECT 
    COUNT(*) AS total_rows,
    COUNT(CASE WHEN salary IS NULL THEN 1 END) AS null_salary_count,
    COUNT(CASE WHEN email IS NULL THEN 1 END) AS null_email_count
FROM employees;

/* COALESCE - Provide default value for NULL */
SELECT 
    employee_id,
    first_name,
    last_name,
    COALESCE(phone_number, 'No Phone') AS phone_number
FROM employees;

-- ============================================================================
-- 4. WINDOW FUNCTIONS (VERY IMPORTANT FOR INTERVIEWS)
-- ============================================================================

/* ROW_NUMBER - Assigns unique sequential number */
SELECT 
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM employees;

/* RANK - Assigns rank with gaps */
SELECT 
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;

/* DENSE_RANK - Assigns rank without gaps */
SELECT 
    name,
    department,
    salary,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank
FROM employees;

/* LAG - Access previous row value */
SELECT 
    sale_id,
    sale_date,
    amount,
    LAG(amount, 1) OVER (ORDER BY sale_date) AS previous_amount
FROM sales;

/* LEAD - Access next row value */
SELECT 
    sale_id,
    sale_date,
    amount,
    LEAD(amount, 1) OVER (ORDER BY sale_date) AS next_amount
FROM sales;

/* Running Total / Cumulative Sum */
SELECT 
    sale_date,
    amount,
    SUM(amount) OVER (ORDER BY sale_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM sales;

/* Moving Average (Last 3 days) */
SELECT 
    sale_date,
    amount,
    AVG(amount) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS three_day_avg
FROM sales;

/* NTILE - Divide into N buckets */
SELECT 
    name,
    salary,
    NTILE(4) OVER (ORDER BY salary) AS quartile
FROM employees;

/* FIRST_VALUE and LAST_VALUE */
SELECT 
    name,
    department,
    salary,
    FIRST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary) AS min_dept_salary,
    LAST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS max_dept_salary
FROM employees;

/* Find Nth Highest Salary by Department */
-- Method 1: Using DENSE_RANK
SELECT department, salary AS second_highest_salary
FROM (
    SELECT department, salary, DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
    FROM employees
) AS ranked_salaries
WHERE rank = 2;

-- Method 2: Using subquery
SELECT department, MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees AS e
    WHERE e.department = employees.department
)
GROUP BY department;

-- ============================================================================
-- 5. COMMON TABLE EXPRESSIONS (CTEs) & RECURSIVE QUERIES
-- ============================================================================

/* Basic CTE */
WITH Average_transaction AS (
    SELECT 
        cu.customer_name,
        ROUND(AVG(tr.amount), 2) AS avg_transaction,
        COUNT(*) AS transaction_count
    FROM customers cu
    JOIN transactions tr ON cu.customer_id = tr.customer_id
    WHERE tr.transaction_date BETWEEN '2023-09-01' AND '2023-09-30'
    GROUP BY cu.customer_name
)
SELECT customer_name, avg_transaction
FROM Average_transaction
WHERE transaction_count > 5;

/* Multiple CTEs */
WITH 
sales_summary AS (
    SELECT product_id, SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY product_id
),
product_info AS (
    SELECT product_id, product_name, category
    FROM products
)
SELECT p.product_name, p.category, s.total_quantity
FROM product_info p
JOIN sales_summary s ON p.product_id = s.product_id;

/* RECURSIVE CTE - Employee Hierarchy */
WITH RECURSIVE EmployeeHierarchy AS (
    -- Anchor member: Top-level managers
    SELECT employee_id, employee_name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive member: Employees reporting to managers
    SELECT e.employee_id, e.employee_name, e.manager_id, eh.level + 1
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM EmployeeHierarchy;

/* Find all employees under a specific manager */
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT emp_id, emp_name, manager_id
    FROM employees
    WHERE emp_id = 7  -- Starting manager
    
    UNION ALL
    
    SELECT e.emp_id, e.emp_name, e.manager_id
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.emp_id
)
SELECT * FROM EmployeeHierarchy;

/* Hierarchical Path */
WITH RECURSIVE EmployeePath AS (
    SELECT emp_id, emp_name, manager_id, CAST(emp_name AS VARCHAR(100)) AS path
    FROM employees
    WHERE emp_id = 1
    
    UNION ALL
    
    SELECT e.emp_id, e.emp_name, e.manager_id, CONCAT(ep.path, ' -> ', e.emp_name)
    FROM employees e
    INNER JOIN EmployeePath ep ON e.emp_id = ep.manager_id
)
SELECT * FROM EmployeePath;

/* Count Direct Reports for Each Manager */
SELECT m.emp_name AS Manager, COUNT(e.emp_id) AS DirectReports
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
GROUP BY m.emp_name
ORDER BY DirectReports DESC;

-- ============================================================================
-- 6. SUBQUERIES & NESTED QUERIES
-- ============================================================================

/* Subquery in WHERE clause */
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

/* Subquery in SELECT clause */
SELECT 
    name,
    salary,
    (SELECT AVG(salary) FROM employees) AS avg_salary,
    salary - (SELECT AVG(salary) FROM employees) AS diff_from_avg
FROM employees;

/* Correlated Subquery */
SELECT e1.name, e1.department, e1.salary
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department = e1.department
);

/* EXISTS */
SELECT c.customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);

/* NOT EXISTS */
SELECT c.customer_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);

/* IN with subquery */
SELECT name FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');

/* ALL operator */
SELECT name, salary
FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE department = 'Sales');

/* ANY operator */
SELECT name, salary
FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE department = 'Sales');

-- ============================================================================
-- 7. DATA MANIPULATION (INSERT, UPDATE, DELETE, MERGE/UPSERT)
-- ============================================================================

/* INSERT */
INSERT INTO employees (name, department, salary)
VALUES ('John Doe', 'IT', 75000);

/* INSERT multiple rows */
INSERT INTO employees (name, department, salary)
VALUES 
    ('Alice', 'Sales', 65000),
    ('Bob', 'Marketing', 70000);

/* INSERT from SELECT */
INSERT INTO employees_backup
SELECT * FROM employees WHERE hire_date < '2020-01-01';

/* UPDATE */
UPDATE employees
SET salary = salary * 1.1
WHERE department = 'Sales';

/* UPDATE with JOIN */
UPDATE e
SET e.department_name = d.name
FROM employees e
JOIN departments d ON e.department_id = d.id;

/* DELETE */
DELETE FROM employees WHERE status = 'Inactive';

/* TRUNCATE - Faster than DELETE, removes all rows */
TRUNCATE TABLE temp_table;

/* MERGE / UPSERT - Insert or Update */
-- SQL Server / PostgreSQL
MERGE INTO target_table AS target
USING source_table AS source
ON target.id = source.id
WHEN MATCHED THEN
    UPDATE SET 
        target.column1 = source.column1,
        target.column2 = source.column2
WHEN NOT MATCHED BY TARGET THEN
    INSERT (id, column1, column2)
    VALUES (source.id, source.column1, source.column2);

/* PostgreSQL UPSERT with ON CONFLICT */
INSERT INTO products (product_id, name, price)
VALUES (2, 'Smartphone', 650), (4, 'Smartwatch', 200)
ON CONFLICT (product_id) DO UPDATE SET
    name = EXCLUDED.name,
    price = EXCLUDED.price;

-- ============================================================================
-- 8. DATA DEDUPLICATION
-- ============================================================================

/* Remove duplicates using ROW_NUMBER */
WITH CTE AS (
    SELECT 
        emp_id,
        emp_name,
        manager_id,
        ROW_NUMBER() OVER (PARTITION BY emp_id, emp_name, manager_id ORDER BY emp_id) AS row_num
    FROM employees
)
SELECT emp_id, emp_name, manager_id
FROM CTE
WHERE row_num = 1;

/* Delete duplicates keeping one record */
DELETE FROM employees
WHERE id NOT IN (
    SELECT MIN(id)
    FROM employees
    GROUP BY name, department, salary
);

/* Identify duplicates */
SELECT name, department, salary, COUNT(*) AS cnt
FROM employees
GROUP BY name, department, salary
HAVING COUNT(*) > 1;

/* Deduplicate using QUALIFY (Snowflake) */
SELECT *
FROM employees
QUALIFY ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY updated_at DESC) = 1;

-- ============================================================================
-- 9. INCREMENTAL LOADS & WATERMARKING
-- ============================================================================

/* Identify new and updated records */
SELECT * 
FROM source_table 
WHERE last_updated > (SELECT MAX(last_updated) FROM target_table);

/* Insert incremental data */
INSERT INTO target_table (columns)
SELECT columns
FROM source_table 
WHERE last_updated > (SELECT MAX(last_updated) FROM target_table);

/* Incremental load with watermark table */
-- Create watermark table
CREATE TABLE watermark (
    table_name VARCHAR(100),
    last_processed_date TIMESTAMP
);

-- Get last processed date
SELECT last_processed_date 
FROM watermark 
WHERE table_name = 'orders';

-- Load incremental data
INSERT INTO target_orders
SELECT *
FROM source_orders
WHERE order_date > (
    SELECT last_processed_date 
    FROM watermark 
    WHERE table_name = 'orders'
);

-- Update watermark
UPDATE watermark
SET last_processed_date = CURRENT_TIMESTAMP
WHERE table_name = 'orders';

-- ============================================================================
-- 10. DATE & TIME FUNCTIONS
-- ============================================================================

/* Current Date and Time */
SELECT GETDATE() AS CurrentDateTime;  -- SQL Server
SELECT CURRENT_TIMESTAMP;  -- Standard SQL
SELECT NOW();  -- MySQL, PostgreSQL

/* Date Arithmetic */
-- SQL Server
SELECT DATEADD(day, 10, '2025-01-05') AS NewDate;  -- Add 10 days
SELECT DATEADD(month, -6, GETDATE()) AS SixMonthsAgo;

-- PostgreSQL / MySQL
SELECT DATE_ADD('2025-01-05', INTERVAL 10 DAY) AS NewDate;
SELECT DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH) AS SixMonthsAgo;

/* Date Difference */
-- SQL Server
SELECT DATEDIFF(day, '2025-01-01', '2025-01-05') AS DateDifference;  -- Returns 4

-- PostgreSQL
SELECT '2025-01-05'::date - '2025-01-01'::date AS DateDifference;

/* Extract Date Parts */
SELECT 
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    DAY(order_date) AS day,
    DATEPART(quarter, order_date) AS quarter,
    DATEPART(week, order_date) AS week
FROM orders;

/* Format Date */
SELECT FORMAT(GETDATE(), 'yyyy-MM-dd') AS formatted_date;  -- SQL Server
SELECT TO_CHAR(CURRENT_DATE, 'YYYY-MM-DD') AS formatted_date;  -- PostgreSQL

/* Customers who ordered in last 6 months */
SELECT customer_id, COUNT(*) AS order_count
FROM orders
WHERE order_date >= DATEADD(MONTH, -6, GETDATE())
GROUP BY customer_id
ORDER BY order_count DESC;

/* Average date difference between transactions */
SELECT 
    c.customer_id,
    c.name,
    AVG(DATEDIFF(DAY, LAG(t.date) OVER (PARTITION BY t.customer_id ORDER BY t.date), t.date)) AS avg_days_between
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
WHERE t.date >= DATEADD(YEAR, -1, GETDATE())
GROUP BY c.customer_id, c.name;

/* Consecutive login days streak */
WITH d AS (
    SELECT DISTINCT emp_id, CAST(login_dt AS DATE) AS login_dt
    FROM emp_logins
),
grp AS (
    SELECT 
        emp_id,
        login_dt,
        DATEADD(day, -ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY login_dt), login_dt) AS grp_key
    FROM d
),
streaks AS (
    SELECT emp_id, grp_key, COUNT(*) AS streak_days
    FROM grp
    GROUP BY emp_id, grp_key
)
SELECT emp_id, MAX(streak_days) AS longest_streak
FROM streaks
GROUP BY emp_id
HAVING MAX(streak_days) >= 5;

-- ============================================================================
-- 11. STRING FUNCTIONS
-- ============================================================================

/* CONCAT */
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;

/* SUBSTRING */
SELECT SUBSTRING(name, 1, 3) AS short_name FROM employees;

/* UPPER / LOWER */
SELECT UPPER(name) AS upper_name, LOWER(name) AS lower_name FROM employees;

/* TRIM / LTRIM / RTRIM */
SELECT TRIM(name) AS trimmed_name FROM employees;

/* REPLACE */
SELECT REPLACE(phone, '-', '') AS clean_phone FROM employees;

/* LENGTH / LEN */
SELECT name, LENGTH(name) AS name_length FROM employees;  -- PostgreSQL
SELECT name, LEN(name) AS name_length FROM employees;  -- SQL Server

/* CHARINDEX / POSITION */
SELECT CHARINDEX('@', email) AS at_position FROM employees;  -- SQL Server
SELECT POSITION('@' IN email) AS at_position FROM employees;  -- PostgreSQL

/* LEFT / RIGHT */
SELECT LEFT(name, 3) AS first_three FROM employees;
SELECT RIGHT(name, 3) AS last_three FROM employees;

/* SPLIT_PART (PostgreSQL) */
SELECT SPLIT_PART(email, '@', 1) AS username FROM employees;

-- ============================================================================
-- 12. ADVANCED PATTERNS & INTERVIEW QUESTIONS
-- ============================================================================

/* Symmetric Difference between two tables */
SELECT * FROM tableA
WHERE (id, value) NOT IN (SELECT id, value FROM tableB)
UNION
SELECT * FROM tableB
WHERE (id, value) NOT IN (SELECT id, value FROM tableA);

/* Pivot - Convert rows to columns */
SELECT *
FROM (
    SELECT student, subject, marks
    FROM student_marks
) AS source
PIVOT (
    SUM(marks)
    FOR subject IN ([Math], [Science], [English])
) AS pivot_table;

/* Find gaps in sequence */
SELECT 
    id,
    LEAD(id) OVER (ORDER BY id) AS next_id,
    LEAD(id) OVER (ORDER BY id) - id - 1 AS gap_size
FROM table_name
WHERE LEAD(id) OVER (ORDER BY id) - id > 1;

/* Top N per group */
WITH RankedSales AS (
    SELECT 
        product_id,
        sale_date,
        amount,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY amount DESC) AS rn
    FROM sales
)
SELECT product_id, sale_date, amount
FROM RankedSales
WHERE rn <= 3;

/* Running total with reset */
SELECT 
    category,
    date,
    amount,
    SUM(amount) OVER (PARTITION BY category ORDER BY date) AS running_total
FROM transactions;

/* Find employees who have at least one subordinate */
SELECT DISTINCT e1.emp_name
FROM employees e1
JOIN employees e2 ON e1.emp_id = e2.manager_id;

/* Customers with no orders */
SELECT c.customer_id, c.customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

/* Self-referencing to find employees earning more than their manager */
SELECT e.name AS employee, e.salary AS emp_salary, m.name AS manager, m.salary AS mgr_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;

/* Concatenate members per team (LISTAGG / STRING_AGG) */
SELECT
    team,
    LISTAGG(member, ', ') WITHIN GROUP (ORDER BY member) AS members
FROM my_table
GROUP BY team;

-- ============================================================================
-- 13. DATABASE CONCEPTS
-- ============================================================================

/*
ACID PROPERTIES:
- Atomicity: All or nothing - transaction either completes fully or not at all
- Consistency: Database remains in valid state before and after transaction
- Isolation: Concurrent transactions don't interfere with each other
- Durability: Committed changes are permanent

NORMALIZATION:
- 1NF: Eliminate repeating groups, atomic values
- 2NF: Remove partial dependencies
- 3NF: Remove transitive dependencies
- BCNF: Every determinant is a candidate key

INDEXES:
- Clustered Index: Determines physical order of data (one per table)
- Non-Clustered Index: Separate structure with pointers to data
- Composite Index: Index on multiple columns
- Unique Index: Ensures uniqueness

CONSTRAINTS:
- PRIMARY KEY: Uniquely identifies each row
- FOREIGN KEY: Establishes relationship between tables
- UNIQUE: Ensures all values in column are different
- NOT NULL: Column cannot have NULL values
- CHECK: Validates data based on condition
- DEFAULT: Provides default value

JOINS PERFORMANCE:
- Use indexes on join columns
- Filter early with WHERE clause
- Use appropriate join type
- Consider denormalization for read-heavy workloads

FACT vs DIMENSION TABLES:
- Fact Table: Contains quantitative data (measures) and foreign keys
- Dimension Table: Contains descriptive attributes

SLOWLY CHANGING DIMENSIONS (SCD):
- Type 0: Fixed, never changes
- Type 1: Overwrite old data
- Type 2: Add new row, preserve history
- Type 3: Add new column for previous value
- Type 4: Separate history table
- Type 6: Hybrid (1+2+3)
*/

/* Create Primary Key */
ALTER TABLE employees ADD PRIMARY KEY (employee_id);

/* Create Foreign Key */
ALTER TABLE employees 
ADD CONSTRAINT fk_department 
FOREIGN KEY (department_id) REFERENCES departments(department_id);

/* Create Index */
CREATE INDEX idx_employee_name ON employees(name);
CREATE UNIQUE INDEX idx_employee_email ON employees(email);
CREATE INDEX idx_composite ON employees(department_id, salary);

/* Create Trigger (Audit Log) */
CREATE TRIGGER AfterSalaryUpdate
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary <> OLD.salary THEN
        INSERT INTO audit_log (employee_id, old_salary, new_salary, change_date)
        VALUES (OLD.employee_id, OLD.salary, NEW.salary, NOW());
    END IF;
END;

/* Create View */
CREATE VIEW active_employees AS
SELECT employee_id, name, department, salary
FROM employees
WHERE status = 'Active';

/* Materialized View (PostgreSQL) */
CREATE MATERIALIZED VIEW sales_summary AS
SELECT product_id, SUM(quantity) AS total_quantity, SUM(amount) AS total_amount
FROM sales
GROUP BY product_id;

-- Refresh materialized view
REFRESH MATERIALIZED VIEW sales_summary;

/*
================================================================================
END OF SQL INTERVIEW GUIDE
================================================================================
*/
