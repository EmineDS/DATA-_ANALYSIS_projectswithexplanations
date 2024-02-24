#kategorik değişkenlerin algoritmalar tarafından
#işleme alınabilmesi için sayısal bir karşılığı olmalıdır
import pandas as pd
import numpy as np
from sklearn import preprocessing as pr
import seaborn as sns
import matplotlib.pyplot as plt
veri=sns.load_dataset("titanic")
pd.set_option('display.max_rows', None)  # Tüm satırları göster
pd.set_option('display.max_columns', None)  # Tüm sütunları göster
print(veri)
#cinsiyeti kodlayalım
#genelde iki gruplu kategorik değişken bir ve sıfırlarla kodlanır.
label=pr.LabelEncoder().fit_transform(veri["sex"])
print(label)
veri["sexcode"]=label
print(veri)
print(veri[["sex","sexcode"]])
veri2=sns.load_dataset("tips")
print(veri2)
veri2["daycode"]=pr.LabelEncoder().fit_transform(veri2["day"])
print(veri2)
#burada da kategorik değişken içerisindeki grup sayısının
#bir öneminin olmadığını gördük üç gruplu day kategorik değişkenine 1 den başlayarak sayı atar.