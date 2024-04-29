# <a href="https://docs.google.com/presentation/d/1ffkH7m5Re7vav2mQcjgeKGRf-4n71sKfxND98MYJt4Y/edit#slide=id.g206125106ce_0_237">Intro to Databases</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/fc4b317d-037a-4fc2-8688-e2bb034e6523)

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/435e6707-fc87-448a-9721-8e403022aff5)

## What is Database?
Special software to store data

### Why we need a special software
A database is a structured collection of data organized for efficient retrieval, storage, and management. It is managed by specialized software that ensures data integrity, security, and scalability. This software provides features such as indexing, querying, and transaction management to optimize performance and usability. Databases are essential for storing and managing large volumes of data in various applications, ranging from simple task lists to complex enterprise systems.

### Twitter Database on a Laptop
Keeping a Twitter database on a laptop presents several challenges:
1. **Storage Limitations:** Laptops typically have limited storage capacity compared to dedicated servers or cloud platforms. Storing a large Twitter database may quickly exhaust available disk space.
2. **Performance:** Laptops may not have the processing power or memory resources to efficiently handle the demands of a Twitter database, especially with frequent updates and queries.
3. **Scalability:** Laptops are not designed for scalable database solutions. As the Twitter database grows in size or requires increased performance, scaling up resources on a laptop becomes impractical.
4. **Reliability:** Laptops are prone to hardware failures, power outages, and other disruptions. Running a critical Twitter database on a laptop increases the risk of data loss or corruption.
5. **Security:** Laptops are more vulnerable to security threats compared to servers located in secure data centers. Protecting sensitive Twitter data on a laptop may require additional security measures.

In summary, while it's technically possible to host a Twitter database on a laptop, it's not recommended due to limitations in storage, performance, scalability, reliability, and security.

## Where do Databases Live?
Databases often reside in the cloud. Cloud computing involves accessing and storing data and applications over the internet instead of on local computers or servers. Cloud providers maintain large data centers with powerful servers and storage systems, where databases are hosted. Users can access these databases remotely via the internet, allowing for scalability, flexibility, and accessibility from anywhere with an internet connection. This setup eliminates the need for organizations to manage their physical hardware and offers benefits such as scalability, reliability, and cost-effectiveness.

Databases typically live on dedicated servers, often hosted in data centers or the cloud.

## Cloud Providers
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/daf003ac-879a-4458-ba5b-1b762f1be0cc)

### What is the cloud and who are its providers? 
The cloud refers to the delivery of computing services, including servers, storage, databases, networking, software, and more, over the internet. 
**Examples of Cloud Providers:**
1. **Amazon Web Services (AWS):** A comprehensive and widely-used cloud platform offering a wide range of services for computing, storage, networking, and more.
2. **Microsoft Azure:** A cloud computing platform by Microsoft providing services such as computing, analytics, storage, and networking.
3. **Google Cloud Platform (GCP):** Google's suite of cloud computing services, offering infrastructure, storage, analytics, machine learning, and more.
4. **IBM Cloud:** A cloud computing platform by IBM offering a range of cloud services, including computing, storage, and networking.
5. **Oracle Cloud:** Oracle's cloud infrastructure providing services such as computing, storage, database, and applications.
6. **Alibaba Cloud:** A leading cloud computing platform by Alibaba Group, offering a wide range of cloud services for businesses globally.
7. **DigitalOcean:** Known for its simplicity and developer-friendly approach, DigitalOcean provides cloud services focused on simplicity and ease of use for developers.
8. **Heroku:** A cloud platform that enables developers to build, deploy, and scale applications easily using a variety of programming languages and frameworks.
9. **Salesforce Cloud:** A cloud-based software-as-a-service (SaaS) platform offering a range of customer relationship management (CRM) and enterprise applications.
10. **VMware Cloud:** VMware offers a range of cloud services, including infrastructure, networking, security, and management solutions, designed to run and manage applications across clouds and devices.

## Renting vs Buying

### If you have 100 computers, where would you keep them and what would be needed?
You would need to rent a physical location, such as an office or a data center, to house the computers. This location would need to provide amenities like power, cooling, and security to ensure the computers operate properly and are protected from theft or damage. Additionally, maintenance costs for hardware repairs, upgrades, and network infrastructure would also be required to keep the computers running smoothly.

### What is disaster management for databases?
Disaster management for databases involves implementing strategies to prevent data loss or corruption during unexpected events, such as hardware failures, cyberattacks, or natural disasters, and ensuring quick recovery to maintain data integrity and availability.


| Aspect          | Renting                         | Buying                      |
|-----------------|---------------------------------|-----------------------------|
| Cost upfront    | Low (often no initial cost)     | High (purchase price)      |
| Ownership       | No ownership                    | Full ownership              |
| Flexibility     | High (can switch easily)        | Low (commitment to asset)  |
| Maintenance     | Generally included in rental     | Responsibility of owner    |
| Scalability     | Easily scale up or down         | Limited by asset            |
| Risk            | Lower risk, as less investment | Higher risk, potential loss |
| Technology      | Access to latest technology     | May become outdated        |
| Conclusion      | Renting is often preferable     | Buying may suit some needs  |

In conclusion, renting is often a better choice than buying due to lower upfront costs, greater flexibility, and reduced risk.

## Operating System (OS) in Cloud
In a cloud environment, the operating system (OS) is often referred to as the "guest OS." It's the software that manages hardware resources and provides services for computer programs. 
### Example:
- **Windows:** Microsoft Windows Server
- **Linux:** Various distributions like Ubuntu, CentOS, or Red Hat Enterprise Linux
In a cloud environment, users can choose their preferred OS when provisioning virtual machines or instances.

## SQL VS NO SQL

| Feature                      | SQL (Relational Database)                                      | NoSQL (Non-Relational Database)                        |
|------------------------------|----------------------------------------------------------------|---------------------------------------------------------|
| Data Model                   | Follows a structured data model with tables and relationships | Offers flexible schema design, including key-value, document, column-family, and graph databases |
| Schema                       | Requires a predefined schema                                    | Can have a dynamic or flexible schema                    |
| Query Language               | Uses SQL (Structured Query Language) for queries               | Doesn't necessarily use SQL, may have its query language or APIs |
| Scalability                  | Vertical scalability (scaling up)                               | Horizontal scalability (scaling out)                     |
| ACID Compliance              | ACID compliant (Atomicity, Consistency, Isolation, Durability) | May or may not be ACID compliant depending on the database |
| Transactions                 | Supports transactions                                           | May support transactions, but implementation varies       |
| Examples                     | MySQL, PostgreSQL, Oracle                                      | MongoDB, Cassandra, Redis, Couchbase                     |


#### Examples:

1. **SQL Example:**
   - Database: PostgreSQL
   - Schema: 
     - Table: `employees`
       - Columns: `id`, `name`, `department`, `salary`
   - Query: 
     ```sql
     SELECT * FROM employees WHERE department = 'IT';
     ```

2. **NoSQL Example:**
   - Database: MongoDB
   - Schema:
     - Collection: `employees`
       - Documents:
         ```json
         {
           "_id": ObjectId("60a825f83436eb054384b75e"),
           "name": "John Doe",
           "department": "IT",
           "salary": 75000
         }
         ```
   - Query:
     ```javascript
     db.employees.find({ department: 'IT' });
     ```

> These examples illustrate the differences in data modeling, schema, query language, and scalability between SQL and NoSQL databases.


# SQL

## <a href = "https://sqlbolt.com/lesson/introduction"> Introduction to SQL </a>
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/a675151e-32a3-4ec9-91ac-84b254e17231)


## <a href = "https://sqlbolt.com/lesson/select_queries_introduction">Lesson 1: SELECT queries 101</a>

![Screenshot_24-4-2024_172952_sqlbolt com](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/f9953193-b8d4-4679-9874-f58ca30affbd)

### Exercise 1 

1. **Find the title of each film:**
   ```sql
   SELECT Title FROM Movies;
   ```
   This query retrieves the titles of all the films from the "Movies" table.

2. **Find the director of each film:**
   ```sql
   SELECT Director FROM Movies;
   ```
   This query fetches the directors of all the films from the "Movies" table.

3. **Find the title and director of each film:**
   ```sql
   SELECT Title, Director FROM Movies;
   ```
   This query retrieves both the title and director of each film from the "Movies" table.

4. **Find the title and year of each film:**
   ```sql
   SELECT Title, Year FROM Movies;
   ```
   This query fetches both the title and the year of release for each film from the "Movies" table.

