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

## []()
```

```