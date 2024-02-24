import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import random

df=pd.read_csv("C:\\Users\edisa\Desktop\earthquake.csv")
print(df["country"].unique())
turkey = df[df["country"] == "turkey"]
veri=turkey["richter"]
print(veri.mean())
print(veri.std())
print(veri)
aralik=stats.norm.interval(confidence=0.95,loc=veri.mean(),scale=2/np.sqrt(len(veri)))
print(aralik)
sns.histplot(veri,kde=True)
plt.show()
