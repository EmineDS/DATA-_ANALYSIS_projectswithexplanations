import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_csv("C:\\Users\edisa\Desktop\earthquake_final (1).csv")
print(df.info())
df.datetime=pd.to_datetime(df.datetime)
turkey = df[df["country"] == "mediterranean"]
print(turkey)
print(len(turkey[turkey["richter"] >= 5.0]))
p=len(turkey[turkey["richter"] >= 5.0])/len(turkey)
n=len(turkey[turkey["richter"] >= 5.0])#orneklem sayısı
print(p)#orneklem değerimizz 20 den büyük p değerimiz 0.5 ten küçük
#n değerimiz 20’den büyük ve p değerimiz 0.05’ten küçük olduğu için
ortalama=p*n
print(ortalama)
turkeyd=df[df["country"] == "mediterranean"]
print(turkeyd["datetime"].max())
years=(turkeyd["datetime"].max()-turkeyd["datetime"].min())/365
print(years)
#bir yılda ortalama 3 büyük deprem olma olasılığı
biryil=ortalama/106
print(biryil)
dagilim=stats.poisson(biryil)
p=dagilim.pmf(k=1)
print(p*100)