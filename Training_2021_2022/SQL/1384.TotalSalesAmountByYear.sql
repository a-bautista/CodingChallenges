/*
Table: Product

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
+---------------+---------+
product_id is the primary key for this table.
product_name is the name of the product.
 

Table: Sales

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| product_id          | int     |
| period_start        | date    |
| period_end          | date    |
| average_daily_sales | int     |
+---------------------+---------+
product_id is the primary key for this table. 
period_start and period_end indicate the start and end date for the sales period, and both dates are inclusive.
The average_daily_sales column holds the average daily sales amount of the items for the period.
The dates of the sales years are between 2018 to 2020.
 

Write an SQL query to report the total sales amount of each item for each year, with corresponding product_name, product_id, product_name, and report_year.

Return the result table ordered by product_id and report_year.

The query result format is in the following example.


Example 1:

Input: 
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 1          | LC Phone     |
| 2          | LC T-Shirt   |
| 3          | LC Keychain  |
+------------+--------------+
Sales table:
+------------+--------------+-------------+---------------------+
| product_id | period_start | period_end  | average_daily_sales |
+------------+--------------+-------------+---------------------+
| 1          | 2019-01-25   | 2019-02-28  | 100                 |
| 2          | 2018-12-01   | 2020-01-01  | 10                  |
| 3          | 2019-12-01   | 2020-01-31  | 1                   |
+------------+--------------+-------------+---------------------+
Output: 
+------------+--------------+-------------+--------------+
| product_id | product_name | report_year | total_amount |
+------------+--------------+-------------+--------------+
| 1          | LC Phone     |    2019     | 3500         |
| 2          | LC T-Shirt   |    2018     | 310          |
| 2          | LC T-Shirt   |    2019     | 3650         |
| 2          | LC T-Shirt   |    2020     | 10           |
| 3          | LC Keychain  |    2019     | 31           |
| 3          | LC Keychain  |    2020     | 31           |
+------------+--------------+-------------+--------------+
Explanation: 
LC Phone was sold for the period of 2019-01-25 to 2019-02-28, and there are 35 days for this period. Total amount 35*100 = 3500. 
LC T-shirt was sold for the period of 2018-12-01 to 2020-01-01, and there are 31, 365, 1 days for years 2018, 2019 and 2020 respectively.
LC Keychain was sold for the period of 2019-12-01 to 2020-01-31, and there are 31, 31 days for years 2019 and 2020 respectively.

*/

/*

Schema creation

CREATE TABLE product (
  product_id INT,
  product_name varchar(20)
);

CREATE TABLE sales (
  product_id INT, 
  period_start date,
  period_end date,
  average_daily_sales int
);

INSERT INTO product (product_id, product_name) VALUES (1, 'LC_Phone');
INSERT INTO product (product_id, product_name) VALUES (2, 'LC T-Shirt');
INSERT INTO product (product_id, product_name) VALUES (3, 'LC Keychain');


INSERT INTO sales (product_id, period_start, period_end, average_daily_sales) VALUES (1, '2019-01-25', '2019-02-28', 100);
INSERT INTO sales (product_id, period_start, period_end, average_daily_sales) VALUES (2, '2018-12-01', '2020-01-01', 10);
INSERT INTO sales (product_id, period_start, period_end, average_daily_sales) VALUES (3, '2019-12-01', '2020-01-31', 1);

https://www.db-fiddle.com/f/uqjxGgagfPXUGZieUT9wp5/0

*/

# Write your MySQL query statement below
with t1 as(select product_id,
                average_daily_sales*(datediff(least('2018-12-31',period_end), greatest('2018-01-01',period_start))+1) 2018sales,
                average_daily_sales*(datediff(least('2019-12-31',period_end), greatest('2019-01-01',period_start))+1) 2019sales,
                average_daily_sales*(datediff(least('2020-12-31',period_end), greatest('2020-01-01',period_start))+1) 2020sales
            from Sales),
    t2 as (select product_id, '2018' report_year, 2018sales as total_amount
            from t1
            where 2018sales>0
            union all
            select product_id, '2019' report_year, 2019sales as total_amount
            from t1
            where 2019sales>0
            union all
            select product_id, '2020' report_year, 2020sales as total_amount
            from t1
            where 2020sales>0
            order by 1,2)
select t2.product_id , product_name , report_year,total_amount
from t2 
join Product p
on t2.product_id=p.product_id