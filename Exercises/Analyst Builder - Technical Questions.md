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

## [Million Dollar Store](https://www.analystbuilder.com/questions/million-dollar-store-ARdQa)
### Python
```
import pandas as pd;
stores_2 = stores.groupby(by='store_id', as_index=False).mean()[['store_id','revenue']]
stores_2['revenue'] = round(stores_2['revenue'],2)
stores_2[stores_2['revenue']>1000000].sort_values('store_id')
```
### PostgreSQL
```
SELECT store_id, ROUND(AVG(revenue),2)
FROM stores
GROUP BY store_id
HAVING AVG(revenue) > 1000000
ORDER BY store_id ASC;
```

## [Separation](https://www.analystbuilder.com/questions/separation-DbHMu)
### Python
```
import pandas as pd;
bad_data['first_name'] = bad_data['id'].apply(lambda x: x[5:])
bad_data['id'] = bad_data['id'].apply(lambda x: x[:5])
bad_data
```
### PostgreSQL
```
SELECT LEFT(id,5) as id, RIGHT(id,LENGTH(id)-5) as first_name
FROM bad_data
```

## [Low Quality YouTube Videos](https://www.analystbuilder.com/questions/low-quality-youtube-video-idbeu)
### Python
```
import pandas as pd;
youtube_videos['like_pct'] = youtube_videos['thumbs_up'] / (youtube_videos['thumbs_up'] + youtube_videos['thumbs_down'])
youtube_videos[youtube_videos['like_pct'] < 0.55][['video_id']].sort_values('video_id')
```
### PostgreSQL
```
SELECT video_id
FROM youtube_videos
WHERE thumbs_up*100/(thumbs_up + thumbs_down) < 55
ORDER BY video_id ASC;
```

## []()
### Python
```

```
### PostgreSQL
```

```

