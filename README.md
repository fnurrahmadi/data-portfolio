# Data Science Portfolio

My name is Fakhri Nurrahmadi. I am an aspiring Data Scientist. I am currently re-learning topics involving relational databases, statistical analysis tools, data visualizations, machine learning modelling from various sources online and offline. You can find me on:
- [LinkedIn](https://www.linkedin.com/in/fnurrahmadi/)
- [Kaggle](https://www.kaggle.com/hidious)
- [GitHub](https://github.com/fnurrahmadi)
- Or directly email me at fnurrahmadi@gmail.com

This repository is created to store the projects I have completed in hopes of building a solid Data Science portfolio. Each folder in this repository contains a separate project. I am thrilled to continue stacking more projects here as I am driven by my will to learn and improve my skills 😊

# [Projects](https://github.com/fnurrahmadi/data-science-portfolio)

## [Project 1: Telco Customer Churn - Classification](https://github.com/fnurrahmadi/FN-Repo/tree/main/Telco%20Customer%20Churn)
- Predicting customer churn using a classification model and developing a retention program
- Handling missing data and fixing data types of categorical and numerical features
- Exploring data and making analysis based on the features with respect to churn
- Encoding categorical data, scaling numerical data, and treating data imbalance
- Selecting features mainly based on the rankings generated by Boruta
- Tuning parameters of Random Forest Classifier to improve prediction
- Measuring the distance of a customer's data point (tenure and charge per year) to find the maximum discount amount to be given

![line of best fit with data points](https://raw.githubusercontent.com/fnurrahmadi/data-science-portfolio/edd9f521ac68ccb43fa36fc4ac00994bf0cdc4f3/Telco%20Customer%20Churn/img/output_159_1.png)

In the graph above, a line of best fit is plotted based on the overall tenure in years and charges per year. To find the maximum amount that can be given to a customer, we can find the distance between the charges per year of the customer and the charges on the line of best fit at a particular tenure. A positive distance indicates that the maximum amount of discount we can give them. Meanwhile, a negative distance indicates that the customer is not profitable for retention and their value is less than the overall customers.

## [Project 2: House Prices Prediction - Kaggle Competition - Regression](https://github.com/fnurrahmadi/data-science-portfolio/tree/main/House%20Prices%20Prediction)
- Predicting house prices using a regression model
- Performed Exploratory Data Analysis (EDA) to find trends and devise a plan for treating anomalies
- Engineered features based on EDA performed and selected important features for the model
- Tuning regression model with Random Search to efficiently get the best model parameters
- Submitted predictions to be scored and achieved an RMSE score of 0.26592