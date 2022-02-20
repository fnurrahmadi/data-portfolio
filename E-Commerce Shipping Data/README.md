# E-Commerce Shipping Data

to be continued

# Exploratory Data Analysis

## Univariate Analysis

From the numerical features, such are our findings:

- `prior_purchases` is relatively right-skewed, and `discount_offered` is right-skewed with a long tail to the right.
- The ratio of `late_delivery` to on-time delivery is 60:40 (more late deliveries).
- `customer_care_calls` has a mode of 4 and is relatively right-skewed.
- `customer_rating` is uniformly distributed.
- Both `cost_of_the_product` and `weight_in_gms` have a bimodal distribution.

From the categorical features, such are our findings:
- `warehouse_block` F has the most shipment, while the other warehouse blocks are significantly lower and have a uniform amount.
- Ship is the most used `mode_of_shipment`.
- From `product_importance`, low has the most shipment, then medium and high respectively.
- Based on `gender`, there is not significant difference in the amount of shipments.

## Multivariate Analysis

to be continued

# Business Insights

to be continued

# Data Preprocessing

The list of steps done in this section are as below:

1. No *missing*, *duplicate*, *redundant*, or *invalid* data
2. Checking *outliers* using *Z-score* and filtering rows with Z-scores bigger than 3
    - Rows with outliers: 10999
    - Rows without outliers: 10642
3. Handling *class imbalance* using *SMOTE oversampling* with a ratio of *0.75*
    - Before sampling: 6282 to 4360
    - After sampling: 6282 to 4711
4. *Splitting data* into train and test set with a ratio of *80:20*
5. *Transforming* distributions (`weight_in_gms`, `prior_purchases`, `discount_offered`, `cost_of_the_product`) using *np.sqrt*
6. *Scaling* numerical features using *MinMaxScaler*
7. *Label encoding* for `gender` (M = 1, F = 0)
8. *One-hot-encoding* for `warehouse_block`, `mode_of_shipment`, and `product_importance`

*Steps 5, 6, and 7* are then executed on the test data as well.

# Feature Selection

To find the features with the best predictive power, a few steps are run, listed as below:

1. Scoring the predictive power of categorical features using *Chi-Squared* test
2. Calculating *feature importances* using *RandomForestClassifier*
3. Setting *feature rankings* using a wrapper method of RandomForestClassifier called *Boruta*
4. Checking *multicollinearity* with *Pearson correlation matrix*

After running the steps above, the features selected are as below:
- `cost_of_the_product`
- `discount_offered`
- `trf_weight_in_gms`
- `product_importance_high`

# Machine Learning Modelling

The goal of this project is to predict late deliveries and minimize the number of False Negatives. As it is more important to predict late deliveries rather than on-time deliveries, the minimum set metrics are as such:

- 0.75 Recall Score for late delivery, and
- 0.50 Recall Score for on-time delivery

The list of steps to find the best model are as below:

- Using *lazypredict* to predict and evaluate using 20+ classification models efficiently
- Cross-validating and evaluating the prediction of the well-performing models from lazypredict
- Hyperparameter tuning and selecting the best prediction model

# Business Recommendation

to be continued

# Future Works

to be continued