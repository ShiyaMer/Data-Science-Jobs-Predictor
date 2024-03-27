"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_excel('cleaneddataset.xlsx')
df.drop(columns=['Unnamed: 0','Job Title','Company Name','Headquarters','Revenue','Competitors','Industry'],inplace=True)
df_dum=pd.get_dummies(df)
df_dum = df_dum.dropna(axis=0)
X=df_dum.drop('avg_salary',axis=1)
y=df_dum.avg_salary.values
from sklearn.model_selection import train_test_split 
X_train, X_test,y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2,shuffle=True)
print(list(X_test.iloc[1,:]))"""
dat_in=[4.3, 51.0, 2008, 0, 0, 77500.0, 100000.0, 1, 16, 0, 0, 0, 0, 1, 0, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]