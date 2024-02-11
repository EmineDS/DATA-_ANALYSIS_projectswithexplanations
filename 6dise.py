import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import date
d1 = {'d1':list(range(1,7))}
df1 = pd.DataFrame(data=d1)

df1['key'] = 1

d2 = {'d2':list(range(1,7))}

df2 = pd.DataFrame(data=d2)

df2['key'] = 1

d3 = {'d3':list(range(1,7))}

df3 = pd.DataFrame(data=d3)

df3['key'] = 1

d4 = {'d4':list(range(1,7))}

df4 = pd.DataFrame(data=d4)

df4['key'] = 1

d5 = {'d5':list(range(1,7))}

df5 = pd.DataFrame(data=d5)

df5['key'] = 1

d6 = {'d6':list(range(1,7))}

df6 = pd.DataFrame(data=d6)

df6['key'] = 1
# To create a table with all combination of rolls, the individual tables are joined similar
# to a SQL cross join.
df_rolls = pd.merge(df1, df2, on ='key')
df_rolls = pd.merge(df_rolls, df3, on ='key')
df_rolls = pd.merge(df_rolls, df4, on ='key')
df_rolls = pd.merge(df_rolls, df5, on ='key')
df_rolls = pd.merge(df_rolls, df6, on ='key')
df_rolls.drop("key", axis=1, inplace=True)
print(df_rolls)
# A column used to sum each of the 6 dice
df_rolls['roll_sum'] = df_rolls['d1'] + df_rolls['d2'] + df_rolls['d3'] + df_rolls['d4'] + df_rolls['d5'] + df_rolls['d6']
print(df_rolls)
df_rolls['winner'] = df_rolls[['roll_sum']].apply(lambda x: 'W' if (x['roll_sum'] == 6) | (x['roll_sum'] == 36)\
                                else 'L', axis=1)
print(df_rolls)
# Create a table that groups by the W/L column created
# Because we have labeled each row as either W or L, we can now use value_counts()
# to count the winners and also get a % of winners out of all possible combinations.
w1 = pd.DataFrame(df_rolls.winner.value_counts().reset_index())
w1.rename(columns={'index':'win_or_lose', 'winner':'possible_outcomes'}, inplace=True)

w2 = pd.DataFrame(df_rolls.winner.value_counts(normalize=True).reset_index(drop=True))
w2.rename(columns={'index':'win_or_lose', 'winner':'possible_outcomes_pct'}, inplace=True)

# 'win_or_lose' sütunu ile birleştirme işlemi
w1 = w1.merge(w2, how='left', left_index=True, right_index=True)
w1 = w1.rename(columns={'possible_outcomes': 'win_or_lose'})
print(w1)
# A dataframe that shows the probabability for each possible sum
print(df_rolls)
a=pd.DataFrame(df_rolls.roll_sum.value_counts(normalize=True).reset_index()).sort_values("roll_sum")
print(a)
# Visualizing the distribution of possible sums
print(df_rolls.roll_sum)
sns.histplot(df_rolls.roll_sum, bins=31)
plt.show()
#6 zarın toplamın 2 ve 3 e bölünen bir sayı olma olasılığı nedir?
# A lambda function used to identify the rows where the sum is even
df_rolls['winner_even'] = df_rolls[['roll_sum']].apply(lambda x: 'W' if (x['roll_sum'] % 2 == 0) & (x['roll_sum'] % 3 == 0) else 'L', axis=1)
# Create a table that groups by the W/L column created
w_count = df_rolls[df_rolls['winner_even'] == 'W'].shape[0]
l_count = df_rolls[df_rolls['winner_even'] == 'L'].shape[0]
p=w_count/(w_count+l_count)
dagilim=stats.bernoulli(p)
gelolasilik=dagilim.pmf(k=1)
print(gelolasilik*100)
sns.histplot(df_rolls['winner_even'], bins=31)
plt.show()