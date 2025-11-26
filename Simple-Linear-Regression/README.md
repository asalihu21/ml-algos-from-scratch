Simple Linear Regression is a regression algorithm, meaning that it is used to predict a continuous value based on a straight line that was created when the model was trained. The idea is simple:

The straight line formula is y = mx + c.

y is your target variable, or 'answer'.
m is the gradient of your line.
x is the value of your feature.
c is the y intercept.

Our goal is to find m and c values that give us the 'line of best fit', meaning the line that passes through or close to as many of our points as possible.
I will achieve this by using a method called gradeint desecent, a recursive algoithm that runs many times, getting m and c closer and closer to their best values