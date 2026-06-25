import pandas as pd
import numpy as np
df=pd.read_csv('Salary_Data.csv')
print(df.head())
l1=[1,2,3,4,4,5,6,7,8,9,10]
s=pd.Series(l1)
print(s)

w={"temp":[32,45,67,89,np.nan],"humidity":[12,34,56,78,np.nan] , "wind":[23,45,67,89,np.nan], "events":["rain","sunny","cloudy","storm",np.nan]}
df1=pd.DataFrame(w)
print(df1)


print(df1.loc[0:2,["temp","humidity"]])
print(df1.iloc[:4,:2])

df.iloc[:,-1].unique()
print(df1[df1["temp"]>25])

print(df1.isnull().sum())

##fillna()

interpolated_df=df1.interpolate()
print(interpolated_df)

df1["event"]=df1["events"].map({"rain":1,"sunny":2,"cloudy":3,"storm":4})
print(df1)