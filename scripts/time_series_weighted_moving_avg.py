import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


from sklearn.metrics import mean_squared_error
from math import sqrt
from statistics import mean 

import warnings
warnings.filterwarnings("ignore")


train_data = pd.read_csv("/Users/paramanandbhat/Downloads/4.3_and_4.4_-_MA_and_WMA/data/train_data.csv")
valid_data = pd.read_csv("/Users/paramanandbhat/Downloads/4.3_and_4.4_-_MA_and_WMA/data/valid_data.csv")

#required preprocessing
train_data.timestamp = pd.to_datetime(train_data['Date'],format='%Y-%m-%d')
train_data.index = train_data.timestamp

print(train_data.shape)
print(train_data.head())

print(valid_data.shape)
print(valid_data.head())

valid_data.timestamp = pd.to_datetime(valid_data['Date'],format='%Y-%m-%d')
valid_data.index = valid_data.timestamp

# list holding last seven values and weights

week_values = train_data['count'][571:578].values
week_values = week_values.tolist()

weights = []
for i in range(1,8):
    W = i/13
    weights.append(W)
len(week_values), len(weights)

valid_data['weighted_moving_average'] = 0

for i in range(0,len(valid_data)):
    
    end = len(week_values)
    start = len(week_values)-7
    
    final_values = week_values[start:end]
    
    weighted_mean = 0
    for j, k in zip(weights,final_values):
        weighted_mean += j*k
        
    weighted_mean = weighted_mean/sum(weights)
        
    valid_data['weighted_moving_average'][i] = weighted_mean
    week_values.append(weighted_mean)

plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index,valid_data['count'], label='valid')
plt.plot(valid_data.index,valid_data['weighted_moving_average'], label='Weighted Moving Average Forecast')
plt.legend(loc='best')
plt.title("Weighted Moving Average Method")
plt.show()

# calculating RMSE 
rmse = sqrt(mean_squared_error(valid_data['count'], valid_data['weighted_moving_average']))
print('The RMSE value for Weighted Moving Approach is', rmse)