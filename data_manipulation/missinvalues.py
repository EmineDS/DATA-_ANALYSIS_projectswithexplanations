import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_excel("C:\\Users\edisa\Desktop\missingvalues.xlsx")

print(data.info())
print(data.isnull())
print(data.isnull().sum())
print(data[data.isnull().any(axis=1)])#hangi satırlarda en az bir null değeri varsa o satırı yazdırır
#msno.matrix(data)
#plt.show()
data2=sns.load_dataset("titanic")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(data2)
#************************BOŞ DEĞERLERİ SİLME
print(data2.isnull().sum())
#msno.heatmap(data2)
#plt.show()
print(data)
datacopy=data.copy()#data setini kopyaladık
#datacopy[~datacopy.isnull()]=1#boş olmayan değerlere 1 atadık
#datacopy[datacopy.isnull()]=0#boş olan değerlere 1 atadık
print(datacopy)

datacopy2=datacopy.notnull().astype("int")#dolu olan değerlere 1 boş olan değerlere 0 döndürdü
print(datacopy2)

print(datacopy2.corr())# % 80 üzerindeki durumda korelasyon kabull edilir.
#yani%80 üzerinde çıksaydı eksik veriler rassal olmayacaktı ancak %80 üzerinde çıkmadığı
#için eksik veriler rastgeledir diyebiliriz.
print(datacopy.isnull().sum())
#boş verileri silebiliriz
datacopy.dropna(how="all",inplace=True)#,eğer bir satırda tüm değişkenler nan ise siler how parametresi bize bunu söyler
#bu satır bazlı çalışır
#sütun silmek içi axis=1, parameresini kullanılır.
datacopy.reset_index(drop=True,inplace=True)
print(datacopy)
#****************************BOŞ DEĞERLERİ DEĞİŞTİRME
datacopy2=data.copy()
#datacopy2.D1.fillna(value=datacopy2.D1.mean(),inplace=True)
datacopy2.fillna(value=datacopy2.median()[:],inplace=True)#özellikle belirli kolumnlar arasında işlem yapmak için ["D1":"D2"]
print(datacopy2)
