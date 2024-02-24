#elimizde on yıllık bist getirilerinin günlere göre listelenmiş hali var buna bakarak
#günlerin getiriler üzerinde anlamlı bir etkisi var mı analiz edelim.
import pandas as pd
from scipy import stats
import pingouin as pg
import scikit_posthocs as sp
veri=pd.read_excel(".\\borsanaliz.xlsx")
print(veri.head())
pzt=veri[veri["GÜN"]=="Pazartesi"]
sl=veri[veri["GÜN"]=="Salı"]
crs=veri[veri["GÜN"]=="Çarşamba"]
prs=veri[veri["GÜN"]=="Perşembe"]
cm=veri[veri["GÜN"]=="Cuma"]
verilist=[pzt["GETİRİ"],sl["GETİRİ"],crs["GETİRİ"],prs["GETİRİ"],cm["GETİRİ"]]
#öncelikle bu veriler için normallik analizi yapılmalıdır.
for i in range(0,4):
    test,p=stats.shapiro(verilist[i])
    print(f"{p:.10f}")
    i=i+1
#normallik hipotezi reddedilir ancak anova testi normallikten etkilenmez
#varyans homojenliği testi yapalım
test,p=stats.bartlett(pzt["GETİRİ"],sl["GETİRİ"],crs["GETİRİ"],prs["GETİRİ"],cm["GETİRİ"])
print(f"{p:.30f}")
#varyansları homojen değil
#anova ile ortalamalarını karşılaştıralım varyansları homojen olmadığı için
#welch'in anova testini kullandık
anova=pg.welch_anova(data=veri,dv="GETİRİ",between="GÜN")
print(anova) #p value 0.8 çıktı bu da bize anlamlı farklılıklar içermiyorsonucunu getirir
tamhane=sp.posthoc_tamhane(veri,val_col="GETİRİ",group_col="GÜN")
print(tamhane)#bu şekilde de yine anlamlı farklılıklar içermediğini görebiliriz