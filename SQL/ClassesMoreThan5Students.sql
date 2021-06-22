-- There is a table courses with columns: student and class

-- Please list out all classes which have more than or equal to 5 students.

-- For example, the table:

/*

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+

*/

select class from 
(
    select class
    from courses 
    group by class
    having count(class)>=5 
) a
order by class desc



-- borrowed from https://stackoverflow.com/q/7745609/808921

CREATE TABLE IF NOT EXISTS `test` (
  `article_id` int(6) unsigned NOT NULL,
  `author_id` int(3) unsigned NOT NULL,
  `viewer_id` int(3) unsigned not NULL,
  -- PRIMARY KEY (`order_number`,`customer_number`)
) 
INSERT INTO `test` (`article_id`, `author_id`, `viewer_id`) VALUES
  ('1', '3', '5'),
  ('1', '3', '6'),
  ('2', '7', '7'),
  ('4', '7', '1');
  ('3', '4', '4');
  ('3', '4', '4');


CREATE TABLE IF NOT EXISTS `test` (
  `article_id` int(6) unsigned NOT NULL,
  `author_id` int(3) unsigned NOT NULL,
  `viewer_id` int(3) unsigned not NULL,
  PRIMARY KEY (`article_id`)
) 

INSERT INTO `test` (`article_id`, `author_id`, `viewer_id`) VALUES
  (1, 3, 5);