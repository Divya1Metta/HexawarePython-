![WhatsApp Image 2024-04-29 at 16 33 10_77e7820b](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/48be7bfa-6da8-4835-a2d9-5958ab399b49)


# JOIN

| Join Type     | Features                                                      | Significance                                                 | Example                                                         | Generated Table and Explanation                                                                                                                                                                           |
|---------------|---------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INNER JOIN    | - Returns rows where there is a match in both tables         | - Most commonly used join type                               | ```sql SELECT * FROM table1 INNER JOIN table2 ON table1.key = table2.key;```  | **Example:** Suppose we have two tables, "employees" and "departments", and we want to retrieve employees along with their departments. An inner join will return only those rows where there is a match in both tables. |
| LEFT JOIN     | - Returns all rows from the left table, and matched rows from the right table | - Ensures all rows from the left table are included         | ```sql SELECT * FROM table1 LEFT JOIN table2 ON table1.key = table2.key;```   | **Example:** Similar to INNER JOIN, but ensures all rows from the left table are included, even if there are no matches in the right table.                                                                  |
| RIGHT JOIN    | - Returns all rows from the right table, and matched rows from the left table | - Similar to LEFT JOIN, but ensures all rows from the right table are included | ```sql SELECT * FROM table1 RIGHT JOIN table2 ON table1.key = table2.key;```  | **Example:** Similar to LEFT JOIN, but ensures all rows from the right table are included, even if there are no matches in the left table.                                                                 |
| FULL JOIN     | - Returns all rows when there is a match in either table      | - Ensures all rows from both tables are included             | ```sql SELECT * FROM table1 FULL JOIN table2 ON table1.key = table2.key;```   | **Example:** Returns all rows from both tables, combining the result of both LEFT and RIGHT JOIN.                                                                                                                                                                       |
| CROSS JOIN    | - Returns the Cartesian product of the two tables             | - Useful for generating combinations of all rows             | ```sql SELECT * FROM table1 CROSS JOIN table2;```                           | **Example:** Returns all possible combinations of rows from both tables.                                                                                                                                                                                                 |
| Equi Join     | - Special case of INNER JOIN where columns in both tables are compared using equality operator | - Used to match rows based on equality of specified columns  | ```sql SELECT * FROM employees e JOIN departments d ON e.department_id = d.department_id;```  | **Example:** Suppose we want to join the "employees" table with the "departments" table based on the "department_id" column to fetch the department name for each employee.                                  |
| Self Join     | - Joining a table to itself                                   | - Used to compare rows within the same table                 | ```sql SELECT e1.name, e2.name FROM employees e1 JOIN employees e2 ON e1.manager_id = e2.employee_id;``` | **Example:** Suppose the "employees" table has a "manager_id" column indicating the ID of the employee's manager. We can use a self-join to retrieve each employee's manager's name.                   |
| Natural Join  | - Automatically joins two tables based on columns with the same name | - Simplifies the join syntax by automatically identifying matching columns | ```sql SELECT * FROM employees NATURAL JOIN departments;```                | **Example:** Automatically joins the "employees" and "departments" tables based on columns with the same name (e.g., "department_id").                                                                                                                                 |


## Inner Join Example:
**Query:**
```sql
SELECT * 
FROM employees e 
INNER JOIN departments d ON e.department_id = d.department_id;
```

**Generated Table:**
| employee_id | name   | department_id | department_id | department_name |
|-------------|--------|---------------|---------------|-----------------|
| 1           | Alice  | 1             | 1             | Engineering     |
| 2           | Bob    | 1             | 1             | Engineering     |
| 3           | Charlie| 2             | 2             | HR              |
| 4           | David  | 3             | NULL          | NULL            |
| 5           | Sneha  | 1             | 1             | Engineering     |

**Explanation:**
This example joins the "employees" table with the "departments" table based on the "department_id" column. It returns all columns from both tables where there is a match in the "department_id" column. The result includes employees along with their corresponding department information.

## Left Join Example:
**Query:**
```sql
SELECT * 
FROM employees e 
LEFT JOIN departments d ON e.department_id = d.department_id;
```

