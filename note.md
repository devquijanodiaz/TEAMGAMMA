
# SQl notes

A schema is a collection of database objects including tables, views, triggers, stored procedures, indexes, etc.

A schema is associated with a username which is known as the schema owner

who is the owner of the logically related database objects.

![schema.jpg](https://i.stack.imgur.com/cBg5l.png)

This is an example of a schema

With the schema in hand. We can use the data to ask for certain questions

For example 'Tell me how many books there are on computer programming' or

'How many Rolling Stones albums were produced before 1980?'

When we ask the database for information we are performing a task called a query

A query is simply a request for data within certain parameters.

This is very useful than having to sift to massive logs of data looking for certain tiny details.

## SQl Commands

The SELECT statement is used to select data from a database.

The data returned is stored in a result table, called the result-set.

![select.jpg](https://i.imgur.com/voNXhD8.png)

The above example is a show case of the usage of the select command

You can also perform a bunch of other tasks with the select command

as in specifying certain elements depending on what tables you have in your schema

The WHERE clause is used to filter records.

The WHERE clause is used to extract only those records that fulfill a specified condition.

![where.jpg](https://i.imgur.com/ZASw1X4.png)

In this example, we are selecting from the column of city where the variable matches the country of Mexico ![where.jpg](https://i.imgur.com/SbhK8cW.png)

In this example, we are searching a similar search for only where the id of the customer equals to 1\.

SQL requires single quotes around text values (most database systems will also allow double quotes).

However, numeric fields should not be enclosed in quotes:

The GROUP BY Statement in SQL is used to arrange identical data into groups with the help of some functions.

i.e if a particular column has same values in different rows then it will arrange these rows in a group.

SELECT SUBJECT, YEAR, Count(*)

FROM Student

GROUP BY SUBJECT, YEAR;

![where.jpg](https://i.imgur.com/HhI1ISA.png)

This would give the following outcome

![subject.jpg](https://i.imgur.com/iPXmphP.png)

The HAVING clause is often used with the GROUP BY clause in the SELECT statement.

If you use a HAVING clause without a GROUP BY clause, the HAVING clause behaves like the WHERE clause.

An easy way to understand the difference is that WHERE clause introduces a condition on individual rows;

HAVING clause introduces a condition on aggregations,

i.e. results of selection where a single result, such as count, average, min, max, or sum,

has been produced from multiple rows

![employee.png](https://cdn.sqltutorial.org/wp-content/uploads/2016/03/employees_dependents_tables.png)

Using this example Schema, to get the managers and their direct reports,

you use the GROUP BY clause to group employees by the managers and

use the COUNT function to count the direct reports.

![where.jpg](https://i.imgur.com/HhI1ISA.png)

You would get the following result

![where.jpg](https://cdn.sqltutorial.org/wp-content/uploads/2016/03/SQL-HAVING-example.png)

The ORDER BY keyword is used to sort the result-set in ascending or descending order.

The ORDER BY keyword sorts the records in ascending order by default.

To sort the records in descending order, use the DESC keyword.

To sort the records in ascending order, use the ASC keyword.

The following is an example of this query

![where.jpg](https://i.imgur.com/sMpZ0rq.png)

This query would reverse the countries going from the bottomost to the top

# Additional notes

SQL is case sensitive like all of the other stuff we were doing, a off note can give you a syntax error

