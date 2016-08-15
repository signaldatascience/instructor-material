Linear regression
=================

* What does "least squares" refer to in the phrase "ordinary least squares regression"?
* What does it mean for the coefficient of a feature to be equal to *k* in a linear regression model?

Assumptions
-----------

* What is one assumption made by ordinary least squares regression?
* What assumption is made by ordinary least squares regression about the predictor variables?
* What assumption is made by ordinary least squares regression about the mean of the error terms?
* What assumption is made by ordinary least squares regression about the variance of the error terms?
* What assumption is made by ordinary least squares regression about the correlations between the error terms?
* What assumption is made by ordinary least squares regression about the correlations between the error terms and the predictor variables?
* What assumption is sometimes made by ordinary least squares regression about the distribution of the error terms?

Residuals
---------

* What is a residual?
* After fitting a linear regression model, how can its residuals be calculated?
* How would you plot the residuals of a linear regression?
* What is one example of information you can get from plotting the residuals of a linear regression?

Cost functions
--------------

* What is a cost function?
* What is one/another example of a cost function? (Repeat 2x.)
* What is the minimum value of these cost functions?
* What is the maximum value of these cost functions?
* What cost function is used for ordinary least squares regression?
* Will you get equivalent results using the RMSE and MSE cost functions?
* How could you modify the cost function to combat overfitting?

Sources of concern
------------------

* You run a linear regression and the target variable is perfectly predicted. What is one possible explanation?
* You run a linear regression and some of the coefficients are absurdly high. What is one possible explanation?
* You run a linear regression and one of the features which you know is strongly causally related to the target variable has a low coefficient. What is one possible explanation?

Regularization
--------------

* What is the L^1 norm of a vector?
* What is the L^2 norm of a vector?
* What is the L^p norm of a vector?
* What is L^1 regularization?
* What is L^2 regularization?
* What is one advantage of using a regularized linear model?
* What is one disadvantage of using a regularized linear model?
* What is one difference in the outcomes obtained by using L^1 or L^2 regularization?
* How can L^1 and L^2 regularization be combined?
* What is one interpretation of regularization in terms of Bayesian modeling?

Resampling
==========

Cross-validation
----------------

* What is *n*-fold cross-validation?
* What is the purpose of *n*-fold cross-validation?
* What values can *n* take on in *n*-fold cross-validation?
* What is an advantage of using a higher value of *n* in *n*-fold cross-validation?
* What is a disadvantage of using a higher value of *n* in *n*-fold cross-validation?

Bootstrapping
-------------

* What is a bootstrapped sample?
* What is the size of a bootstrapped sample?
* Approximately what proportion of the original dataset shows up in a bootstrapped sample?
* How can bootstrapping be used to estimate the generalizable error?
* How can bootstrapping be used to estimate parameters of probability distributions?

Overfitting
-----------

* What is one disadvantage of having more columns than rows in your dataset?
* What is one concrete example of overfitting?
* What is one/another way to deal with overfitting? (Repeat question 2-3x.)