**Generated Table:**
| employee_id | name   | department_id | department_id | department_name |
|-------------|--------|---------------|---------------|-----------------|
| 1           | Alice  | 1             | 1             | Engineering     |
| 2           | Bob    | 1             | 1             | Engineering     |
| 3           | Charlie| 2             | 2             | HR              |
| 4           | David  | 3             | NULL          | NULL            |
| 5           | Sneha  | 1             | 1             | Engineering     |

**Explanation:**
This example performs a left join between the "employees" table and the "departments" table based on the "department_id" column. It includes all rows from the left table (employees) and only matching rows from the right table (departments). If there is no match in the right table, NULL values are included in the result.

## Right Join Example:
**Query:**
```sql
SELECT * 
FROM employees e 
RIGHT JOIN departments d ON e.department_id = d.department_id;
```

**Generated Table:**
| employee_id | name   | department_id | department_id | department_name |
|-------------|--------|---------------|---------------|-----------------|
| 1           | Alice  | 1             | 1             | Engineering     |
| 2           | Bob    | 1             | 1             | Engineering     |
| 3           | Charlie| 2             | 2             | HR              |
| NULL        | NULL   | NULL          | 3             | Marketing       |

**Explanation:**
This example performs a right join between the "employees" table and the "departments" table based on the "department_id" column. It includes all rows from the right table (departments) and only matching rows from the left table (employees). If there is no match in the left table, NULL values are included in the result.

## Full Join Example:
**Query:**
```sql
SELECT * 
FROM employees e 
FULL JOIN departments d ON e.department_id = d.department_id;
```

**Generated Table:**
| employee_id | name   | department_id | department_id | department_name |
|-------------|--------|---------------|---------------|-----------------|
| 1           | Alice  | 1             | 1             | Engineering     |
| 2           | Bob    | 1             | 1             | Engineering     |
| 3           | Charlie| 2             | 2             | HR              |
| 4           | David  | 3             | NULL          | NULL            |
| 5           | Sneha  | 1             | 1             | Engineering     |
| NULL        | NULL   | NULL          | 3             | Marketing       |

**Explanation:**
This example performs a full outer join between the "employees" table and the "departments" table based on the "department_id" column. It includes all rows from both tables, and if there is no match in one table, NULL values are included in the result for the corresponding columns from the other table.

## Cross Join Example:
**Query:**
```sql
SELECT * 
FROM employees e 
CROSS JOIN departments d;
```

**Generated Table:**
| employee_id | name   | department_id | department_id | department_name |
|-------------|--------|---------------|---------------|-----------------|
| 1           | Alice  | 1             | 1             | Engineering     |
| 1           | Alice  | 1             | 2             | HR              |
| 1           | Alice  | 1             | 3             | Marketing       |
| 2           | Bob    | 2             | 1             | Engineering     |
| 2           | Bob    | 2             | 2             | HR              |
| 2           | Bob    | 2             | 3             | Marketing       |
| 3           | Charlie| 3             | 1             | Engineering     |
| 3           | Charlie| 3             | 2             | HR              |
| 3           | Charlie| 3             | 3             | Marketing       |
| 4           | David  | NULL          | 1             | Engineering     |
| 4           | David  | NULL          | 2             | HR              |
| 4           | David  | NULL          | 3             | Marketing       |
| 5           | Sneha  | 1             | 1             | Engineering     |
| 5           | Sneha  | 1             | 2             | HR              |
| 5           | Sneha  | 1             | 3             | Marketing       |

**Explanation:**
This example performs a cross join (also known as a Cartesian join) between the "employees" table and the "departments" table. It returns all possible combinations of rows from both tables, resulting in a table with a number of rows equal to the product of the number of rows in each table.

## Equi Join Example:
**Query:**
```sql
SELECT e.name, d.department_name 
FROM employees e 
JOIN departments d ON e.department_id = d.department_id;
```

**Generated Table:**
| name     | department_name |
|----------|-----------------|
| Alice    | Engineering     |
| Bob      | Engineering     |
| Charlie  | HR              |
| Sneha    | Engineering     |

**Explanation:**
This example performs an equi join between the "employees" table and the "departments" table based on the "department_id" column. It returns the names of employees along with their corresponding department names, where there is a match in the "department_id" column.