5. **Find all the information about each film:**
   ```sql
   SELECT * FROM Movies;
   ```
   This query selects all columns (attributes) for each film in the "Movies" table, effectively fetching all available information about each film.

> These queries return columns from the "Movies" table that meet the specified criteria.


## <a href = "https://sqlbolt.com/lesson/select_queries_with_constraints">Lesson 2: Queries with constraints (Pt. 1)</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/60065cd6-348e-4b3d-9a30-d13387b07ce6)

### Exercise 2

1. **Find the movie with a row id of 6:**
   ```sql
   SELECT * FROM Movies WHERE Id = 6;
   ```
   This query retrieves all columns for the movie with a row ID of 6 from the "Movies" table.

2. **Find the movies released in the years between 2000 and 2010:**
   ```sql
   SELECT * FROM Movies WHERE Year BETWEEN 2000 AND 2010;
   ```
   This query fetches all columns for movies released between the years 2000 and 2010 from the "Movies" table.

3. **Find the movies not released in the years between 2000 and 2010:**
   ```sql
   SELECT * FROM Movies WHERE Year NOT BETWEEN 2000 AND 2010;
   ```
   This query retrieves all columns for movies not released between the years 2000 and 2010 from the "Movies" table.

4. **Find the first 5 Pixar movies and their release year:**
   ```sql
   SELECT * FROM Movies WHERE Director = 'Pixar' LIMIT 5;
   ```
   This query selects all columns for the first 5 movies where the director's name contains 'Pixar' (case-insensitive) and also limits the result to 5 rows.

5. **Retrieve all movies released in the years 1999, 2007, and 2010.**
   ```sql
    SELECT * FROM Movies WHERE Year IN (1999, 2007, 2010);
   ```

6. **Retrieve all movies except those released in the years 1999, 2007, and 2010.**
   ```sql
    SELECT * FROM Movies WHERE Year NOT IN (1999, 2007, 2010);
   ```
   These (5th n 6th) queries provide a way to filter movies based on whether their release year is within or outside the specified set of years.

> These queries return rows from the "Movies" table that meet the specified criteria.


## <a href = "https://sqlbolt.com/lesson/select_queries_with_constraints_pt_2">Lesson 3: Queries with constraints (Pt. 2)</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/2f568a83-b769-436f-8382-03c0eb90f34c)

### Exercise 3

**1. Find all the Toy Story movies:**
```sql
SELECT * FROM Movies WHERE Title LIKE 'Toy Story%';
```
This command selects all movies with titles starting with "Toy Story".

```sql
SELECT * FROM Movies WHERE Title LIKE 'Toy Story_';
```
This command selects all movies with titles exactly matching "Toy Story" followed by one additional character.

```sql
SELECT * FROM Movies WHERE Title LIKE '%Toy Story%';
```
This command selects all movies with "Toy Story" appearing anywhere in the title.

**2. Find all the movies directed by John Lasseter:**
```sql
SELECT * FROM Movies WHERE Director = 'John Lasseter';
```
This command selects all movies directed by "John Lasseter".

**3. Find all the movies (and director) not directed by John Lasseter:**
```sql
SELECT * FROM Movies WHERE Director != 'John Lasseter';
```
This command selects all movies not directed by "John Lasseter".

**4. Find all the WALL movies:**
```sql
SELECT * FROM Movies WHERE Title LIKE '%WALL%';
```
This command selects all movies with "WALL" in their title.

> These SQL operators and wildcards are commonly used for pattern matching and comparison in queries to filter rows based on specific conditions or patterns.

## <a href = "https://sqlbolt.com/lesson/filtering_sorting_query_results">Lesson 4: Filtering and sorting Query results</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/7d9b7d75-9627-4c07-b11b-b328222a269f)

### Exercise 4

**1. List all directors of Pixar movies (alphabetically), without duplicates**
```sql
SELECT DISTINCT Director FROM Movies WHERE Director LIKE '%Pixar%' ORDER BY Director;
```
This command selects all unique directors from the Movies table whose names contain "Pixar" and orders them alphabetically without duplicates.

**2. List the last four Pixar movies released (ordered from most recent to least)**
```sql
SELECT * FROM Movies WHERE Director LIKE '%Pixar%' ORDER BY Id DESC LIMIT 4;
```
This command selects the last four movies from the Movies table whose directors contain "Pixar" and orders them by their Id in descending order, representing the most recent releases.

**3. List the first five Pixar movies sorted alphabetically**
```sql
SELECT * FROM Movies WHERE Director LIKE '%Pixar%' ORDER BY Title ASC LIMIT 5;
```
This command selects the first five movies from the Movies table whose directors contain "Pixar" and orders them alphabetically by their title in ascending order.

**4. List the next five Pixar movies sorted alphabetically**
```sql
SELECT * FROM Movies WHERE Director LIKE '%Pixar%' ORDER BY Title ASC LIMIT 5 OFFSET 5;
```
This command selects the next five movies from the Movies table whose directors contain "Pixar" and orders them alphabetically by their title in ascending order, starting from the sixth row.

> These SQL commands provide various queries to retrieve information about Pixar movies, sorted and limited in different ways to meet specific requirements. Utilizing SQL commands like ORDER BY, LIMIT, and DISTINCT to narrow down and organize data according to specific criteria, ensuring clarity and relevance in the result set.

## <a href = "https://sqlbolt.com/lesson/select_queries_review">Review: Simple SELECT Queries</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/2780d096-b8a2-4ab6-8ecc-3b205e211c38)

### Exercise 5

**1. List all the Canadian cities and their populations:**
```sql
SELECT City, Population FROM North_American_Cities WHERE Country = 'Canada';
```
This command retrieves cities and their populations from the North American Cities table specifically for Canada. It helps understand the distribution of population within Canada.

**2. Order all the cities in the United States by the latitude from north to south:**
```sql
SELECT City, Latitude FROM North_American_Cities WHERE Country = 'United States' ORDER BY Latitude DESC;
```
By ordering cities based on latitude in descending order, this query sorts them from north to south. This arrangement aligns with the fact that latitude increases towards the North Pole, providing insights into the geographical layout of cities in the United States.

**3. List all the cities west of Chicago, ordered from west to east:**
```sql
SELECT City FROM North_American_Cities WHERE Longitude < (SELECT Longitude FROM North_American_Cities WHERE City = 'Chicago') ORDER BY Longitude ASC;
```
This command retrieves cities located west of Chicago and orders them from west to east based on longitude. It aligns with the principle that as longitude increases towards the east, cities are arranged from west to east.

**4. List the two largest cities in Mexico by population:**
```sql
SELECT City, Population FROM North_American_Cities WHERE Country = 'Mexico' ORDER BY Population DESC LIMIT 2;
```
By ordering cities in Mexico by population in descending order and limiting the result to the top two, this query identifies the two largest cities in Mexico. It provides insights into the demographic distribution and urbanization within the country.

**5. List the third and fourth largest cities by population in the United States:**
```sql
SELECT City, Population FROM North_American_Cities WHERE Country = 'United States' ORDER BY Population DESC LIMIT 2 OFFSET 2;
```
This command retrieves the third and fourth largest cities in the United States by population. By skipping the first two results and then limiting to the next two, it provides insights into the population hierarchy and urbanization trends within the country.

> Explore how the relationship between longitude and latitude impacts geographic positioning: longitude increases towards the east, while latitude increases towards the north.


## <a href = "https://sqlbolt.com/lesson/select_queries_with_joins">Lesson 6: Multi-table queries with JOINs</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/4aaa6f86-8688-4471-846f-96da33337336)

### Exercise 6 

**1. Find the domestic and international sales for each movie:**
```sql
SELECT m.Title, b.Domestic_sales, b.International_sales
FROM Movies m
JOIN Boxoffice b ON m.Id = b.Movie_id;
```
This query joins the Movies and Boxoffice tables on the Movie_id column to retrieve the title of each movie along with its domestic and international sales.

**2. Show the sales numbers for each movie that did better internationally rather than domestically:**
```sql
SELECT m.Title, b.Domestic_sales, b.International_sales
FROM Movies m
JOIN Boxoffice b ON m.Id = b.Movie_id
WHERE b.International_sales > b.Domestic_sales;
```
This query filters the results to show only the movies where the international sales exceeded the domestic sales, displaying their titles along with the respective sales numbers.

**3. List all the movies by their ratings in descending order:**
```sql
SELECT m.Title, b.Rating
FROM Movies m
JOIN Boxoffice b ON m.Id = b.Movie_id
ORDER BY b.Rating DESC;
```
This query retrieves the titles of all movies along with their ratings, ordering the results in descending order based on the movie ratings.

