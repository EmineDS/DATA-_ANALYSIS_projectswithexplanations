import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
df=pd.read_csv("C:/Users/edisa/Downloads/file.csv")#GİTHUBA EKLEDİM
print(df.head())
print(df.dtypes)
print(df.shape)#boyut
print(df.columns)#burada column isimlerinde boşluk karakterleri olduğunu görebilirizsiniz bu işimizi
#zorlaştıracağından boşluk karakterlerini kaldıralım.
df.columns=df.columns.str.replace(" ","")
print(df.columns)
print(df.isnull().sum())#boş karakter olmadığını görüyoruz
df["Date/Time"]=pd.to_datetime(df["Date/Time"])
print(df.dtypes)
df["Weather"]=df.Weather.str.split(",").str[0]
print(df.columns)
print(df.columns)
print(df.Weather.unique())
#df.weather2.fillna(df.weather2.value_counts().idxmax(),inplace=True)
#print(df.weather2.unique())
print(df.groupby("Weather").get_group("Clear"))
print(df)
#sns.lineplot(data=df.Press_kPa,linewidth=2)
#find the number of time when the "wind speed was exactly 4km/h
print(df["WindSpeed_km/h"]==4)#böyle yazdığımızda sadece boolean değerlerini döndürüyor
print(df[df["WindSpeed_km/h"]==4])#bu şekilde dataframe değerlerini görüyoruz
print(df.notnull().sum())
df.rename(columns={"Weather":"weather_conditions"},inplace=True)
print(df.weather_conditions)
print(df.Visibility_km.mean())
print(df.Press_kPa.std())
print(df["RelHum_%"].var())
a=df[(df["WindSpeed_km/h"]>24) & (df["Visibility_km"]==25)]#shif 6 &
print(a)
print(df.groupby("weather_conditions").mean())#hava durumuna göre bölüp her hava durumundaki kolumunun ortalamasını aldık
print(df.groupby("weather_conditions").min())
print(df.groupby("weather_conditions").max())
print(df[df["weather_conditions"]=="Snow"])
print(df[(df["weather_conditions"]=="Clear")|(df["Visibility_km"]>40)])#or condinitons
sns.lineplot(x=df["Temp_C"],y=df["Press_kPa"],data=df[df["weather_conditions"]=="Snow"])
plt.show()