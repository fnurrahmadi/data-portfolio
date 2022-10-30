# User and Revenue AB Testing

In this project, a change was made to the landing page of the company's website to see if it would positively affect the conversion rate of users. This project showcases the frequentist method to determine the outcome of the hypothesis testing. In this particular dataset, the convert column for each user is ready to be used right away. There are only two separate groups of variants:
- Control Group -- the existing website
- Treatment Group -- the website with the change

# Hypothesis

The metric used for the test is the conversion rate of users. As such, the statistical hypothesis is designed as below:
- H0: the conversion rate of the control group is equal to the conversion rate of the treatment group.
- H1: the conversion rate of the control group does not equal to the conversion rate of the treatment group.

# Power Analysis

## Power of the Test

The power of the statistical test (1 - beta) is the probability of correctly rejecting the null hypothesis.
The power set in this test is 80%, which means that there is a 20% chance for Type II error to happening.

## Significance Level of the Test

The significance level of the test (alpha) sets the probability of Type I error, which is the likelihood of rejecting the null. In this test, the significance level is set to 5%, which also means that confidence level is 95%.

## Minimum Detectable Effect

The minimum detectable effect of the test (delta) is an estimate set to determine how much better should the metric be than the previous version in order to be able to approve the new version, which is usually set by stakeholders.

# Sample Size

In this A/B test, two proportions (conversion rates) are being compared. We will use the power analysis to compute the minimum sample size needed and see the if the sample we already have in the dataset is enough.

# Duration of the Test

It is important to set the duration before running the test and not during to remove bias. A good baseline of duration time is  to divide the sample size by the number of visitors per day.

# Running the A/B Test

Since the sample size is larger than 30 samples and the metric follows asymptotic Normal Distribution, the 2-sample Z-test (parametric) is used to compare the conversion rates of the control and the variant group.

# Analyzing the Test

Unfortunately, the p-value is not less than or equal to the significance level meaning that the null hypothesis cannot be rejected, and alternate hypothesis cannot be accepted. The new landing page does not positively affect the conversion rate compared to the old landing page. Therefore, we cannot make the recommendation to switch to the new landing page.