> Multi-table queries with JOINs allow combining data from multiple tables based on common columns, facilitating the retrieval of related information in a single result set.

## <a href = "https://sqlbolt.com/lesson/select_queries_with_outer_joins">Lesson 7: OUTER JOINs</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/f4171669-001c-4a89-aa82-15f76b1a2518)

### Exercise 7 

**1. Find the list of all buildings that have employees:**
```sql
SELECT DISTINCT Building
FROM Employees;
```
This query retrieves the distinct list of buildings from the Employees table, indicating all buildings where employees are assigned.

**2. Find the list of all buildings and their capacity:**
```sql
SELECT Building_name, Capacity
FROM Buildings;
```
This query retrieves the list of all buildings along with their respective capacities from the Buildings table.

**3. List all buildings and the distinct employee roles in each building (including empty buildings):**
```sql
SELECT b.Building_name, b.Capacity, e.Role
FROM Buildings b
LEFT JOIN Employees e ON b.Building_name = e.Building;
```
This query uses a LEFT JOIN to combine the Buildings and Employees tables, ensuring that all buildings are included in the result set even if they have no associated employees. It lists each building along with its capacity and the distinct employee roles present in each building.


## <a href = "https://sqlbolt.com/lesson/select_queries_with_nulls">Lesson 8: A short note on NULLs</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/66ba948b-3b68-4817-971d-f4518739c0f2)

### Exercise 8

**1. Find the name and role of all employees who have not been assigned to a building:**
```sql
SELECT Name, Role
FROM Employees
WHERE Building IS NULL;
```
This query selects the names and roles of employees from the Employees table where the Building column is NULL, indicating that they have not been assigned to any building.

**2. Find the names of the buildings that hold no employees:**
```sql
SELECT b.Building_name
FROM Buildings b
LEFT JOIN Employees e ON b.Building_name = e.Building
WHERE e.Building IS NULL;
```
This query retrieves the names of buildings from the Buildings table that have no associated employees. It uses a LEFT JOIN between the Buildings and Employees tables, ensuring that all buildings are included in the result set, and then filters out those buildings where no employees are assigned.

## <a href = "https://sqlbolt.com/lesson/select_queries_with_expressions">Lesson 9: Queries with expressions</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/2ff28483-f276-4ef3-ab5f-951c50e80d0d)

### Exercise 9
**Exercise 9 — Tasks**

**1. List all movies and their combined sales in millions of dollars:**
```sql
SELECT m.Title, 
       (b.Domestic_sales + b.International_sales) / 1000000 AS Combined_sales_in_millions
FROM Movies m
JOIN Boxoffice b ON m.Id = b.Movie_id;
```
This query retrieves the titles of all movies along with their combined sales (domestic and international) converted into millions of dollars.

**2. List all movies and their ratings in percent:**
```sql
SELECT m.Title, 
       b.Rating * 10 AS Rating_percent
FROM Movies m
JOIN Boxoffice b ON m.Id = b.Movie_id;
```
This query retrieves the titles of all movies along with their ratings converted into percentages.

**3. List all movies that were released on even-numbered years:**
```sql
SELECT *
FROM Movies
WHERE Year % 2 = 0;
```
This query retrieves all movies that were released on even-numbered years based on the Year column in the Movies table.

## <a href = "https://sqlbolt.com/lesson/select_queries_with_aggregates">Lesson 10: Queries with aggregates (Pt. 1)</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/0c13904b-0b23-4294-b39a-12b638c00652)

### Exercise 10

1. **Find the longest time that an employee has been at the studio:**
```sql
SELECT MAX(Years_employed) AS Longest_time_at_studio
FROM Employees;
```
This query retrieves the maximum value of the `Years_employed` column from the `Employees` table, which represents the longest time an employee has been employed at the studio.

2. **For each role, find the average number of years employed by employees in that role:**
```sql
SELECT Role, AVG(Years_employed) AS Average_years_employed
FROM Employees
GROUP BY Role;
```
This query calculates the average number of years employed (`AVG(Years_employed)`) for each distinct role (`GROUP BY Role`) in the `Employees` table.

3. **Find the total number of employee years worked in each building:**
```sql
SELECT Building, SUM(Years_employed) AS Total_years_worked
FROM Employees
GROUP BY Building;
```
This query calculates the total number of employee years worked (`SUM(Years_employed)`) in each building (`GROUP BY Building`) based on the data in the `Employees` table.

> These SQL queries will provide the desired insights into employee tenure and years of service in various roles and buildings within the studio.


## <a href = "https://sqlbolt.com/lesson/select_queries_with_aggregates_pt_2">Lesson 11: Queries with aggregates (Pt. 2)</a>
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/25723360-84e5-4aad-a187-ff96a1399c35)

### Exercise 11

1. **Find the number of Artists in the studio (without a HAVING clause):**
```sql
SELECT COUNT(*) AS Number_of_Artists
FROM Employees
WHERE Role = 'Artist';
```
This query selects the count of rows (`COUNT(*)`) from the `Employees` table where the role is 'Artist'.

2. **Find the number of Employees of each role in the studio:**
```sql
SELECT Role, COUNT(*) AS Number_of_Employees
FROM Employees
GROUP BY Role;
```
This query groups the employees by their roles (`GROUP BY Role`) and counts the number of employees in each role (`COUNT(*)`).

3. **Find the total number of years employed by all Engineers:**
```sql
SELECT SUM(Years_employed) AS Total_years_employed
FROM Employees
WHERE Role = 'Engineer';
```
This query calculates the sum of years employed (`SUM(Years_employed)`) for all engineers in the `Employees` table.

> By executing these SQL queries, we can obtain the desired information about the number of artists, employees in each role, and the total years employed by engineers in the studio.

## <a href = "https://sqlbolt.com/lesson/select_queries_order_of_execution">Lesson 12: Order of execution of a Query</a>
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/bf87d3c3-7fb5-449c-b077-e032edab69e3)

### Exercise 12
1. **Find the number of movies each director has directed:**
```sql
SELECT Director, COUNT(*) AS Number_of_Movies_Directed
FROM Movies
GROUP BY Director;
```
This query groups the movies by their directors using the `GROUP BY` clause and counts the number of movies directed by each director using the `COUNT(*)` function.

2. **Find the total domestic and international sales attributed to each director:**
```sql
SELECT m.Director, SUM(b.Domestic_sales) AS Total_Domestic_Sales, SUM(b.International_sales) AS Total_International_Sales
FROM Movies m
JOIN Boxoffice b ON m.Id = b.Movie_id
GROUP BY m.Director;
```
This query joins the `Movies` and `Boxoffice` tables on the movie ID and groups the data by director. It then calculates the sum of domestic and international sales for each director using the `SUM()` function.

> By executing these SQL queries, we can obtain the desired information about the number of movies each director has directed and the total domestic and international sales attributed to each director.


## <a href = "https://sqlbolt.com/lesson/inserting_rows">Lesson 13: Inserting rows</a>
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/1fe46591-f815-4b00-95d0-8ec5112199ad)

### Exercise 13

1. **Add the studio's new production, Toy Story 4 to the list of movies:**
```sql
INSERT INTO Movies (Title, Director, Year, Length_minutes)
VALUES ('Toy Story 4', 'New Director', 2020, 110);
```
This SQL statement is inserting a new row into the `Movies` table. We specify the columns we want to populate (`Title`, `Director`, `Year`, `Length_minutes`) and provide the corresponding values for the new movie "Toy Story 4". The values are: Title = 'Toy Story 4', Director = 'New Director', Year = 2020, Length_minutes = 110.

2. **Add the record for Toy Story 4 to the BoxOffice table:**
```sql
INSERT INTO Boxoffice (Movie_id, Rating, Domestic_sales, International_sales)
VALUES ((SELECT MAX(Id) FROM Movies), 8.7, 340000000, 270000000);
```
This SQL statement inserts a new row into the `Boxoffice` table. We need to specify the `Movie_id` which corresponds to the newly added movie "Toy Story 4". To get the `Movie_id`, we use a subquery `(SELECT MAX(Id) FROM Movies)` which retrieves the maximum ID from the `Movies` table, thus obtaining the ID of the newly inserted movie. The rating is set to 8.7, and the domestic and international sales are set to 340 million and 270 million, respectively.

> By executing these SQL statements, we effectively add the new movie "Toy Story 4" to the `Movies` table and its associated record to the `Boxoffice` table.


