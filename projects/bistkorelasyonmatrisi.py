import pandas as pd
import yfinance as yf #yahoo finans
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
hisse=pd.read_excel(".\\bistkorelasyon.xlsx")
hissekod=hisse+"."+"IS"
print(type(hissekod))
#bir dataframe in belirli bir sütunu nasıl listeye çevrilir
hisseler=hissekod["kod"].values.tolist()
print(hisseler)
veri=yf.download(tickers=hisseler,start="2020-01-01",end="2022-05-24")
print(veri)
fiyat=veri["Adj Close"].reset_index()
getiri=veri["Adj Close"].pct_change()
print(getiri)
sp=getiri.std()
print(sp.sort_values(ascending=False))#büyükten küçüğe sıraladık
kor=getiri.corr()
plt.title("Bist30 Getiri Korelasyon Matrisi",color="red",fontsize=15)
sns.heatmap(kor,annot=True,cmap="Blues",xticklabels=True,yticklabels=True,vmin=-1,vmax=1)
plt.show()
#korelasyonu gördük ancak bunlar anlamlı mı
anlam=pg.pairwise_corr(getiri)
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)
print(anlam)
print(anlam[anlam["p-unc"]<0.05])#anlamlı olanlar
