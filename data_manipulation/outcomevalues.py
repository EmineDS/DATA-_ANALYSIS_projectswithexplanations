import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#yaş=[30,33,31,33,30]
#yıl=[7,10,9,12,25]
#sns.scatterplot(x=yaş,y=yıl)
#plt.show()
veri=sns.load_dataset("taxis")
veri2=veri.copy()
print(veri.isnull().sum())
#aykırı değerler için sınır bulalım
q1=veri2.tip.quantile(0.25)#1.çeyrek
q3=veri2.tip.quantile(0.75)#ikinci çeyrek (normal dağılım grafiğine bak)
#*******formül
IQR=q3-q1
altsinir=q1-1.5*IQR
ustsinir=q3+1.5*IQR
#**************
aykırımin=veri[veri2["tip"]<altsinir].tip
aykırımax=veri[veri2["tip"]>ustsinir].tip
#hangi satırdaki değerlerin aykırı gözlem olduğunu görelim
aykırı=pd.concat([aykırımin,aykırımax],axis=0).index
print(aykırı)
#aykırı adlı değişkendeki aykırı değerlerin indexlerini data frame içinde  olduğu için kullanamıyoruz kullanmak için de listeye alalım
indexler=[]
for i in aykırı:
    indexler.append(i)
print(indexler)
#aykırı değer indexlerini silelim
veri3=veri2.drop(index=indexler).reset_index()
sns.boxplot(veri3.tip)
plt.show()
#AYKIRI DEĞERLERE ORTALAMA DEĞER ATAMAK
ortalama=veri2.tip.mean()
print(ortalama)
#veri2.loc[indexler,"tip"]=ortalama
#sns.boxplot(veri2.tip)
#plt.show()
#AYKIRI DEĞERLERİ BASKILAMAK
#alt sınırın altında kalanlara alt sınır üst sınırın üstüne kalanlara üst sınırı atadık
veri2.loc[veri2.tip<altsinir]=altsinir
veri2.loc[veri2.tip>ustsinir]=ustsinir
sns.boxplot(veri2.tip)
plt.show()