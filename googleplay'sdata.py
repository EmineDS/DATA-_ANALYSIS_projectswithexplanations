import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#gogle play store verileri üzerinden veri ayıklama ve görselleştirme yaptım
df=pd.read_csv("C:\\Users\edisa\Desktop\googleplaystore.csv")
pd.set_option('display.max_columns', None)
print(df.head())
print(df.columns)
df.columns=df.columns.str.replace(" ","_")#column isimlerindeki boşlukları _ ile değiştirdik
print(df.columns)
print(df.shape)#datanın büyüklüğünü(satır sütün )şeklinde görüyoruz
print(df.dtypes)#veri türlerini görüyoruz
print(df.isnull().sum())#eksik verilerini görüyoruz
#eksik verileri görselleştirdik
sns.set_theme()
#sns.set(rc={"figure.dpi":300,"figure.figsize":(12,9)})#kalite ve boyut
sns.heatmap(df.isnull(),cbar=False)
plt.show()
#eksik değerler yerine medyan yazılması tercih edilir
#eksik değer olmaması gerekir. ratingde çok fazla olduğu için manipüle edilmelidir.
rating_median=df["Rating"].median()
print(rating_median)
df["Rating"].fillna(rating_median,inplace=True)#eksik yani boş verileri bu şekilde doldurduk
#fillna(doldurulucak değer,inplace= yani değiştir yerleştir ve kaydet için zorunlu)
#diğer sütunlardaki eksik veriler az olduğu için
#bu eksik verileri direkt kaldırabiliriz
df.dropna(inplace=True)#buarada data framede kalan tüm boş değerleri sildik
print(df.isnull().sum().sum())#kaç adet boş değer olduğunu sorguladık 0 olmalı
print(df.info())#sütunlar hakkında bilgileri çıkardık
#SONRAKİ AŞAMA OBŞE TİPİNDE OLAN ANCAK SAYISAL OLMASI GEREKEN DEĞERLERİ DEĞİŞTİRMEK
#reviews den başlayalım
print(df["Reviews"].describe())#betimsel istatistik değerlerini çıkardık
#değerleri integer a çevirelim
df["Reviews"]=df["Reviews"].astype("int64")#Reviews değerlerini int e çevirip tekrar reviews sütununa atadık
print(df["Reviews"].describe().round())#float değerlerini en yakın tam sayıya yuvarlaması için round kullandık
#size columuna geçtik burada baktığımızda sıyasal değerlerin yanında mve k iabreleri var
print(df["Size"].unique())#boyutun yanında m ve k ifadeleri var
df["Size"].replace("M","",regex=True,inplace=True)
df["Size"].replace("k","",regex=True,inplace=True)
print(df["Size"].unique())#içerisinde bir adet metinsel fade var bunun columnu sayıya çeviriken hata vereceğini bilmeliyiz
size_median=df[df["Size"]!="Varies with device"]["Size"].astype(float).median()#buarada sayı olan değer dışındakilerin hepsini floata veririp medianını aldık
print(size_median)
#şimdi size daki yazı ifadesini median ile değiştirelim
df["Size"].replace("Varies with device",size_median,inplace=True)
df["Size"]=pd.to_numeric(df.Size)#değerleri sayısala dönüştürmenin farklı bir yolu
print(df.Size.describe())
#şimdi install sütununa bakalım isntall sütununda değerlerin , ve + ifadeleri içeerdiğini görebiliriz
print(df["Installs"].unique())
#bu defa farklı bir yol olarak lambda ile nasıl yapılacağına bakalım
df.Installs=df.Installs.apply(lambda x:x.replace("+",""))
df.Installs=df.Installs.apply(lambda x:x.replace(",",""))
df.Installs=df.Installs.apply(lambda x:int(x))
print(df["Installs"].unique())
#Price sütununa bakalım
print(df.Price.unique())
df.Price=df.Price.apply(lambda x:x.replace("$",""))
df.Price=df.Price.apply(lambda x:float(x))
print(df.Price.unique())
#Genres sütununa bakalım
print(df.Genres.head(10))
# buarada baktığımızda ifadeler noktalı virgülle ayrılmış ve ilk ifade türü ikinci ifade alt kategoriyi gösteriyor
df.Genres=df.Genres.str.split(";").str[0]#değerleri noktalı virgülden ayırıp ilk değeri seçtik
print(df.Genres.unique())
print(df.Genres.value_counts())
# music kategıorisinden 25 music and audio kategorisinden 1 olduğu için az olan kategoriyi de music yapıp birleştirelim
df.Genres.replace("Music & Audio","Music",inplace=True)
print(df.Genres.value_counts())
#Last_Updated columuna bakalım
print(df.Last_Updated.head())#buarada tarihler var
#ancak görebileceğiniz gibi tarihler obje tipinde
#pandasta date time yapısı olduğu için k-bunu date time a dönüştürelim
df["Last_Updated"]=pd.to_datetime(df.Last_Updated)
print(df.dtypes)
#veri ayıklama ve temizleme işlemi bitti şimdi veri görselleştirelim
#sns.barplot(df["Type"].value_counts(),color="red")#burada type columundaki değerlerin(ücretli ücretsiz) sayısına göre
#bir bar grafiği oluşturduk
#sns.boxplot(x="Type",y="Rating",data=df)
#sns.countplot(y="Content_Rating",data=df)#burada uygulamaların yaşlara göre sayı grafiğini yaptık
#sns.countplot(y="Genres",data=df)#burada da türleri sayısına göre yazdık
sns.boxplot(x="Content_Rating",y="Rating",data=df)
plt.show()