## Self Join Example:
**Query:**
```sql
SELECT e1.name AS employee_name, e2.name AS manager_name 
FROM employees e1 
JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

**Generated Table:**
| employee_name | manager_name |
|---------------|--------------|
| Bob           | Alice        |
| Charlie       | Alice        |
| Sneha         | Bob          |

**Explanation:**
This example performs a self join on the "employees" table to retrieve the names of employees along with the names of their respective managers. It matches rows within the same table based on the "manager_id" column (which indicates the ID of the employee's manager).

## Natural Join Example:
**Query:**
```sql
SELECT * 
FROM employees 
NATURAL JOIN departments;
```

**Generated Table:**
| employee_id | name   | department_id | department_name |
|-------------|--------|---------------|-----------------|
| 1           | Alice  | 1             | Engineering     |
| 2           | Bob    | 1             | Engineering     |
| 3           | Charlie| 2             | HR              |
| 5           | Sneha  | 1             | Engineering     |

**Explanation:**
This example performs a natural join between the "employees" and "departments" tables. It automatically joins the tables based on columns with the same name (e.g., "department_id"). The result includes all columns from both tables where there is a matching column name.

## Outer Apply Example:
**Query:**
```sql
SELECT e.name, d.department_name 
FROM employees e 
OUTER APPLY (
    SELECT *
    FROM departments d
    WHERE e.department_id = d.department_id
) AS d;
```

**Generated Table:**
| name     | department_name |
|----------|-----------------|
| Alice    | Engineering     |
| Bob      | Engineering     |
| Charlie  | HR              |
| Sneha    | Engineering     |
| David    | NULL            |

**Explanation:**
This example uses the OUTER APPLY operator to perform an outer join-like operation between the "employees" and "departments" tables. It returns all rows from the left table (employees) and the result of the correlated subquery (departments), matching rows where the department IDs are equal. If there is no match in the subquery, NULL values are included in the result for the corresponding columns.

## Cross Apply Example:
**Query:**
```sql
SELECT e.name, d.department_name 
FROM employees e 
CROSS APPLY (
    SELECT *
    FROM departments d
    WHERE e.department_id = d.department_id
) AS d;
```

**Generated Table:**
| name     | department_name |
|----------|-----------------|
| Alice    | Engineering     |
| Bob      | Engineering     |
| Charlie  | HR              |
| Sneha    | Engineering     |

**Explanation:**
This example uses the CROSS APPLY operator to perform a cross join-like operation between the "employees" and "departments" tables, with an additional condition specified in the correlated subquery. It returns all possible combinations of rows from both tables where the department IDs are equal.
# EXISTS VS NOT EXISTS

### Step 1: Initial Setup and Data Insertion
```sql
CREATE DATABASE projects;
USE projects;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    employee_id INT,
    start_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees (employee_id, name, department) VALUES 
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Engineering'),
(3, 'Charlie', 'HR'),
(4, 'David', 'Marketing'),
(5, 'Sneha', 'Engineering');

