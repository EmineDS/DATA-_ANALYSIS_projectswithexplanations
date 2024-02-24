import pandas as pd
import numpy as np
from sklearn import preprocessing as pr
veri=pd.read_excel(".\onehotencoding.xlsx")
print(veri)
pd.set_option('display.max_rows', None)  # Tüm satırları göster
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
#burada eğitim kategorik değişkeni hiyerarşik bir yapı olmasına rağmen
# diğer kategorik değişkneler cinsiyet ve araç rengi hiyerarşik gruplanmamıştır.
veri["cinsiyetkod"]=pr.LabelEncoder().fit_transform(veri.Cinsiyet)
veri["AraçRenkkod"]=pr.LabelEncoder().fit_transform(veri.AraçRenk)
veri["Eğitimkod"]=pr.LabelEncoder().fit_transform(veri.Eğitim)
#hepsinin tek seferde kodlanabileceği fonksiyonlar da varmış. araştırılabilir.
print(veri.sort_values(by=["Eğitimkod"]))#eğitim koduna göre sıraladık
#diğer kategorik değişkenlerin hiyerarşik olmadığını bilgisayara söylemeliyiz
onehotdonusum=pd.get_dummies(veri,columns=["Cinsiyet","AraçRenk"], dtype=int)
print(onehotdonusum)
#aralarında hiyerarşi tanımlamaması için kategorik değişkenleri parçaladı ve o şekilde numaralandırdı. ve değişkenin kedisini sildi.
#*************************** KUKLA DEĞİŞKEN TUZAĞI *******************************************************
onehotdonusum=pd.get_dummies(veri,columns=["Cinsiyet"], dtype=int,drop_first=True)
print(onehotdonusum)
onehotdonusum=pd.get_dummies(veri,columns=["AraçRenk"], dtype=int,drop_first=True)
print(onehotdonusum)
#Kukla dönüşüm tuzağına düşmemek için kategorik değişkenlerin gruplarına tabma yaparken bir tanesini siler
#iki grupsa örneğin erkek ve kadın gibi sadece bir tanesini gösterir
#m tane grupsa m-1 tanesini gösterecektir.
#drop_first parametresiyle çalışıyor