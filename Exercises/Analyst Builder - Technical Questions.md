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
import pandas as pd;
customers[(customers['age']>65)|(customers['total_purchase']>200)]['customer_id'].count()
```
### PostgreSQL
```
SELECT COUNT(1)
FROM customers
WHERE age > 65
OR total_purchase > 200
```

## [Electric Bike Replacement](https://www.analystbuilder.com/questions/electric-bike-replacement-ZaFie)
### Python
```
import pandas as pd;
bikes[bikes['miles']>10000]['bike_id'].count()
```
### PostgreSQL
```
SELECT COUNT(1)
FROM bikes 
WHERE miles > 10000
```

## [TMI (Too Much Information)](https://www.analystbuilder.com/questions/tmi-too-much-information-VyNhZ)
### Python
```
import pandas as pd;
customers[['first_name', 'last_name']] = customers['full_name'].str.split(' ', expand=True)
customers[['customer_id','first_name']]
```
### PostgreSQL
```
SELECT customer_id, SPLIT_PART(full_name,' ',1)
FROM customers;
```

## [Costco Rotisserie Loss](https://www.analystbuilder.com/questions/costco-rotisserie-loss-kkCDh)
### Python
```
import pandas as pd;
round(sales['lost_revenue_millions'].sum())
```
### PostgreSQL
```
SELECT ROUND(SUM(lost_revenue_millions))
FROM sales;
```

## []()
### Python
```

```
### PostgreSQL
```

```

