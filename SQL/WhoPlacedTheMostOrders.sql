CREATE TABLE IF NOT EXISTS `order1` (
  `order_number` int(6) unsigned NOT NULL,
  `customer_number` int(3) unsigned NOT NULL,
  PRIMARY KEY (`order_number`,`customer_number`)
) DEFAULT CHARSET=utf8;
INSERT INTO `order1` (`order_number`, `customer_number`) VALUES
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4', '3');

select customer_number 
from (select customer_number, count(order_number) order_count 
from order1 group by customer_number) a 
order by order_count 
desc limit 1