# [LeetCode - 30 Days of Pandas](https://leetcode.com/studyplan/30-days-of-pandas/)

## [Big Countries](https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['area']>=3000000) | (world['population']>=25000000)][['name','population','area']]
```

## [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats']=='Y')&(products['recyclable']=='Y')][['product_id']]
```

## [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    df = df.rename(columns={'name':'Customers'})
    return df[df['customerId'].isnull()][['Customers']]
```

## [Article Views I](https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views['author_id'] == views['viewer_id']][['author_id']].drop_duplicates().sort_values('author_id').rename(columns={'author_id':'id'})
```

## []()
```

```