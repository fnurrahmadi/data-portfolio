# [DataLemur - SQL Interview Question](https://leetcode.com/studyplan/30-days-of-pandas/)

## [Histogram of Tweets [Twitter SQL Interview Question]](https://datalemur.com/questions/sql-histogram-tweets)
```
SELECT tweet_bucket, COUNT(1) AS users_num
FROM (SELECT user_id, COUNT(1) AS tweet_bucket
  FROM tweets
  WHERE EXTRACT(YEAR FROM tweet_date) = '2022'
  GROUP BY 1) a
GROUP BY 1;
```

## [Data Science Skills [LinkedIn SQL Interview Question]](https://datalemur.com/questions/matching-skills)
```
SELECT candidate_id
FROM candidates
GROUP BY 1
HAVING SUM(CASE WHEN skill IN ('Python','Tableau','PostgreSQL') THEN 1 ELSE 0 END) = 3
ORDER BY 1 ASC;
```

## [Page With No Likes [Facebook SQL Interview Question]](https://datalemur.com/questions/sql-page-with-no-likes)
```
SELECT p.page_id
FROM pages p
LEFT JOIN page_likes l
  ON p.page_id = l.page_id
GROUP BY 1
HAVING COALESCE(COUNT(user_id),0) = 0
ORDER BY 1 ASC;
```

## []()
```

```

