/*

Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key for this table.
This table contains information about the order ID and the customer ID.
 

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.

The query result format is in the following example.

 

Example 1:

Input: 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
Output: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
Explanation: 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.

CREATE TABLE orders (
  order_number INTEGER PRIMARY KEY,
  customer_number TEXT NOT NULL
);

-- insert some values
INSERT INTO orders VALUES (1, 1);
INSERT INTO orders VALUES (2, 2);
INSERT INTO orders VALUES (3, 3);
INSERT INTO orders VALUES (4, 3);
INSERT INTO orders VALUES (5, 2);

*/


select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1

/*
    Follow up question: 
    What if more than one customer have the largest number of orders, can you find all the customer_number in this case?
*/

select customer_number from
(
    select *,rank() over (order by sum_cust_number desc) as most_ordered_customer
    from
        (
        select customer_number, count(customer_number) as sum_cust_number
        from orders
        group by 1
        )a
)b
where most_ordered_customer=1;