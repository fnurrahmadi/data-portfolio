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

## []()
```

```