## <a href = "https://sqlbolt.com/lesson/updating_rows">Lesson 14: Updating rows</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/753bcd1a-696d-4aaf-8f12-6bd43a81e9bb)

### Exercise 14

1. **Update director for "A Bug's Life":**
   ```sql
   UPDATE Movies
   SET Director = 'John Lasseter'
   WHERE Title = 'A Bug''s Life';
   ```
   This statement updates the `Director` column for the movie "A Bug's Life" to "John Lasseter".

2. **Update release year for "Toy Story 2":**
   ```sql
   UPDATE Movies
   SET Year = 1999
   WHERE Title = 'Toy Story 2';
   ```
   This statement corrects the release year of "Toy Story 2" to 1999.

3. **Update title and director for "Toy Story 8":**
   ```sql
   UPDATE Movies
   SET Title = 'Toy Story 3',
       Director = 'Lee Unkrich'
   WHERE Id = 3;
   ```
   This statement updates both the `Title` and `Director` columns for the movie with `Id` 3 (assuming it's "Toy Story 8") to "Toy Story 3" directed by "Lee Unkrich".

> These `UPDATE` statements ensure that the information in the `Movies` table is corrected according to the given tasks. Always remember to use caution when updating data and double-check your conditions to avoid unintended changes.

## <a href = "https://sqlbolt.com/lesson/deleting_rows">Lesson 15: Deleting rows</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/948f17cf-5f7d-48da-8667-b84712f0dceb)

### Exercise 15

1. **Delete movies released before 2005:**
   ```sql
   DELETE FROM Movies
   WHERE Year < 2005;
   ```
   This statement removes all rows from the `Movies` table where the `Year` is before 2005.

2. **Delete movies directed by Andrew Stanton:**
   ```sql
   DELETE FROM Movies
   WHERE Director = 'Andrew Stanton';
   ```
   This statement deletes all rows from the `Movies` table where the `Director` is "Andrew Stanton".

> These `DELETE` statements help clean up the `Movies` table by removing unwanted rows according to the specified conditions. Always be cautious when deleting data from a table and ensure that you are targeting the correct rows to avoid unintended data loss.

## <a href = "https://sqlbolt.com/lesson/creating_tables">Lesson 16: Creating tables</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/18f70de1-c4b3-479d-b8ab-3703f7b2340c)

### Exercise 16

To create the `Database` table with the specified columns, we use the `CREATE TABLE` statement. Here's how we can create the table:

```sql
CREATE TABLE Database (
    Name VARCHAR(255), -- A string describing the name of the database
    Version FLOAT,     -- A floating point number of the latest version of this database
    Download_count INTEGER -- An integer count of the number of times this database was downloaded
);
```
This statement creates a new table named `Database` with three columns: `Name`, `Version`, and `Download_count`, each with their respective data types. The `Name` column is of type `VARCHAR` (variable character) with a maximum length of 255 characters, the `Version` column is of type `FLOAT` (floating point number), and the `Download_count` column is of type `INTEGER`. There are no constraints specified for this table.


## <a href = "https://sqlbolt.com/lesson/altering_tables">Lesson 17: Altering tables</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/4068d7bb-508b-412b-931b-4b3825cd6cbc)

### Exercise 17

**1. To add a new column named `Aspect_ratio` with a `FLOAT` data type to the `Movies` table:**
```sql
ALTER TABLE Movies
ADD Aspect_ratio FLOAT;
```
This command adds a new column named `Aspect_ratio` to the `Movies` table with a data type of `FLOAT`. Now the table will have the following structure:

| Id | Title         | Director       | Year | Length_minutes | Aspect_ratio |
|----|---------------|----------------|------|----------------|--------------|
| 1  | Toy Story     | John Lasseter | 1995 | 81             |              |
| 2  | A Bug's Life  | John Lasseter | 1998 | 95             |              |
| 3  | Toy Story 2   | John Lasseter | 1999 | 93             |              |
| 4  | Monsters, Inc.| Pete Docter    | 2001 | 92             |              |

**2. To add another column named `Language` with a `TEXT` data type and set the default language to English:**
```sql
ALTER TABLE Movies
ADD Language TEXT DEFAULT 'English';
```
This command adds a new column named `Language` to the `Movies` table with a data type of `TEXT` and sets the default value to 'English'. Now the table will have the following structure:

| Id | Title         | Director       | Year | Length_minutes | Aspect_ratio | Language |
|----|---------------|----------------|------|----------------|--------------|----------|
| 1  | Toy Story     | John Lasseter | 1995 | 81             |              | English  |
| 2  | A Bug's Life  | John Lasseter | 1998 | 95             |              | English  |
| 3  | Toy Story 2   | John Lasseter | 1999 | 93             |              | English  |
| 4  | Monsters, Inc.| Pete Docter    | 2001 | 92             |              | English  |


## <a href = "https://sqlbolt.com/lesson/dropping_tables">Lesson 18: Dropping tables</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/d4fc40a0-4e6c-4e0a-88e3-3f579ab6adb5)

### Exercise 18

**1. To drop the `Movies` table:**
```sql
DROP TABLE Movies;
```
This command removes the `Movies` table from the database. Once executed, the table and all its associated data will be permanently deleted.

**2. To drop the `BoxOffice` table:**
```sql
DROP TABLE Boxoffice;
```
This command removes the `Boxoffice` table from the database. Similar to dropping the `Movies` table, once executed, the `Boxoffice` table and all its associated data will be permanently deleted.

> By dropping these tables, we are cleaning up the database and removing all the data and structures we've worked with throughout the exercises.

## <a href = "https://sqlbolt.com/lesson/end">Lesson X: To infinity and beyond!</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/99484a0a-d15f-4fa9-92fc-9f51aa2ffe22)

## Tables 

These tables provide a clear representation of the data stored in each table.

### Salesman Table
```sql
CREATE TABLE salesman(
    salesman_id INT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    commission DECIMAL(4,2)
);

INSERT INTO salesman (salesman_id, name, city, commission) VALUES 
(5001, 'James Hoog', 'New York', 0.15), 
(5002, 'Nail Knite', 'Paris', 0.13), 
(5005, 'Pit Alex', 'London', 0.11), 
(5006, 'Mc Lyon', 'Paris', 0.14), 
(5003, 'Lauson Hen', NULL, 0.12), 
(5007, 'Paul Adam', 'Rome', 0.13);
```

| salesman_id | name         | city       | commission |
|-------------|--------------|------------|------------|
| 5001        | James Hoog   | New York   | 0.15       |
| 5002        | Nail Knite   | Paris      | 0.13       |
| 5005        | Pit Alex     | London     | 0.11       |
| 5006        | Mc Lyon      | Paris      | 0.14       |
| 5003        | Lauson Hen   | NULL       | 0.12       |
| 5007        | Paul Adam    | Rome       | 0.13       |


### Orders Table
```sql
CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);

INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES 
(70001, 150.5, '2012-10-05', 3005, 5002), 
(70009, 270.65, '2012-09-10', 3001, 5005), 
(70002, 65.26, '2012-10-05', 3002, 5001), 
(70004, 110.5, '2012-08-17', 3009, 5003), 
(70007, 948.5, '2012-09-10', 3005, 5002), 
(70005, 2400.6, '2012-07-27', 3007, 5001), 
(70008, 5760, '2012-09-10', 3002, 5001), 
(70010, 1983.43, '2012-10-10', 3004, 5006), 
(70003, 2480.4, '2012-10-10', 3009, 5003), 
(70012, 250.45, '2012-06-27', 3008, 5002), 
(70011, 75.29, '2012-08-17', 3003, 5007), 
(70013, 3045.6, '2012-04-25', 3002, 5001);
```

| ord_no | purch_amt | ord_date   | customer_id | salesman_id |
|--------|-----------|------------|-------------|-------------|
| 70001  | 150.50    | 2012-10-05 | 3005        | 5002        |
| 70009  | 270.65    | 2012-09-10 | 3001        | 5005        |
| 70002  | 65.26     | 2012-10-05 | 3002        | 5001        |
| 70004  | 110.50    | 2012-08-17 | 3009        | 5003        |
| 70007  | 948.50    | 2012-09-10 | 3005        | 5002        |
| 70005  | 2400.60   | 2012-07-27 | 3007        | 5001        |
| 70008  | 5760.00   | 2012-09-10 | 3002        | 5001        |
| 70010  | 1983.43   | 2012-10-10 | 3004        | 5006        |
| 70003  | 2480.40   | 2012-10-10 | 3009        | 5003        |
| 70012  | 250.45    | 2012-06-27 | 3008        | 5002        |
| 70011  | 75.29     | 2012-08-17 | 3003        | 5007        |
| 70013  | 3045.60   | 2012-04-25 | 3002        | 5001        |

### Customer Table
```sql
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT NULL,
    salesman_id INT
);

INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES 
(3002, 'Nick Rimando', 'New York', 100, 5001), 
(3005, 'Graham Zusi', 'California', 200, 5002), 
(3001, 'Brad Guzan', 'London', NULL, 5005), 
(3004, 'Fabian Johns', 'Paris', 300, 5006), 
(3007, 'Brad Davis', 'New York', 200, 5001), 
(3009, 'Geoff Camero', 'Berlin', 100, 5003), 
(3008, 'Julian Green', 'London', 300, 5002), 
(3003, 'Jozy Altidor', 'Moscow', 200, 5007);
```

| customer_id | cust_name     | city       | grade | salesman_id |
|-------------|---------------|------------|-------|-------------|
| 3002        | Nick Rimando  | New York   | 100   | 5001        |
| 3005        | Graham Zusi   | California | 200   | 5002        |
| 3001        | Brad Guzan    | London     | NULL  | 5005        |
| 3004        | Fabian Johns  | Paris      | 300   | 5006        |
| 3007        | Brad Davis    | New York   | 200   | 5001        |
| 3009        | Geoff Camero  | Berlin     | 100   | 5003        |
| 3008        | Julian Green  | London     | 300   | 5002        |
| 3003        | Jozy Altidor  | Moscow     | 200   | 5007        |

---

Here's the breakdown of which table is used for each task:

1. **Task 1: Average Commission of Salesmen from Paris**
   - Table Used: `salesman`

2. **Task 2: Cities with Only One Salesman**
   - Table Used: `salesman`

3. **Task 3: Maximum Commission in Each City and Corresponding Salesmen**
   - Table Used: `salesman`

4. **Task 4: Orders Issued by Paul Adam**
   - Tables Used: `salesman`, `orders`

5. **Task 5: Orders with Amounts Greater Than the Average Order Value for October 10, 2012**
   - Table Used: `orders`

6. **Task 6: Orders with Above-Average Amounts for Their Customers**
   - Tables Used: `orders`, `customer`

7. **Task 7: Orders Attributed to Salesmen in New York**
   - Tables Used: `orders`, `salesman`

8. **Task 8: Salesmen with More Than One Customer**
   - Tables Used: `salesman`, `customer`

9. **Task 9: Customers with Grades Higher Than Every Customer in New York**
   - Tables Used: `customer`

10. **Task 10: Orders with Amounts Smaller Than Any Amount for a Customer in London**
    - Tables Used: `orders`, `customer`

---

## SQL Queries and Explanations

### Task 1: Average Commission of Salesmen from Paris

#### Query 1 (Original):
```sql
SELECT AVG(commision) 
FROM salesman 
WHERE city = 'Paris';
```
#### Explanation:
- **Aggregate Function (AVG)**: Calculates the average commission for salesmen in Paris.
- **Filtering with WHERE**: Limits the calculation to salesmen records with 'Paris' as their city.

#### Query 2 (Alternative using JOIN and Subquery):
```sql
SELECT AVG(s.commision)
FROM salesman s
JOIN (
    SELECT salesman_id
    FROM salesman
    WHERE city = 'Paris'
) p ON s.salesman_id = p.salesman_id;
```
#### Explanation:
- **Subquery with JOIN**: Filters salesmen records to include only those from Paris, then calculates the average commission.

#### Table Generated
| AVG(commision) |
|----------------|
| 0.135          |

### Task 2: Cities with Only One Salesman

#### Query 1 (Original):
```sql
SELECT city, COUNT(salesman_id) 
FROM salesman 
WHERE city IS NOT NULL 
GROUP BY city 
HAVING COUNT(salesman_id) = 1;
```
#### Explanation:
- **Grouping and Counting**: Groups salesmen by city and counts the number of salesmen in each city.
- **Filtering with HAVING**: Filters out cities with only one salesman.

#### Query 2 (Alternative using CASE statement):
```sql
SELECT city,
    CASE
        WHEN COUNT(salesman_id) = 1 THEN 'Only One Salesman'
        ELSE 'Multiple Salesmen'
    END AS status
FROM salesman 
GROUP BY city;
```
#### Explanation:
- **CASE Statement**: Categorizes cities based on the count of salesmen, indicating whether there's only one salesman or multiple salesmen.

#### Table Generated 
| city    | COUNT(salesman_id) |
|---------|---------------------|
| London  | 1                   |
| New York| 1                   |
| Rome    | 1                   |

### Task 3: Maximum Commission in Each City and Corresponding Salesmen

#### Query 1 (Original):
```sql
SELECT s.city, MAX(s.commision), t.name 
FROM salesman s 
JOIN salesman t ON s.salesman_id = t.salesman_id 
GROUP BY s.city;
```
#### Explanation:
- **Joining Tables**: Joins the salesman table with itself to find corresponding salesman names.
- **Grouping and Aggregation**: Groups results by city and finds the maximum commission in each city.

#### Query 2 (Alternative using WINDOW functions):
```sql
SELECT city, 
       MAX(commision) OVER (PARTITION BY city) AS max_commission,
       FIRST_VALUE(name) OVER (PARTITION BY city ORDER BY commision DESC) AS top_salesman
FROM salesman;
```
#### Explanation:
- **Window Functions**: Computes the maximum commission and corresponding salesman using window functions, providing flexibility in data retrieval and analysis.

#### Table Generated
| city    | MAX(commision) | name      |
|---------|----------------|-----------|
| London  | 0.15           | James Hoog|
| New York| 0.13           | Nail Knite|
| Paris   | 0.14           | Mc Lyon   |


### Task 4: Orders Issued by Paul Adam (Using Subquery)

#### Query 1 (Original):
```sql
SELECT * 
FROM orders
WHERE salesman_id = (SELECT salesman_id FROM salesman WHERE name='Paul Adam');
```
#### Explanation:
- **Subquery**: Retrieves the salesman ID associated with the salesman named 'Paul Adam' to filter orders.

#### Query 2 (Alternative using JOIN):
```sql
SELECT o.*
FROM orders o
JOIN salesman s ON o.salesman_id = s.salesman_id
WHERE s.name = 'Paul Adam';
```
#### Explanation:
- **JOIN Operation**: Joins the orders table with the salesman table to filter orders attributed to Paul Adam directly.

#### Table Generated 
| ord_no | purch_amt | ord_date   | customer_id | salesman_id |
|--------|-----------|------------|-------------|-------------|
| 70011  | 75.29     | 2012-08-17 | 3003        | 5007        |

### Task 5: Orders with Values Greater Than the Average Order Value for 10th October 2012

#### Query 1 (Using Subquery with AVG):
```sql
SELECT * 
FROM orders 
WHERE purch_amt > (
    SELECT AVG(purch_amt) 
    FROM orders 
    WHERE ord_date = '2012-10-10'
);
```
#### Explanation:
- **Subquery with AVG**: The subquery calculates the average purchase amount for orders placed on 10th October 2012.
- **Comparison:** The main query selects orders with purchase amounts greater than the average calculated from the subquery for the specified date.

#### Query 2 (Alternative using JOIN and GROUP BY):
```sql
SELECT o.* 
FROM orders o 
JOIN (
    SELECT ord_date, AVG(purch_amt) AS avg_amt 
    FROM orders 
    WHERE ord_date = '2012-10-10' 
    GROUP BY ord_date
) AS avg_orders 
ON o.ord_date = avg_orders.ord_date 
WHERE o.purch_amt > avg_orders.avg_amt;
```
#### Explanation:
- **Join with Subquery:** The main query joins the `orders` table with a subquery that calculates the average purchase amount for orders placed on 10th October 2012.
- **Comparison:** It selects orders with purchase amounts greater than the average amount calculated from the subquery.

#### Table Generated 
| ord_no | purch_amt | ord_date   | customer_id | salesman_id |
|--------|-----------|------------|-------------|-------------|
| 70003  | 2480.40   | 2012-10-10 | 3009        | 5003        |
| 70010  | 1983.43   | 2012-10-10 | 3004        | 5006        |
| 70013  | 3045.60   | 2012-10-10 | 3002        | 5001        |


### Task 6: Orders with Above-Average Amounts for Their Customers

#### Query 1 (Original):
```sql
SELECT customer_id, purch_amt, AVG(purch_amt) 
FROM orders
GROUP BY customer_id
HAVING purch_amt > AVG(purch_amt);
```
#### Explanation:
- **Aggregate Function**: The `AVG()` function calculates the average purchase amount for each customer.
- **Grouping**: The `GROUP BY` clause groups orders by customer ID to compute the average purchase amount for each customer.
- **Filtering with HAVING**: The `HAVING` clause filters out orders where the purchase amount exceeds the average purchase amount for their respective customers.

#### Query 2 (Alternative using Subquery):
```sql
SELECT o.customer_id, o.purch_amt, avg_amt
FROM orders o
JOIN (
    SELECT customer_id, AVG(purch_amt) AS avg_amt
    FROM orders
    GROUP BY customer_id
) t ON o.customer_id = t.customer_id
WHERE o.purch_amt > t.avg_amt;
```
#### Explanation:
- **Subquery with JOIN**: We use a subquery to calculate the average purchase amount for each customer. Then, we join this subquery with the orders table to compare each order's purchase amount with the average amount for its respective customer.
- **Comparison with WHERE**: In the main query, we filter out orders where the purchase amount exceeds the average amount using the `WHERE` clause.

#### Table Generated 
| customer_id | purch_amt | AVG(purch_amt) |
|-------------|-----------|----------------|
| 3002        | 2400.6    | 2447.2733333333|
| 3008        | 250.45    | 250.45         |


### Task 7: Orders Attributed to Salesmen in New York and Paris

#### Query 1 (Original):
```sql
SELECT * 
FROM orders o
JOIN salesman s ON o.salesman_id = s.salesman_id
WHERE s.city IN ('New York', 'Paris');
```
#### Explanation:
- **JOIN Operation**: We use a `JOIN` to combine the orders and salesman tables based on the salesman ID to retrieve orders attributed to salesmen.
- **Filtering with WHERE**: The `WHERE` clause filters the results to include only orders attributed to salesmen in New York or Paris.

#### Query 2 (Alternative using Subquery):
```sql
SELECT * 
FROM orders 
WHERE salesman_id IN (
    SELECT salesman_id 
    FROM salesman 
    WHERE city IN ('New York', 'Paris')
);
```
#### Explanation:
- **Subquery Filtering**: We use a subquery to retrieve the salesman IDs associated with salesmen in New York or Paris.
- **Filtering with IN**: The `IN` operator is used in the main query to filter orders based on the salesman IDs obtained from the subquery.

#### Table Generated by Query 1:
| ord_no | purch_amt | ord_date   | customer_id | salesman_id | salesman_id | name      | city      | commision |
|--------|-----------|------------|-------------|-------------|-------------|-----------|-----------|-----------|
| 70002  | 65.26     | 2012-10-05 | 3002        | 5001        | 5001        | James Hoog| New York  | 0.15      |
| 70005  | 2400.6    | 2012-07-27 | 3007        | 5001        | 5001        | James Hoog| New York  | 0.15      |
| 70008  | 5760      | 2012-09-10 | 3002        | 5001        | 5001        | James Hoog| New York  | 0.15      |

#### Table Generated 
| ord_no | purch_amt | ord_date   | customer_id | salesman_id |
|--------|-----------|------------|-------------|-------------|
| 70002  | 65.26     | 2012-10-05 | 3002        | 5001        |
| 70005  | 2400.6    | 2012-07-27 | 3007        | 5001        |
| 70008  | 5760      | 2012-09-10 | 3002        | 5001        |

### Task 8: Salesmen with More Than One Customer

#### Query 1 (Original):
```sql
SELECT t.name, t.salesman_id 
FROM salesman t
WHERE t.salesman_id IN (SELECT s.salesman_id 
                        FROM salesman s 
                        JOIN customer c ON s.salesman_id = c.salesman_id
                        GROUP BY s.salesman_id 
                        HAVING COUNT(c.customer_id) > 1);
```
#### Explanation:
- **Subquery with JOIN**: The subquery joins the `salesman` and `customer` tables based on the salesman ID to count the number of customers for each salesman.
- **Filtering with HAVING**: The `HAVING` clause filters salesmen who have more than one customer, ensuring only those salesmen are selected.

#### Query 2 (Alternative using EXISTS):
```sql
SELECT name, salesman_id 
FROM salesman t
WHERE EXISTS (SELECT 1 
              FROM customer c 
              WHERE c.salesman_id = t.salesman_id 
              GROUP BY c.salesman_id 
              HAVING COUNT(c.customer_id) > 1);
```
#### Explanation:
- **Subquery with EXISTS**: This alternative approach uses a subquery with `EXISTS` to check if a salesman has more than one customer.
- **Correlation with Outer Query**: The subquery correlates with the outer query by checking the existence of customers associated with each salesman.

#### Table Generated 
| name      | salesman_id |
|-----------|-------------|
| James Hoog| 5001        |
| Nail Knite| 5002        |


### Task 9: Customers with Grades Higher Than Every Customer in New York

#### Query 1 (Original):
```sql
SELECT * 
FROM customer 
WHERE grade > ALL (SELECT grade 
                   FROM customer 
                   WHERE city = 'New York');
```
#### Explanation:
- **Subquery with ALL**: The subquery retrieves the grades of all customers in New York.
- **Comparison with ALL**: The main query selects customers with grades higher than all grades in New York, ensuring only those customers are included.

#### Query 2 (Alternative using MAX):
```sql
SELECT c.* 
FROM customer c
JOIN (SELECT MAX(grade) AS max_grade 
      FROM customer 
      WHERE city = 'New York') t ON c.grade > t.max_grade;
```
#### Explanation:
- **Subquery with MAX**: This alternative approach calculates the maximum grade among customers in New York.
- **Join and Comparison**: The main query joins with the subquery result and selects customers with grades higher than the maximum grade in New York.

#### Table Generated
| customer_id | cust_name    | city      | grade | salesman_id |
|-------------|--------------|-----------|-------|-------------|
| 3001        | Brad Guzan   | London    | NULL  | 5005        |
| 3004        | Fabian Johns | Paris     | 300   | 5006        |
| 3007        | Brad Davis   | New York  | 200   | 5001        |
| 3008        | Julian Green | London    | 300   | 5002        |
| 3003        | Jozy Altidor | Moscow    | 200   | 5007        |

Sure, let's proceed with the alternative queries, explanations, and generated tables for the remaining tasks:

### Task 10: Orders with Amounts Smaller Than Any Amount for a Customer in London

#### Query 1 (Original):
```sql
SELECT o.purch_amt, c.customer_id 
FROM customer c 
JOIN orders o ON c.customer_id = o.customer_id 
WHERE o.purch_amt < ANY (
    SELECT o.purch_amt 
    FROM customer c 
    JOIN orders o ON c.customer_id = o.customer_id 
    WHERE c.city = 'London'
);
```
#### Explanation:
- **Subquery with ANY**: The subquery retrieves all purchase amounts for customers in London.
- **Comparison with ANY**: The main query selects orders with purchase amounts smaller than any purchase amount for customers in London.

#### Query 2 (Alternative using MAX):
```sql
SELECT o.purch_amt, c.customer_id 
FROM customer c 
JOIN orders o ON c.customer_id = o.customer_id 
WHERE o.purch_amt < (SELECT MAX(purch_amt) 
                      FROM orders 
                      JOIN customer ON orders.customer_id = customer.customer_id 
                      WHERE city = 'London');
```
#### Explanation:
- **Subquery with MAX**: This alternative approach calculates the maximum purchase amount among orders for customers in London.
- **Comparison with MAX**: The main query selects orders with purchase amounts smaller than the maximum purchase amount for customers in London.

#### Table Generated
| purch_amt | customer_id |
|-----------|-------------|
| 150.5     | 3005        |
| 270.65    | 3001        |
| 1983.43   | 3004        |
| 75.29     | 3003        |
# <a href = "https://www.lucidchart.com">LUCID</a>

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/f7783673-e4e7-4a17-8530-0526d72ffd69)

