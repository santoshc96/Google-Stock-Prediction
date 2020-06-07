# -*- coding: utf-8 -*-
"""Google Stock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fgh1E2rcNbS-X6nBVelgTX2ETeCr1ks6
"""

#Import libraries
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
from google.colab import files
uploaded=files.upload()
df=pd.read_csv('/content/GOOG_1month.csv')
df.head(5)

#Create the list x and y dataset
dates=[]
prices=[]

#Get the number of rows and column in dataset
df.shape

#Get the last data of the row
df.tail(1)

#Get the last data of the row
df=df.head(len(df)-1)
df

#the new shape
df.shape

#Get all off the row from Data column
df_dates=df.loc[:,'Date']

#Get all of the row from Open column
df_open=df.loc[:,'Open']

#Create an independent dataset X
for date in df_dates:
  dates.append([int(date.split('-')[0])])

print(dates)
#Create an dependent data set Y
for open_price in df_open:
  prices.append(float(open_price))

#see the dates
print(dates)

def predict_prices(dates, prices, x):

  #Create a 3 support vector regression
  svr_lin=SVR(kernel='linear', C=1e3)
  svr_poly=SVR(kernel='poly', C=1e3, degree=2)
  svr_rbf=SVR(kernel='rbf', C=1e3, gamma=0.1)

  #Train SVR Model
  svr_lin.fit(dates,prices)
  svr_poly.fit(dates,prices)
  svr_rbf.fit(dates,prices)

  #Create a liear regresion model
  lin_reg=LinearRegression()
  #Train the model
  lin_reg.fit(dates,prices)

  #Plot the model and best fit
  plt.figure(figsize=(16,8))
  plt.scatter(dates,prices, color='black', label='Data')
  plt.scatter(dates,svr_rbf.predict(dates), color='red', label='SVR RBF')
  plt.scatter(dates,svr_poly.predict(dates), color='blue', label='SVR POLY')
  plt.scatter(dates,svr_lin.predict(dates), color='green', label='SVR LINEAR')
  plt.scatter(dates,lin_reg.predict(dates), color='orange', label='LINEAR REG')
  plt.xlabel('Days',fontsize=18)
  plt.ylabel('Prices',fontsize=18)
  plt.title('Regression')
  plt.legend()
  plt.show()

  return svr_rbf.predict(x)[0], svr_lin.predict(x)[0],svr_poly.predict(x)[0],lin_reg.predict(x)[0]

#predict price on day 27
predict_prices=predict_prices(dates,prices,[[27]]) 
print(predict_prices)



