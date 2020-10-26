import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

df_tips.head()

df_tips.info()

df_tips['tip'].plot(kind='hist')