<br>

## Cardinality

![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/c1d24cdb-9158-4b98-855a-ad360d8c18a1)

<br>

## Keywords

| Keyword        | Description                                                                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Entity         | Represents a real-world object or concept in the database, such as `Professor`, `Student`, `Course`, and `Enrollment`.                                                                             |
| Attribute      | Describes a property or characteristic of an entity, such as `professor_id`, `professor_name`, `department`, `student_id`, `student_name`, `course_id`, `course_name`, and `enroll_id`.         |
| Primary Key    | A unique identifier for each record in a table. Used to ensure each record is uniquely identifiable and to establish relationships between tables.                                                  |
| Foreign Key    | A column in one table that references the primary key in another table. Used to establish relationships between tables and enforce referential integrity.                                            |
| Relationship   | Describes how entities are related to each other in the database. In this schema, relationships exist between `Professor` and `Course`, `Student` and `Enrollment`, and `Course` and `Enrollment`. |
| One-to-Many    | A relationship where one record in a table is related to many records in another table. For example, one `Professor` can teach many `Courses`.                                                    |
| Many-to-One    | A relationship where many records in a table are related to one record in another table. For example, many `Enrollments` belong to one `Course`.                                                  |
| Cascade Delete | A referential action that automatically deletes associated records in related tables when a record in the parent table is deleted. Used to maintain data integrity.                              |

