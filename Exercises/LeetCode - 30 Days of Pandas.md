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

## [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len()>15][['tweet_id']]
```

## [Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if (x['employee_id']%2!=0) & ~(x['name'].lower().startswith('m')) else 0, axis=1)
    return employees[['employee_id','bonus']].sort_values('employee_id')
```

## [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')
```

## [Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.match('^[A-Za-z][A-Za-z_0-9\-\.\_]*@leetcode\.com$')]
```

## [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata)
```
import pandas as pd
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains('^DIAB1| DIAB1')]
```

## []()
```

```