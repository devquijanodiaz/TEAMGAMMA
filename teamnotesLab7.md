# SLIDE 7

Sorting
Ascending(ASC) order will sort the information from lowest to highest starting from the top >bottom. 
Descending(DESC) does the same but in opposite order
ORDER BY clause is entered at the end of the SELECT statement. So you would do ORDER BY column1 ASC; which would organize the colum1 in ascending order.

Syntax below:
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC; 



# Rank Function:

Using RANK() OVER(PARTITION BY repid ORDER BY qty DESC) AS ‘Rank’ creates a new column Rank where repid is partitioned and qty is in descending order within the partitioned repid colum.
Syntax as follows:
	SELECT  repid, qty, custnum,
	RANK() OVER(PARTITION BY repid ORDER BY qty DESC) AS ‘Rank’
	FROM sales
	WHERE qty > 300




The DENSE_RANK Function
Syntax as follows:
	SELECT repid, qty, custnum,
DENSE_RANK() OVER(PARTITION BY repid ORDER BY qty DESC) AS ‘	Dense rank’
FROM sales

For more information about Rank :   <https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-rank-function/>

#Group Function:
The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country".
The GROUP BY statement is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.
Syntax below:
SELECT column_name(s) FROM table_name WHERE condition
GROUP BY column_name(s) ORDER BY column_name(s); 
# The Having Clause:
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
Example below:
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
# The Rollup Function:
The SQL Server ROLLUP is a subclause of the GROUP BY clause which provides a shorthand for defining multiple grouping sets. 
When generating the grouping sets, ROLLUP assumes a hierarchy among the dimension columns and only generates grouping sets based on this hierarchy.
The ROLLUP is commonly used to calculate the aggregates of hierarchical data such as sales by year > quarter > month.


# LAB 7



So our team queried by typing SELECT sldate, partnum, qty, custnum, which is pulling those specific columns.  After the proper columns have been selected, use RANK() in order to create a new column called quantity_rank. This will be ordered by qty descending and partitioned by the month name of the date in the sldate. To do this, type the following query:

SELECT sldate, partnum, qty, custnum, RANK() OVER (PARTITION by MONTHNAME(sldate) ORDER BY qty DESC) quantity_rank FROM pub1.sales ORDER BY quantity_rank;




Partitioning is a way in which a database (MySQL in this case) splits its actual data down into separate tables, but still gets treated as a single table by the SQL layer. When partitioning in MySQL, it's a good idea to find a natural partition key.





