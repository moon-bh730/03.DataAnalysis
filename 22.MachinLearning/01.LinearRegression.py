#import lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error

#read data
df = pd.read_csv('data/slr12.csv')
x = df['AnnualFranchiseFee'].values
y = df['StartUpCost'].values

#mean
def get_mean(arr):
    return np.sum(arr)/len(arr)

#variance
def get_variance(arr,mean):
    return np.sum((arr-mean)**2)

#convariance
def get_covariance(arr_x, mean_x, arr_y, mean_y):
    final_arr = (arr_x - mean_x) * (arr_y - mean_y)
    return np.sum(final_arr)

# find coffee
def get_coefficients(x, y):
    x_mean = get_mean(x)
    y_mean = get_mean(y)
    m = get_covariance(x, x_mean, y, y_mean)/get_variance(x, x_mean)
    c = y_mean - x_mean*m
    return m, c

# Regression Function
def liner_regression(x_train, y_train, x_test, y_test):
    prediction = []
    m, c = get_coefficients(x_train, y_train)
    for x in x_test:
        y = m*x + c
        prediction.append(y)

    mse = mean_squared_error(prediction, y_test)
    print("The MSE score of the model is : ", mse)
    return prediction

# There are 36 sample out of which 30 are for training and 6 are for testing
liner_regression(x[:30], y[:30], x[30:], y[30:])

# visualize
def plot_reg_line(x, y):
    prediction = []
    m, c = get_coefficients(x, y)
    for x0 in range(650,1400):
        yhat = m*x0 +c
        prediction.append(yhat)

    fig = plt.figure(figsize=(20, 7))
    plt.subplot(1,2,1)
    sns.scatterplot(x=x, y=y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot between X and Y')

    plt.subplot(1,2,2)
    sns.scatterplot(x=x, y=y, color= 'blue')
    sns.lineplot(x = [i for i in range(650, 1400)], y = prediction, color = 'red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Regression Plot')
    plt.show()

plot_reg_line(x, y)

