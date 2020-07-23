
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

# Primary and foreign keys 

Primary keys are columns or sets of columns in a table whose values uniquely identify a row in the table. A relational  
  
database is designed to enforce by only allowing one row with a given primary key 
 
As an example, a student id might be a primary key in a student table, a department code in a table of all departments in  
an organisation.
![priamry.jpg](http://rdbms.opengrass.net/2_Database%20Design/2.1_TermsOfReference/r/keyPrimary.gif)       
 
The studentId would serve as a main reference and is used throughout the database to help establish relationships with  

other tables.  The primary key must contain unique values, must never be null and uniquely  

identify each record in the table. 
 
The foreign key is a column that creates a relationship between two tables. The purpose of Foreign keys is to maintain  
 
data integrity and allow navigation between two different instances of an entity. It acts as a cross-reference between  
  
two tables as it references the primary key of another table.
 
![foreign.jpg](https://i.imgur.com/fj0yOiF.png)    
 
In this example CourseId would be the primary key of one instance and called into another table to be the foreign key. 
 
# Types of relationships 
When creating a database, common sense dictates that we use separate tables for different types of entities. Some  

examples are: customers, orders, items, messages etc... But we also need to have relationships between these tables. For   
instance, customers make orders, and orders contain items. These relationships need to be represented in the database. 

* One to One Relationships
* One to Many and Many to One Relationships
* Many to Many Relationships
* Self Referencing Relationships
 
 ### One to One Relationships 
In a one-to-one relationship, one record in a table is associated with one and only one record in another table. For example, in a school database, each student has only one student ID, and each student ID is assigned to only one person.

A one-to-one relationship looks like this in the relationships graph: 
![onetoone.jpg](https://fmhelp.filemaker.com/help/18/fmp/en/FMP_Help/images/one-to-one.png) 
  
In this example, the key field in each table, Student ID, is designed to contain unique values. In the Students table, the Student ID field is the primary key; in the Contact  
 
Info table, the Student ID field is a foreign key.

This relationship returns related records when the value in the Student ID field in the Contact Info table is the same as the Student ID field in the Students table.   

![onetoone.jpg](https://fmhelp.filemaker.com/help/18/fmp/en/FMP_Help/images/relational.07.03.2.png)   
 
Basically only one element in Table A can only be linked to one element on Table B, and vice versa. 

 ### One to Many Relationships  
 This is the most commonly used type of relationship. Consider an e-commerce website, with the following:
 
*Customers can make many orders.
  
*Orders can contain many items.
 
*Items can have descriptions in many languages.
 
*In these cases we would need to create "One to Many" relationships. Here is an example:
 
![onetomany.jpg](https://cdn.tutsplus.com/net/uploads/legacy/538_sql3/ss_3.png)   
 
 Notice how more than one order_id is attached to one customer_id, but an order can only belong to one customer. 
  
![onetomany.jpg](https://cdn.tutsplus.com/net/uploads/legacy/538_sql3/graph_2.png)    
 
 ### Many to Many Relationships 
In some cases, you may need multiple instances on both sides of the relationship. For example, each order can contain  

multiple items. And each item can also be in multiple orders.

Let’s say you have a list of books, and a list of authors—each book may have one or more authors, and each author may  
 
have written multiple books. In this case, you have many books related to many authors. 
 
![manytomany.jpg](https://support.airtable.com/hc/en-us/article_attachments/206808577/Screen_Shot_2016-04-26_at_3.02.52_PM.png)
However Relational database systems usually don't allow you to implement a direct many-to-many relationship between two  

tables. Consider the example of keeping track of invoices. If there were many invoices with the same invoice number and  

one of your customers inquired about that invoice number you wouldn't know which number they were referring to. This is  

one reason for assigning a unique value to each invoice. 
 
To avoid this problem, you can break the many-to-many relationship into two one-to-many relationships by using a third  

table, called a join table. Each record in a join table includes a match field that contains the value of the primary  

keys of the two tables it joins. (In the join table, these match fields are foreign keys.) These foreign key fields are  
 
populated with data as records in the join table are created from either table it joins. Which would look something like  
this.     
 
![manytomany.jpg](https://blog.sqlauthority.com/i/b/j2p/j2p_8_2.jpg) 

With this example we can see that multiple items were ordered several items and some were ordered more than once on  
 
different dates.  

### Junction Tables  
 
When you need to establish a many-to-many relationship between two groups, the simplest solution is to use a Junction  

Table. A Junction Table (sometimes referred to as a "Bridge Table") is a table that contains references to both groups;  
 
bridging them together. For example: A school includes two groups: Students and Classes. One student can attend many  

classes, and one class can contain many students. Hence, the "many-to-many" relationship between students and classes.  

Here's how you relate the two groups using a Junction Table:  

![junctions.jpg](https://www.utteraccess.com/w/images/2/21/JunctionTableExample1.jpg) 

The Junction Table, tblClassMembers, contains one record for each student/class combination. Note that tblClassMembers  

can contain additional information about that combined piece of information: strSeatLocation. Because you know the  

student and the class, you can describe where the student sits during that class. 

### Recursive Relationship or Unary Relationship
When there is a relationship between two entities of the same type, it is known as a recursive relationship. This means  
 
that the relationship is between different instances of the same entity type.

Here is an easy way to understand this concept 

![recursive.jpg](https://i.stack.imgur.com/DzIwq.png) 
In this example A manager supervises a subordinate. Every employee can have a supervisor in their department and there  

can be at most one boss for each employee however one employee may be the boss of more than one employee. It's almost  

like a cycle that repeats itself  

### Crow's foot 
 
To understand the concept of a crow's foot, we must first discuss the term cardinality. 

Now what is cardinality? 

In a simple way to explain, while we write up a schema we create things called data structures, these structure are  
 
called Entity Relationship Diagrams. 
 
An Entity Relationship Diagram shows entities (tables) in a database and relationships between tables within that  

database. For a good database design it is essential to have an Entity Relationship Diagram. 

![erd.jpg](https://cdn-images.visual-paradigm.com/guide/data-modeling/what-is-erd/17-dfd-data-store-modeled-by-erd.png)  
 
In data modeling, cardinality refers to the relationship of data in one database table with respect to another table.  

The way we represent the relationship or cardinality is by using a crow foot notation 

![cardinality.jpg](https://i.stack.imgur.com/uuDiz.jpg)  
 
Notice how the relations kind of look like the foot of a bird, with more and more arrows going into each entity. 

This would be known as the crow foot notation. Basically it's a name for a set of ways to represent different relationships.
