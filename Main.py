import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns

dv= pd.read_csv("/content/topSubscribed.csv")

dv

dv.info()

dv.head()

dv["Rank"].unique()

dv.head()

import  seaborn as sns

plt.figure(figsize=(5,5),dpi =100)
sns.scatterplot(data=dv,x='Rank',y='Subscribers',hue='Youtube Channel')
plt.show()


import plotly.express as px
from datetime import date
import datetime as dt

fig=px.scatter(dv,x="Rank",y="Subscribers",color="Video Views")
fig.show()

fig=px.scatter(dv,x="Rank",y="Subscribers",color="Youtube Channel",animation_frame="Started")
fig.show()
