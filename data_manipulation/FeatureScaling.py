import pandas as pd
import numpy as np
from sklearn import preprocessing as pr
import matplotlib.pyplot as plt
import seaborn as sns
veri=pd.read_excel("C:\\Users\edisa\Desktop\scaling.xlsx")
print(veri)
#max min ölçeklendirme
maxmindonus=pr.MinMaxScaler().fit_transform(veri)
#bu fonksiyon aynı zamanda değerlei küçükten büyüğe doğru sıralar.
#fonksiyon en büyük sayıyı 1 en küçük sayıyı 0 olarak tanımlar
# ve diğer değerlere de bu aralıkta tanımlama yapar
print(maxmindonus)
veri2=pd.DataFrame(maxmindonus)
print(veri2)
#ROBUST ÖLÇEKLENDİRME YAPISI(MAX MİN DEN DAHA GÜCLÜ AYKIRI DEĞERLERE KARŞI)
robust=pr.RobustScaler().fit_transform(veri)
#bu fonksiyon herhangi bir sıralama işlemi yapmaz
print(robust)
veri2=pd.DataFrame(robust)
print(veri2)
#STANDART ÖLÇEKLENDİRME
standards=pr.StandardScaler().fit_transform(veri)
#standartlaştırma işlemi yapar
veri2=pd.DataFrame(standards)
print(veri2)
sns.kdeplot(veri2)
plt.show()

