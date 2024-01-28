# [LeetCode - SQL 50](https://leetcode.com/studyplan/top-sql-50/)

## [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT product_id
FROM PRODUCTS
WHERE low_fats = 'Y'
    AND recyclable = 'Y';
```

## [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT name
FROM Customer
WHERE COALESCE(referee_id,0) <> 2;
```

## [Big Countries](https://leetcode.com/problems/big-countries/submissions/1151532070/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT name, population, area
FROM World
WHERE area >= 3000000
    OR population >= 25000000;
```

## [Article Views I](https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id;
```

## [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```

## [Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT u.unique_id, e.name
FROM Employees e
    LEFT JOIN EmployeeUNI u
    ON e.id = u.id;
```

## [Product Sales Analysis](https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT p.product_name, s.year, s.price
FROM Sales s
    LEFT JOIN Product p
    ON s.product_id = p.product_id;
```

## [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT
v.customer_id,
COUNT(v.visit_id) - COUNT(t.transaction_id) AS count_no_trans
FROM Visits v
    LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
GROUP BY v.customer_id
HAVING (COUNT(v.visit_id) - COUNT(t.transaction_id)) > 0;
```

## [Rising Temperature](https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT w.id
FROM Weather w
WHERE w.temperature > (SELECT z.temperature FROM Weather z WHERE w.recordDate - interval '1 day' = z.recordDate);
```

## [Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50)
```
WITH a AS (
SELECT machine_id,
    process_id,
    SUM(
        CASE WHEN activity_type = 'end' THEN timestamp ELSE 0 END -
        CASE WHEN activity_type = 'start' THEN timestamp ELSE 0 END
    ) AS x
FROM Activity
GROUP BY 1,2
)
SELECT machine_id, ROUND(CAST(AVG(x) AS numeric),3) AS processing_time
FROM a
GROUP BY 1;
```

## [Employee Bonus](https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT e.name, b.bonus
FROM Employee e
    LEFT JOIN Bonus b
    ON e.empID = b.empId
WHERE COALESCE(b.bonus,0) < 1000;
```

## [Students and Examinations](https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT s1.student_id, s1.student_name, s2.subject_name,
    (SELECT COUNT(e.student_id) FROM Examinations e WHERE e.student_id = s1.student_id AND e.subject_name = s2.subject_name) AS attended_exams
FROM Students s1
    CROSS JOIN Subjects s2
GROUP BY 1,2,3
ORDER BY 1,3;
```

## [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50)
```
WITH table_1 AS (
    SELECT managerId, COUNT(1) AS direct
    FROM Employee
    GROUP BY 1
    HAVING COUNT(1) >= 5
)
SELECT e.name
FROM Employee e
    INNER JOIN table_1 t
    ON t.managerId = e.id;
```

## [Confirmation Rate](https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50)
```
WITH rate AS (
    SELECT user_id,
    SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed,
    COUNT(1) AS total
    FROM Confirmations
    GROUP BY 1
)
SELECT s.user_id, ROUND(COALESCE(r.confirmed/r.total::numeric,0),2) AS confirmation_rate
FROM Signups s
    LEFT JOIN rate r
    ON s.user_id = r.user_id;
```

## [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT *
FROM Cinema
WHERE id % 2 <> 0
    AND description NOT LIKE 'boring'
ORDER BY rating DESC;
```

## [Average Selling Price](https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT p.product_id,
    COALESCE(ROUND(SUM(u.units*p.price) / SUM(u.units)::numeric,2),0) AS average_price
FROM Prices p
    LEFT JOIN UnitsSold u
    ON u.product_id = p.product_id
        AND u.purchase_date BETWEEN p.start_date AND p.end_date 
GROUP BY 1;
```

## [Project Employees I](https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT p.project_id, ROUND(AVG(e.experience_years),2) AS average_years
FROM Project p
    INNER JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY 1;
```

## [Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT r.contest_id,
ROUND(100*COUNT(1) / (SELECT COUNT(1) FROM Users)::numeric,2) AS percentage
FROM Register r
GROUP BY 1
ORDER BY 2 DESC, 1 ASC;
```

## [Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT q.query_name,
    ROUND(AVG(rating/position::numeric),2) AS quality,
    ROUND(100*SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(1)::numeric,2) AS poor_query_percentage
FROM Queries q
WHERE q.query_name IS NOT NULL
GROUP BY 1;
```

## [Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month, country,
    COUNT(1) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY 1,2;
```

## [Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT ROUND(100 * COUNT(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE NULL END) / COUNT(1)::numeric, 2) AS immediate_percentage
FROM Delivery d
WHERE d.order_date = (SELECT MIN(z.order_date) FROM Delivery z WHERE z.customer_id = d.customer_id);
```

## [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50)
```
SELECT ROUND(COUNT(1) / (SELECT COUNT(DISTINCT c.player_id) FROM Activity c)::numeric,2) AS fraction
FROM Activity a
WHERE a.event_date = (SELECT MIN(b.event_date) FROM Activity b WHERE b.player_id = a.player_id) + interval '1 day'
```

## []()
```

```

