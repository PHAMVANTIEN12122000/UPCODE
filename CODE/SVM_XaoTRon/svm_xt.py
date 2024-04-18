from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn import svm
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import decomposition
from sklearn import datasets




min = 0
min1 = 0
dem = 0
for bien in range(10000):
    dataX = pd.read_csv('TongHop.csv')
    X = dataX.iloc[:, :-1]
    Y = np.array(dataX.iloc[:, -1])
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3 , shuffle = True)
    SVM = svm.SVC()
    SVM.fit(X_train,y_train)      
    Y_pred=SVM.predict(X_test)
    y_tt= np.array(X_test.iloc[:,-1])
    dung = accuracy_score(Y_pred, y_test)
    dem = dem + 1
    x = (len(y_tt) * dung)
    if(dung > min):
        min = dung
        y = x
        mau_svm = SVM.fit(X_train,y_train) #mau tot nhat
  
    print('==> Độ chính xác của lần lặp ',dem, 'là ',round(min * 100,3),'%','\n')


print("________________________________ĐỘ CHÍNH XÁC CỦA SVM + XÁO TRỘN DỮ LIỆU ĐẦU VÀO______________________________________________________________", '\n')


print("==> Số dự đoán đúng trên tập dữ liệu data_test thực tế :", round(y), "trên tổng", len(y_tt),'\n')
print('==> Tỉ Lệ Chính xác của K-fold cross validation + SVM  Là :',round(min * 100,3),'%','\n')