INSERT INTO projects (project_id, project_name, employee_id, start_date) VALUES 
(101, 'Alpha', 1, '2021-01-10'),
(102, 'Beta', 2, '2021-03-15'),
(103, 'Gamma', 1, '2021-02-20');
```

### Step 2: View Data from Tables
```sql
SELECT * FROM employees;
```
**Generated Employees Table:**
| employee_id | name   | department   |
|-------------|--------|--------------|
| 1           | Alice  | Engineering  |
| 2           | Bob    | Engineering  |
| 3           | Charlie| HR           |
| 4           | David  | Marketing    |
| 5           | Sneha  | Engineering  |

```sql
SELECT * FROM projects;
```
**Generated Projects Table:**
| project_id | project_name | employee_id | start_date |
|------------|--------------|-------------|------------|
| 101        | Alpha        | 1           | 2021-01-10 |
| 102        | Beta         | 2           | 2021-03-15 |
| 103        | Gamma        | 1           | 2021-02-20 |


### Step 3: Query Employees from Engineering Department Working on Projects
```sql
SELECT * 
FROM employees o
WHERE department = 'Engineering' 
AND EXISTS (
    SELECT * 
    FROM projects i 
    WHERE o.employee_id = i.employee_id
);
```

#### Explanation:
- **Intuition/Approach:** We want to find employees from the Engineering department who are actively involved in projects. To do this, we'll use the `EXISTS` operator to check if there are any records in the "projects" table for each employee in the Engineering department.
- **Code Breakdown:**
  - The outer query selects all columns from the "employees" table and aliases it as `o`.
  - We filter the results to include only employees from the Engineering department (`WHERE department = 'Engineering'`).
  - The `EXISTS` operator is used to check if there's at least one row in the "projects" table (`i`) where the `employee_id` matches with that of the outer query's employee (`o.employee_id`).
  - If such a row exists, the employee is included in the result.

### Step 4: Query Employees from Engineering Department Not Working on Any Project
```sql
SELECT * 
FROM employees o
WHERE department = 'Engineering' 
AND NOT EXISTS (
    SELECT * 
    FROM projects i 
    WHERE o.employee_id = i.employee_id
);
```

#### Explanation:
- **Intuition/Approach:** Here, we want to identify employees from the Engineering department who are not assigned to any project. We'll use the `NOT EXISTS` operator to filter out employees who have no corresponding records in the "projects" table.
- **Code Breakdown:**
  - Similar to Step 3, the outer query selects all columns from the "employees" table and aliases it as `o`.
  - We again filter the results to include only employees from the Engineering department (`WHERE department = 'Engineering'`).
  - The `NOT EXISTS` operator checks if there are no rows in the "projects" table (`i`) where the `employee_id` matches with that of the outer query's employee (`o.employee_id`).
  - If no such row exists, the employee is included in the result.

#### Operators Explanation:
- **EXISTS:** This operator checks if a subquery returns any rows. If the subquery returns at least one row, the result of the EXISTS operator is true, otherwise false.
- **NOT EXISTS:** This operator is the negation of EXISTS. It returns true if the subquery returns no rows.
# GROUP By & ORDER BY

## Create Table
```sql
CREATE TABLE EmployeeSales (
    EmployeeID INT,
    Region VARCHAR(50),
    Category VARCHAR(50),
    Quarter VARCHAR(10),
    SalesAmount DECIMAL(10,2)
);
```

## Insert Values
```sql
INSERT INTO EmployeeSales (EmployeeID, Region, Category, Quarter, SalesAmount)
VALUES
    (101, 'North', 'Electronics', 'Q1', 1200.00),
    (101, 'North', 'Electronics', 'Q2', 1500.00),
    (102, 'North', 'Clothing', 'Q1', 800.00),
    (102, 'North', 'Clothing', 'Q2', 950.00),
    (103, 'South', 'Electronics', 'Q1', 1000.00),
    (103, 'South', 'Clothing', 'Q1', 1200.00),
    (104, 'East', 'Electronics', 'Q2', 1150.00),
    (104, 'East', 'Clothing', 'Q2', 500.00),
    (105, 'West', 'Electronics', 'Q1', 1900.00),
    (105, 'West', 'Clothing', 'Q1', 1100.00),
    (105, 'West', 'Electronics', 'Q2', 2100.00),
    (105, 'West', 'Clothing', 'Q2', 1300.00);
