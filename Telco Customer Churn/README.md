# TELCO CUSTOMER CHURN

It's no surprise to say that companies suffer when their customers cancel their subscription and stop using their services. A particular telecommunication company requires help in coming up with a business solution in order to solve their issue with customers churning. Apart from that, the company would also like to know if a customer is worth retaining. Thus, the objectives in this project are as follows:
- Predicting customers who are likely to churn
- Determining customer value
- Creating a suitable retention program

# DATA OVERVIEW

From the given description of this data set, some information are already known about the columns in our data set as such:

- Churn indicates the customers who left within the last month, which is our target variable
- Services that customers have signed up for, which are phone service, multiple lines, internet, online security, online backup, device protection, tech support, TV streaming, and movie streaming
- Customer account information, which are tenure, contract type, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers, which are gender, if they are a senior citizen, and if they have partners and dependents

# EXPLORATORY DATA ANALYSIS

This section consists of quick visualizations to conduct univariate analysis and bivariate analysis, to view the distributions and outliers of each of the features and to see if any anomalies exist in our data. The features are grouped into two categories based on their data types, namely numerical and categorical, as they require different types of analysis.

# FEATURE EXTRACTION

After understanding all the features in the data set and the objective in this project, we can create new features in attempt to help achieve the goal of the project. The extracted features are as such:
- tenureYear = tenure * 12 months
- AnnualCharges = MonthlyCharges * 12 months
- residual = AnnualCharges - ( a * tenureYear + b )

# DATA TRANSFORMATION

To prevent data leak, data is first split into training data and testing data. Any data transformation done to the training set will then also be done on the testing set accordingly. The transformations done on the data are as listed below:
- Feature Scaling using RobustScaler
- Label Encoding using LabelEncoder
- One Hot Encoding using OneHotEncoder
- Class Balancing using SMOTE (sampling_strategy = 0.5)

The same scaling, label encoding, and one hot encoding are done on the testing set as well.

# FEATURE SELECTION

The data is transformed and ready to be processed for machine learning. However, issues such as dimensionality and multicollinearity can still hinder us from getting the best performing machine learning model. As such, this section attempts to solve such issues. Important features are selected using Boruta, categorical features are ranked using Chi-squared, and multicollinearity is solved using Pearson correlation matrix. To list them, the techniques done in this section are as follows:
- Boruta (Feature Importance)
- Chi-Squared
- Pearson Correlation Matrix

# MACHINE LEARNING MODEL

To find the best model, a list of estimators will be fitted on our training data and evaluated on the testing data as an initial step to quickly find the potentially top-performing models. The metrics we look at are the Recall scores since we want to minimize False Negatives, the customers who are actually churning but are not predicted correctly, and also the ROC AUC scores to evaluate the model's performance on imbalanced data. Below is a set of steps done in this section to find the best performing models:
- Selecting best 5 models using lazypredict.LazyClassifier
- Testing robustness of models using Cross Validation based on Recall and ROC AUC score
- Evaluating prediction on the testing set

# HYPERPARAMETER TUNING

Having tested the models on the training data, the testing data, and also evaluated them using cross validation, we see which of the models actually perform well overall. To further improve these models, hyperparamater tuning is done. The models selected and their scores after hyperparameter tuning are as such:
- Nearest Centroid (88% Recall, 0.734 ROC AUC)
- Gaussian Naive Bayes (85% Recall, 0.746 ROC AUC)
- Quadratic Discriminant Analysis (84% Recall, 0.749 ROC AUC)

All of these models should perform just as well as they were have been validated and are proven to be computationally efficient, but we picked Nearest Centroid since it has the best Recall score out of all and that their ROC AUC scores are close.

# BUSINESS SOLUTION

Using the selected machine learning model, we are able to predict when customers are churning. As previously stated in the introduction, the company wants to make sure that the customer is worth retaining. The proposed method of determing the customer value is calculating the vertical distance between the customer's data point and the regression line of annual charges on tenure in years, otherwise known as the residual values. The residual value determines the maximum amount of discount that can still be provided for a customer to end up profitable. A positive value indicates that there is room to give a profitable discount, while a negative value indicates this means that the customer is in the red and is low in terms of customer value.

 ![residual](https://raw.githubusercontent.com/fnurrahmadi/data-science-portfolio/main/Telco%20Customer%20Churn/img/residual.jpg)

The graph above shows two customer's data points:
- Green Dot: a customer whose residual is positive
- Red X-mark: a customer whose residual is negative

The green dot still has a maximum discount of ~500 that can still be given. The company can provide an amount in below that number and still profit from the customer. Meanwhile, the red X-mark is negative. If the company were to give the customer any discount, it would only lower the customer's value even more in the coming tenures.

# CONCLUSION

After completing all the preliminary tasks, a machine learning model was successfully designed to clear our first objective which was to predict customers who are churning. Using several feature selection techniques, the resulting features that are used in our model are: `tenureYear`, `residual`, `Contract_Two year`, and `PaymentMethod_Electronic check`. Based on their Recall and ROC AUC scores, there were 3 hyperparameter-tuned machine learning models that performed best using the selected features; from the best to worst, they are: `Nearest Centroid`, `Gaussian Naive Bayes`, and `Quadratic Discriminant Analysis`.

To clear our second and third objective, a suitable customer retention program was designed. To determine a customer's value, the distance between the customer's data point and the regression line of annual charges on tenure in years is calculated, denoted as `residual`. A positive value indicates the maximum amount of discount that can be given for the customer, while a negative value indicates a low customer value.

# FUTURE WORKS

When aggregated, we see that the average of the residual values of all customers is practically at 0, while the average of the residual values of loyal customers are at -60. Giving customer discounts would mean that the average of the residual values would go even lower after the discount. A solution for this would be to run a cluster analysis to discover which customers are likely to upgrade their subscription. Upgrading customers' subscriptions would mean more income for the company and thus in turn allows more room to for customer retention.
