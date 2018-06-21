import csv
import pandas as pd
import tensorflow as tf

file = './2017_reduced.csv'
COLUMN_NAME = ['brithday', 'department',
               'adminssion-date', 'leave-date', 'details', 'results']
train_data = pd.read_csv(file, names=COLUMN_NAME, header=0, encoding='GB2312')

# train_x, train_y = train_data, train_data.pop('y_name')


# SPECIES = [1, 2, 3, 4, 5]

brithday = train_data['brithday']

# print(train_data)
print(brithday[0:3])

results = train_data['results'].unique()
print(results)

# x = train_data['results'][0:2]