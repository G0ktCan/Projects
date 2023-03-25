import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import os

os.chdir('Calisma_Dizniniz')

dataset = pd.read_csv('dosya.csv')

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size = 1/3, random_state = 0)

reg = LinearRegression()
reg.fit(Xtrain,ytrain)

ypred = reg.predct(Xtest)

plt.scatter(Xtrain, ytrain, color = 'red')
plt.title('Kıdeme Göre Maaş Tahmini Regresyon Modeli')
plt.xlabel('Kıdem')
plt.ylabel('Maaş')
plt.show()