> Understanding these keywords helps in comprehending the structure and functionality of the database schema, including how entities relate to each other and how data integrity is maintained through keys and relationships.

<br>

## TASK 1

### Salesman Table
| salesman_id | name         | city       | commission |
|-------------|--------------|------------|------------|
| 5001        | James Hoog   | New York   | 0.15       |
| 5002        | Nail Knite   | Paris      | 0.13       |
| 5005        | Pit Alex     | London     | 0.11       |
| 5006        | Mc Lyon      | Paris      | 0.14       |
| 5003        | Lauson Hen   | NULL       | 0.12       |
| 5007        | Paul Adam    | Rome       | 0.13       |

### Order Table
| ord_no | purch_amt | ord_date   | customer_id | salesman_id |
|--------|-----------|------------|-------------|-------------|
| 70001  | 150.50    | 2012-10-05 | 3005        | 5002        |
| 70009  | 270.65    | 2012-09-10 | 3001        | 5005        |
| 70002  | 65.26     | 2012-10-05 | 3002        | 5001        |
| 70004  | 110.50    | 2012-08-17 | 3009        | 5003        |
| 70007  | 948.50    | 2012-09-10 | 3005        | 5002        |
| 70005  | 2400.60   | 2012-07-27 | 3007        | 5001        |
| 70008  | 5760.00   | 2012-09-10 | 3002        | 5001        |
| 70010  | 1983.43   | 2012-10-10 | 3004        | 5006        |
| 70003  | 2480.40   | 2012-10-10 | 3009        | 5003        |
| 70012  | 250.45    | 2012-06-27 | 3008        | 5002        |
| 70011  | 75.29     | 2012-08-17 | 3003        | 5007        |
| 70013  | 3045.60   | 2012-04-25 | 3002        | 5001        |

