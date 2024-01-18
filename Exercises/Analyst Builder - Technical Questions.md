# Analyst Builder - Technical Questions

## [Media Addicts](https://www.analystbuilder.com/questions/media-addicts-deISZ)
### Python
```
import pandas as pd;
avg_time = user_time['media_time_minutes'].mean()
user_time_2 = user_time[user_time['media_time_minutes'] > avg_time]
users.merge(user_time_2, on='user_id').sort_values(by='first_name', ascending=True)[['first_name']]
```
### PostgreSQL
```
SELECT u.first_name
FROM users u
  INNER JOIN user_time ut
    ON u.user_id = ut.user_id
WHERE ut.media_time_minutes > (SELECT AVG(media_time_minutes) FROM user_time)
ORDER BY u.first_name ASC;
```

## [Heart Attack Risks](https://www.analystbuilder.com/questions/heart-attack-risk-FKfdn)
### Python
```
import pandas as pd;
patients[(patients['age']>50)&(patients['cholesterol']>=240)&(patients['weight']>=200)].sort_values(by='cholesterol', ascending=False)
```
### PostgreSQL
```
SELECT *
FROM patients
WHERE age > 50
AND cholesterol >= 240
AND weight >= 200
ORDER BY cholesterol DESC
```

## [On The Way Out](https://www.analystbuilder.com/questions/on-the-way-out-LGNoQ)
### Python
```
import pandas as pd;
employees['birth_date'] = pd.to_datetime(employees['birth_date'])
employees.sort_values(by='birth_date', ascending=True).head(3)[['employee_id']]
```
### PostgreSQL
```
SELECT employee_id
FROM employees 
ORDER BY birth_date ASC
LIMIT 3;
```

## [Chocolate](https://www.analystbuilder.com/questions/chocolate-vPiUY)
### Python
```
import pandas as pd;
bakery_items[bakery_items['product_name'].str.lower().str.contains('chocolate')]
```
### PostgreSQL
```
SELECT product_name FROM bakery_items
WHERE LOWER(product_name) LIKE '%chocolate%';
```

## [Apply Discount](https://www.analystbuilder.com/questions/apply-discount-RdWhb)
### Python
```

```
### PostgreSQL
```

```

## []()
### Python
```

```
### PostgreSQL
```

```

