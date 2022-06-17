/*
Table: Cinema

+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment primary key column for this table.
Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.
 

Write an SQL query to report all the consecutive available seats in the cinema.

Return the result table ordered by seat_id in ascending order.

The test cases are generated so that more than two seats are consecutively available.

The query result format is in the following example.

 

Example 1:

Input: 
Cinema table:
+---------+------+
| seat_id | free |
+---------+------+
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
+---------+------+
Output: 
+---------+
| seat_id |
+---------+
| 3       |
| 4       |
| 5       |
+---------+

*/

-- create a table
CREATE TABLE cinema (
  seat_id INTEGER PRIMARY KEY,
  free boolean
);
-- insert some values
INSERT INTO cinema VALUES (1, 1);
INSERT INTO cinema VALUES (2, 0);
INSERT INTO cinema VALUES (3, 1);
INSERT INTO cinema VALUES (4, 1);
INSERT INTO cinema VALUES (5, 1);
INSERT INTO cinema VALUES (6, 0);
INSERT INTO cinema VALUES (7, 1);
INSERT INTO cinema VALUES (8, 1);

-- fetch some values
-- SELECT customer_number
-- FROM orders
-- group by customer_number
-- order by count(*) desc
-- limit 1

SELECT seat_id
FROM cinema
WHERE free = 1 AND (
    seat_id - 1 IN (SELECT seat_id FROM cinema WHERE free = 1)
    OR
    seat_id + 1 IN (SELECT seat_id FROM cinema WHERE free = 1)
);