### Customer Table
| customer_id | cust_name     | city       | grade | salesman_id |
|-------------|---------------|------------|-------|-------------|
| 3002        | Nick Rimando  | New York   | 100   | 5001        |
| 3005        | Graham Zusi   | California | 200   | 5002        |
| 3001        | Brad Guzan    | London     | NULL  | 5005        |
| 3004        | Fabian Johns  | Paris      | 300   | 5006        |
| 3007        | Brad Davis    | New York   | 200   | 5001        |
| 3009        | Geoff Camero  | Berlin     | 100   | 5003        |
| 3008        | Julian Green  | London     | 300   | 5002        |
| 3003        | Jozy Altidor  | Moscow     | 200   | 5007        |

### ER Diagram
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/51b4b0d9-6f28-4b21-a5f0-32bfa991365c)

<br>

## TASK 2

| StudentID | StudentName | CourseID | CourseName | ProfessorID | ProfessorName | Department   |
|-----------|-------------|----------|------------|-------------|---------------|--------------|
| 5001      | Alice       | C001     | Math 101   | POO1        | Dr. Brown     | Mathematics  |
| 5002      | Bob         | C002     | Physics 101| P002        | Dr. Smith     | Physics      |
| 5001      | Alice       | C002     | Physics 101| P002         | Dr. Smith    | Physics      |
| 5003      | Charlie     | C001     | Math 101   | P001        | Dr. Brown     | Mathematics  |

### ER Diagram
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/cfa2c910-306d-4c10-b120-9e389be02a9a)

### SQL Queries

### Creating Tables:

```sql
-- Create Professor table
CREATE TABLE Professor (
  professor_id VARCHAR(255),
  professor_name VARCHAR(255),
  department VARCHAR(255),
  PRIMARY KEY (professor_id)
);

-- Create Student table
CREATE TABLE Student (
  student_id VARCHAR(255),
  student_name VARCHAR(255),
  PRIMARY KEY (student_id)
);

-- Create Course table
CREATE TABLE Course (
  course_id VARCHAR(255),
  course_name VARCHAR(255),
  professor_id VARCHAR(255),
  PRIMARY KEY (course_id),
  FOREIGN KEY (professor_id) REFERENCES Professor(professor_id) ON DELETE CASCADE
);

-- Create Enrollment table
CREATE TABLE Enrollment (
  enroll_id VARCHAR(255),
  course_id VARCHAR(255),
  student_id VARCHAR(255),
  PRIMARY KEY (enroll_id),
  FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE,
  FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE
);
```

### Performing Operations:

#### Making Queries:

```sql
-- Query to retrieve information about student enrollments
SELECT 
    e.student_id AS StudentID, 
    s.student_name AS StudentName, 
    e.course_id AS CourseID, 
    c.course_name AS CourseName, 
    c.professor_id AS ProfessorID, 
    p.professor_name AS ProfessorName, 
    p.department AS Department
FROM 
    Enrollment e
JOIN 
    Student s ON e.student_id = s.student_id
JOIN 
    Course c ON e.course_id = c.course_id
JOIN 
    Professor p ON c.professor_id = p.professor_id;
```

#### Dropping Tables:

```sql
-- Drop Enrollment table
DROP TABLE IF EXISTS Enrollment;

-- Drop Course table
DROP TABLE IF EXISTS Course;

-- Drop Student table
DROP TABLE IF EXISTS Student;

-- Drop Professor table
DROP TABLE IF EXISTS Professor;
```

<br>
## SQL In-Built Functions

### String Functions:
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/1e7fc21f-6681-44f9-a94b-d514d82bab0c)

| Function                                      | Description                                           | Example                                         | Output          |
|-----------------------------------------------|-------------------------------------------------------|-------------------------------------------------|-----------------|
| `CONCAT(str1, str2, ...)`                    | Concatenates strings                                 | `SELECT CONCAT('Hello', ' ', 'World');`        | `Hello World`   |
| `CONCAT_WS(separator, str1, str2, ...)`      | Concatenates strings with a separator                | `SELECT CONCAT_WS('-', '2022', '04', '25');`   | `2022-04-25`    |
| `LENGTH(str)`                                | Returns the length of a string                       | `SELECT LENGTH('Hello');`                      | `5`             |
| `CHAR_LENGTH(str)` or `CHARACTER_LENGTH(str)`| Returns the number of characters in a string         | `SELECT CHAR_LENGTH('Hello');`                 | `5`             |
| `UPPER(str)`                                 | Converts a string to uppercase                       | `SELECT UPPER('hello');`                       | `HELLO`         |
| `LOWER(str)`                                 | Converts a string to lowercase                       | `SELECT LOWER('HELLO');`                       | `hello`         |
| `SUBSTRING(str, start, length)` or `SUBSTR(str, start, length)` | Extracts a substring from a string       | `SELECT SUBSTRING('Hello World', 1, 5);`       | `Hello`         |
| `LEFT(str, length)`                          | Extracts characters from the left of a string        | `SELECT LEFT('Hello World', 5);`               | `Hello`         |
| `RIGHT(str, length)`                         | Extracts characters from the right of a string       | `SELECT RIGHT('Hello World', 5);`              | `World`         |
| `REPLACE(str, search_str, replace_str)`      | Replaces occurrences of a substring in a string     | `SELECT REPLACE('Hello World', 'World', 'Universe');` | `Hello Universe` |
| `LTRIM(str)`                                 | Removes leading spaces from a string                | `SELECT LTRIM('   Hello');`                    | `Hello`         |
| `RTRIM(str)`                                 | Removes trailing spaces from a string               | `SELECT RTRIM('Hello   ');`                    | `Hello`         |
| `TRIM([leading \| trailing \| both] [trim_str] FROM str)` | Removes leading, trailing, or both leading and trailing characters from a string | `SELECT TRIM('   Hello   ');` | `Hello` |
| `REVERSE(str)`                               | Reverses the characters in a string                 | `SELECT REVERSE('Hello');`                     | `olleH`         |
| `LOCATE(substr, str [, start])` or `INSTR(str, substr)` | Searches for a substring in a string and returns its position | `SELECT LOCATE('World', 'Hello World');` | `7` |
| `LPAD(str, length, pad_str)`                 | Left-pads a string with another string              | `SELECT LPAD('Hello', 10, '*');`               | `*****Hello`    |
| `RPAD(str, length, pad_str)`                 | Right-pads a string with another string             | `SELECT RPAD('Hello', 10, '*');`               | `Hello*****`    |


