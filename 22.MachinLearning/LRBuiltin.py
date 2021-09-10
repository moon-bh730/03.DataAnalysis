#import lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/slr12.csv')
x = df['AnnualFranchiseFee'].values
y = df['StartUpCost'].values

reg = LinearRegression()
reg.fit(x[:30].reshape(-1,1), y[:30])
prediction = reg.predict(x[30:].reshape(-1, 1))
mse = mean_squared_error(prediction, y[30:])

print('The MSE score of the model is : ', mse)

prediction = reg.predict(np.array([i for i in range(650, 1400)]).reshape(-1, 1))

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