import pandas as pd
df=pd.DataFrame({'name':['Rahul','Anjali','Harry'],'marks':[99,95,8]})
print(df['name'])
print(df['marks'].mean())
print(df['marks'].max())
print(df[df['marks'] > 70])