### Mathematical Functions:
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/b5525eb6-89c6-4f94-a296-d0c1346d083e)

| Function                                      | Description                                           | Example                                         | Output          |
|-----------------------------------------------|-------------------------------------------------------|-------------------------------------------------|-----------------|
| `ABS(num)`                                   | Returns the absolute (positive) value of a number    | `SELECT ABS(-5);`                              | `5`             |
| `CEIL(num)` or `CEILING(num)`                | Rounds a number up to the nearest integer            | `SELECT CEIL(3.5);`                            | `4`             |
| `FLOOR(num)`                                 | Rounds a number down to the nearest integer          | `SELECT FLOOR(3.5);`                           | `3`             |
| `ROUND(num [, decimals])`                    | Rounds a number to a specified number of decimal places | `SELECT ROUND(3.14159, 2);`                  | `3.14`          |
| `SIGN(num)`                                  | Returns the sign of a number (-1, 0, or 1)           | `SELECT SIGN(-5);`                             | `-1`            |
| `MOD(num, divisor)`                          | Returns the remainder of a division operation        | `SELECT MOD(10, 3);`                           | `1`             |
| `SQRT(num)`                                  | Returns the square root of a number                  | `SELECT SQRT(25);`                             | `5`             |
| `POWER(num, exponent)`                       | Raises a number to the power of an exponent          | `SELECT POWER(2, 3);`                          | `8`             |
| `RAND([seed])`                               | Returns a random floating-point value between 0 and 1 | `SELECT RAND();`                              | (Random value)  |


### Date Functions:
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/8561d419-094e-4ba1-91bc-847fdb62a65e)

| Function                                      | Description                                           | Example                                         | Output          |
|-----------------------------------------------|-------------------------------------------------------|-------------------------------------------------|-----------------|
| `NOW()`                                      | Returns the current date and time                    | `SELECT NOW();`                                | `2022-04-25 10:30:15` |
| `CURDATE()`                                  | Returns the current date                             | `SELECT CURDATE();`                            | `2022-04-25`    |
| `CURTIME()`                                  | Returns the current time                             | `SELECT CURTIME();`                            | `10:30:15`      |
| `DATE_FORMAT(date, format)`                  | Formats a date according to a specified format       | `SELECT DATE_FORMAT(NOW(), '%Y-%m-%d');`       | `2022-04-25`    |
| `DATE_ADD(date, INTERVAL value unit)`        | Adds a specified value to a date                     | `SELECT DATE_ADD('2022-04-25', INTERVAL 1 MONTH);` | `2022-05-25` |
| `DATE_SUB(date, INTERVAL value unit)`        | Subtracts a specified value from a date              | `SELECT DATE_SUB('2022-04-25', INTERVAL 7 DAY);` | `2022-04-18`   |
| `DATEDIFF(date1, date2)`                     | Returns the number of days between two dates         | `SELECT DATEDIFF('2022-04-30', '2022-04-25');` | `5`             |
| `DAYNAME(date)`                              | Returns the name of the day for a given date         | `SELECT DAYNAME('2022-04-25');`               | `Monday`        |
| `DAYOFMONTH(date)`                           | Returns the day of the month for a given date        | `SELECT DAYOFMONTH('2022-04-25');`            | `25`            |
| `DAYOFWEEK(date)`                            | Returns the day of the week for a given date         | `SELECT DAYOFWEEK('2022-04-25');`             | `2` (Monday)    |
| `DAYOFYEAR(date)`                            | Returns the day of the year for a given date         | `SELECT DAYOFYEAR('2022-04-25');`             | `115`           |
| `MONTH(date)`                                | Returns the month for a given date                   | `SELECT MONTH('2022-04-25');`                 | `4`             |
| `YEAR(date)`                                 | Returns the year for a given date                    | `SELECT YEAR('2022-04-25');`                  | `2022`          |
| `HOUR(time)`                                 | Returns the hour component of a time value           | `SELECT HOUR('10:30:15');`                    | `10`            |
| `MINUTE(time)`                               | Returns the minute component of a time value         | `SELECT MINUTE('10:30:15');`                  | `30`            |
| `SECOND(time)`                               | Returns the second component of a time value         | `SELECT SECOND('10:30:15');`                  | `15`            |
| `TIMESTAMPDIFF(unit, start_datetime, end_datetime)` | Returns the difference between two datetime expressions based on a specified unit | `SELECT TIMESTAMPDIFF(DAY, '2022-04-25', '2022-05-01');` | `6` (days) |
| `TIMESTAMPADD(unit, value, datetime)`       | Adds a specified value to a datetime expression based on a specified unit | `SELECT TIMESTAMPADD(MONTH, 1, '2022-04-25');` | `2022-05-25` |
| `UNIX_TIMESTAMP([datetime])`                | Returns the number of seconds since the Unix epoch   | `SELECT UNIX_TIMESTAMP('2022-04-25 10:30:15');` | `1671970215`   |


# Employee Data Management

### Create EmployeeData Table

```sql
CREATE TABLE EmployeeData (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT,
    StartDate DATE
);
```

### Insert Data into EmployeeData Table

```sql
INSERT INTO EmployeeData (EmployeeID, FirstName, LastName, Salary, StartDate) VALUES
(1, 'John', 'Doe', 70000, '2020-05-01'),
(2, 'Jane', 'Smith', 85000, '2018-08-15'),
(3, 'Emily', 'Jones', 94000, '2019-12-30'),
(4, 'Chris', 'Brown', 62000, '2021-03-22');
```

### Generated EmployeeData Table

| EmployeeID | FirstName | LastName | Salary | StartDate  |
|------------|-----------|----------|--------|------------|
| 1          | John      | Doe      | 70000  | 2020-05-01 |
| 2          | Jane      | Smith    | 85000  | 2018-08-15 |
| 3          | Emily     | Jones    | 94000  | 2019-12-30 |
| 4          | Chris     | Brown    | 62000  | 2021-03-22 |

<br>

## Task 1: Sort Employees by Length of First Names (Descending)

**Intuition:** This task sorts the employees based on the length of their first names in descending order. It's useful for understanding the distribution of name lengths in the dataset.

```sql
SELECT * 
FROM EmployeeData 
ORDER BY LENGTH(FirstName) DESC;
```

### Sorted Employees by Length of First Names (Descending)

| EmployeeID | FirstName | LastName | Salary | StartDate  |
|------------|-----------|----------|--------|------------|
| 3          | Emily     | Jones    | 94000  | 2019-12-30 |
| 2          | Jane      | Smith    | 85000  | 2018-08-15 |
| 4          | Chris     | Brown    | 62000  | 2021-03-22 |
| 1          | John      | Doe      | 70000  | 2020-05-01 |

<br>

## Task 2: Get the Initials JD, JS, EJ, CB

**Intuition:** This task retrieves the initials of each employee by taking the first letter of their first name and the first letter of their last name.

```sql
SELECT CONCAT(SUBSTRING(FirstName, 1, 1), SUBSTRING(LastName, 1, 1)) AS Initials
FROM EmployeeData;
```

### Initials

| Initials |
|----------|
| JD       |
| JS       |
| EJ       |
| CB       |

<br>

## Task 3: Extract and Display the First Three Letters of Each Employee's Last Name in Upper Case

**Intuition:** This task extracts the first three letters of each employee's last name and displays them in upper case. It provides a quick reference for the first few letters of each last name.

```sql
SELECT UPPER(SUBSTRING(LastName, 1, 3)) AS LastnamePrefix
FROM EmployeeData;
```

### Last Name Prefixes

| LastnamePrefix |
|----------------|
| DOE            |
| SMI            |
| JON            |
| BRO            |

<br>

## Task 4: Calculate Tenure of Each Employee in Complete Years as of Today

**Intuition:** This task calculates the tenure of each employee in complete years as of today. It helps in understanding how long each employee has been with the company.

```sql
SELECT 
    EmployeeID, 
    DATEDIFF(CURDATE(), StartDate) / 365 AS TenureInYears
FROM 
    EmployeeData;
```

### Tenure of Each Employee (Years)

| EmployeeID | TenureInYears |
|------------|---------------|
| 1          | 2             |
| 2          | 4             |
| 3          | 2             |
| 4          | 1             |