```

### Generated Table:

| EmployeeID | Region | Category    | Quarter | SalesAmount |
|------------|--------|-------------|---------|-------------|
| 101        | North  | Electronics | Q1      | 1200.00     |
| 101        | North  | Electronics | Q2      | 1500.00     |
| 102        | North  | Clothing    | Q1      | 800.00      |
| 102        | North  | Clothing    | Q2      | 950.00      |
| 103        | South  | Electronics | Q1      | 1000.00     |
| 103        | South  | Clothing    | Q1      | 1200.00     |
| 104        | East   | Electronics | Q2      | 1150.00     |
| 104        | East   | Clothing    | Q2      | 500.00      |
| 105        | West   | Electronics | Q1      | 1900.00     |
| 105        | West   | Clothing    | Q1      | 1100.00     |
| 105        | West   | Electronics | Q2      | 2100.00     |
| 105        | West   | Clothing    | Q2      | 1300.00     |

### Queries

#### Query 1: Order by Region, SalesAmount desc

```sql
SELECT *
FROM EmployeeSales
ORDER BY Region, SalesAmount DESC;
```

- **Operator Used**: ORDER BY
- **Explanation**: This query retrieves all columns from the `EmployeeSales` table and orders the results by `Region` in ascending order and then by `SalesAmount` in descending order.
- **Approach and Intuition**: Sorting by region first groups sales from the same region together, and then sorting by sales amount in descending order helps identify the highest sales within each region.

**Generated Table**:

| EmployeeID | Region | Category    | Quarter | SalesAmount |
|------------|--------|-------------|---------|-------------|
| 101        | North  | Electronics | Q2      | 1500.00     |
| 101        | North  | Electronics | Q1      | 1200.00     |
| 102        | North  | Clothing    | Q2      | 950.00      |
| 102        | North  | Clothing    | Q1      | 800.00      |
| 103        | South  | Electronics | Q1      | 1000.00     |
| 103        | South  | Clothing    | Q1      | 1200.00     |
| 104        | East   | Electronics | Q2      | 1150.00     |
| 104        | East   | Clothing    | Q2      | 500.00      |
| 105        | West   | Electronics | Q2      | 2100.00     |
| 105        | West   | Clothing    | Q2      | 1300.00     |
| 105        | West   | Electronics | Q1      | 1900.00     |
| 105        | West   | Clothing    | Q1      | 1100.00     |
<br>

#### Query 2: Order by Category, SalesAmount desc

```sql
SELECT *
FROM EmployeeSales
ORDER BY Category, SalesAmount DESC;
```

- **Operator Used**: ORDER BY
- **Explanation**: This query retrieves all columns from the `EmployeeSales` table and orders the results by `Category` in ascending order and then by `SalesAmount` in descending order.
- **Approach and Intuition**: Sorting by category first groups sales from the same category together, and then sorting by sales amount in descending order helps identify the highest sales within each category.

**Generated Table**:

| EmployeeID | Region | Category    | Quarter | SalesAmount |
|------------|--------|-------------|---------|-------------|
| 105        | West   | Electronics | Q2      | 2100.00     |
| 105        | West   | Electronics | Q1      | 1900.00     |
| 105        | West   | Clothing    | Q2      | 1300.00     |
| 105        | West   | Clothing    | Q1      | 1100.00     |
| 101        | North  | Electronics | Q2      | 1500.00     |
| 101        | North  | Electronics | Q1      | 1200.00     |
| 104        | East   | Electronics | Q2      | 1150.00     |
| 103        | South  | Clothing    | Q1      | 1200.00     |
| 102        | North  | Clothing    | Q2      | 950.00      |
<br>

#### Query 3: Year to date sale Q1 today (How much sales?)

```sql
SELECT SUM(SalesAmount)
FROM EmployeeSales
WHERE Quarter = 'Q1';
```

- **Operator Used**: SUM
- **Explanation**: This query calculates the total sales amount for the first quarter ('Q1').
- **Approach and Intuition**: Filtering the data to include only sales from the first quarter ensures that we're summing the sales for that specific time period.

**Generated Table**:

| SUM(SalesAmount) |
|------------------|
| 4100.00          |
<br>

#### Query 4: Select Region, Category, Sum(SalesAmount)...

```sql
SELECT Region, Category, SUM(SalesAmount)
FROM EmployeeSales
GROUP BY Region, Category
ORDER BY Region, SUM(SalesAmount) DESC;
```

- **Operator Used**: GROUP BY, SUM, ORDER BY
- **Explanation**: This query groups the data by `Region` and `Category`, calculates the sum of `SalesAmount` for each group, and then orders the results by `Region` and the sum of `SalesAmount` in descending order within each region.
- **Approach and Intuition**: Grouping the data by region and category allows us to see the total sales amount for each combination, and ordering the results by region ensures that the regions are presented in alphabetical order with the highest sales amount first.

**Generated Table**:

| Region | Category    | SUM(SalesAmount) |
|--------|-------------|------------------|
| East   | Electronics | 1150.00          |
| East   | Clothing    | 500.00           |
| North  | Electronics | 2700.00          |
| North  | Clothing    | 1750.00          |
| South  | Electronics | 1000.00          |
| South  | Clothing    | 1200.00          |
| West   | Electronics | 4000.00          |
| West   | Clothing    | 2400.00          |
<br>

#### Query 5: Select Region, Sum(SalesAmount)...

```sql
SELECT Region, SUM(SalesAmount)
FROM EmployeeSales
GROUP BY Region;
```

- **Operator Used**: GROUP BY, SUM
- **Explanation**: This query groups the data by `Region` and calculates the sum of `SalesAmount` for each region.
- **Approach and Intuition**: Grouping the data by region allows us to see the total sales amount for each region.

**Generated Table**:

| Region | SUM(SalesAmount) |
|--------|------------------|
| North  | 4450.00          |
| South  | 2200.00          |
| East   | 1650.00          |
| West   | 6400.00          |
<br>

#### Query 6: Select [Quarter], Sum(SalesAmount)...

```sql
SELECT [Quarter], SUM(SalesAmount)
FROM EmployeeSales
GROUP BY [Quarter];
```

- **Operator Used**: GROUP BY, SUM
- **Explanation**: This query groups the data by `Quarter` and calculates the sum of `SalesAmount` for each quarter.
- **Approach and Intuition**: Grouping the data by quarter allows us to see the total sales amount for each quarter.

**Generated Table**:

| Quarter | SUM(SalesAmount) |
|---------|------------------|
| Q1      | 5300.00          |
| Q2      | 6950.00          |
<br>

#### Query 7: Grouping Sets R-C, R-Q, R, Q

```sql
SELECT Region, Category, [Quarter], SUM(SalesAmount)
FROM EmployeeSales
GROUP BY GROUPING SETS(
    (Region, Category),
    (Region, [Quarter]),
    (Region),
    ([Quarter])
);
```

- **Operator Used**: GROUP BY, GROUPING SETS, SUM
- **Explanation**: This query computes the sum of `SalesAmount` for various grouping combinations, including by region and category, region and quarter, region only, and quarter only.
- **Approach and Intuition**: Using GROUPING SETS allows for multiple levels of aggregation, providing insights into sales amounts at different hierarchical levels.

**Generated Table**:

| Region | Category    | Quarter | SUM(SalesAmount) |
|--------|-------------|---------|------------------|
| East   | Electronics | Q2      | 1150.00          |
| East   | Clothing    | Q2      | 500.00           |
| East   | Electronics | NULL    | 1150.00          |
| East   | Clothing    | NULL    | 500.00           |
| North  | Electronics | Q1      | 1200.00          |
| North  | Electronics | Q2      | 1500.00          |
| North  | Clothing    | Q1      | 800.00           |
| North  | Clothing    | Q2      | 950.00           |
| North  | Electronics | NULL    | 2700.00          |
| North  | Clothing    | NULL    | 1750.00          |
| South  | Electronics | Q1      | 1000.00          |
| South  | Clothing    | Q1      | 1200.00          |
| South  | Electronics | NULL    | 1000.00          |
| South  | Clothing    | NULL    | 1200.00          |
| West   | Electronics | Q1      | 1900.00          |
| West   | Electronics | Q2      | 2100.00          |
| West   | Clothing    | Q1      | 1100.00          |
| West   | Clothing    | Q2      | 1300.00          |
| West   | Electronics | NULL    | 4000.00          |
| West   | Clothing    | NULL    | 2400.00          |
| NULL   | NULL        | Q1      | 5300.00          |
| NULL   | NULL        | Q2      | 6950.00          |
| NULL   | NULL        | NULL    | 12250.00         |
<br>

#### Query 8: Grouping Sets (continued)

```sql
SELECT Region, Category, [Quarter], SUM(SalesAmount)
FROM EmployeeSales
GROUP BY GROUPING SETS(
    (Region, Category),
    (Region, [Quarter]),
    (Region),
    ([Quarter])
)
ORDER BY GROUPING (Region), GROUPING (Category), GROUPING([Quarter]);
```

- **Operator Used**: GROUP BY, GROUPING SETS, SUM, ORDER BY, GROUPING
- **Explanation**: This query extends the previous query by ordering the results based on the grouping sets and indicating the groupings using the GROUPING function.
- **Approach and Intuition**: Ordering by the grouping sets and displaying the grouping indicators help understand the hierarchy and relationships between different levels of aggregation.

**Generated Table**:

| Region | Category    | Quarter | SUM(SalesAmount) |
|--------|-------------|---------|------------------|
| East   | Electronics | Q2      | 1150.00          |
| East   | Clothing    | Q2      | 500.00           |
| East   | Electronics | NULL    | 1150.00          |
| East   | Clothing    | NULL    | 500.00           |
| North  | Electronics | Q1      | 1200.00          |
| North  | Electronics | Q2      | 1500.00          |
| North  | Clothing    | Q1      | 800.00           |
| North  | Clothing    | Q2      | 950.00           |
| North  | Electronics | NULL    | 2700.00          |
| North  | Clothing    | NULL    | 1750.00          |
| South  | Electronics | Q1      | 1000.00          |
| South  | Clothing    | Q1      | 1200.00          |
| South  | Electronics | NULL    | 1000.00          |
| South  | Clothing    | NULL    | 1200.00          |
| West   | Electronics | Q1      | 1900.00          |
| West   | Electronics | Q2      | 2100.00          |
| West   | Clothing    | Q1      | 1100.00          |
| West   | Clothing    | Q2      | 1300.00          |
| West   | Electronics | NULL    | 4000.00          |
| West   | Clothing    | NULL    | 2400.00          |
| NULL   | NULL        | Q1      | 5300.00          |
| NULL   | NULL        | Q2      | 6950.00          |
| NULL   | NULL        | NULL    | 12250.00         |

## Key Types and Definitions

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/861cbc03-de81-4342-bd4a-4f9539ad5b3c)

| Key Type       | Definition                                                                                                                                                     | Example                                                                                     | Usage and Significance                                                                                       |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Primary Key    | A primary key is a unique identifier for each record in a table. It ensures data integrity by preventing duplicate entries.                                    | `EmpID` in Employees table                                                                  | Used to uniquely identify each record in the table and establish relationships with other tables.           |
| Candidate Key  | A candidate key is a set of attributes that can uniquely identify a tuple (row) in a relation (table).                                                        | `{EmpLicence}` in Employees table                                                           | Serves as potential primary keys; ensures each row can be uniquely identified.                               |
| Foreign Key    | A foreign key is a column or a set of columns in one table that refers to the primary key in another table. It enforces referential integrity in database relationships. | `Did` in Employees table, referencing `Did` in Designation table                           | Establishes relationships between tables; ensures data consistency by linking related information.           |
| Alternate Key  | An alternate key is a candidate key that was not chosen as the primary key.                                                                                   | `{EmpPassport}` in Employees table                                                          | Provides alternative unique identifiers if the primary key is not suitable for certain operations.          |
| Super Key      | A super key is a set of attributes within a table whose values can uniquely identify each row. It may contain more attributes than necessary for uniqueness.       | `{EmpID, EmpName}` in Employees table                                                        | Acts as a broader identifier than the primary key; useful in indexing and query optimization.               |
| Unique Key     | A unique key constraint ensures that all values in a column or a group of columns are unique. Unlike a primary key, a table can have multiple unique keys.        | `Designation` in Designation table                                                          | Ensures uniqueness within specified columns; useful for enforcing data integrity and constraints.           |
| Composite Key  | A composite key is a combination of two or more columns that together uniquely identify each row in a table.                                                  | `{EmpID, EmpLicence}` in Employees table                                                     | Ensures uniqueness by combining multiple attributes; used when no single attribute can uniquely identify each row.  |

---

## ACID Property

| ACID Property | Definition                                                                                                    | Example                                                                                                                                                  |
|---------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Atomicity     | Ensures that either all operations in a transaction are completed successfully or none of them are.           | When transferring money between bank accounts, the entire transfer must either succeed (withdrawing from one account and depositing into the other) or fail. |
| Consistency   | Ensures that the database remains in a consistent state before and after a transaction.                      | In a hotel booking system, if a room is booked, the system should ensure that the room is no longer available for booking.                            |
| Isolation     | Ensures that the execution of multiple transactions concurrently does not interfere with each other.          | If two people try to book the same hotel room at the same time, the system should handle it so that one booking doesn't affect the other.             |
| Durability    | Guarantees that once a transaction is committed, its changes are permanent and will not be lost.             | Saving a document on your computer: once you save it, you expect it to be there even if your computer crashes.                                        |
