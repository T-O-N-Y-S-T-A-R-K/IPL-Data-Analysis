import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

import plotly.offline as py
import plotly.graph_objs as go

from yellowbrick.contrib.scatter import ScatterVisualizer
from yellowbrick.features.radviz import RadViz
from yellowbrick.features.pcoords import ParallelCoordinates
from yellowbrick.model_selection import CVScores
from yellowbrick.features.rankd import Rank2D
from yellowbrick.features.manifold import Manifold

# Avoid showing warnings
warnings.simplefilter('ignore')

# Load datasets
data1 = pd.read_csv('matches.csv')
data2 = pd.read_csv('deliveries.csv')

# Show first 5 rows of data1
print("Matches Data Preview:")
print(data1.head())

# Matplotlib (for plots)
plt.figure(figsize=(10, 5))
sns.countplot(x='winner', data=data1, order=data1['winner'].value_counts().index)
plt.title('Match Wins by Team')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()  

# Plotly (opens in browser)
bar = go.Bar(x=data1['winner'].value_counts().index,
             y=data1['winner'].value_counts().values)
layout = go.Layout(title='Match Wins by Team (Plotly)')
fig = go.Figure(data=[bar], layout=layout)
py.plot(fig, filename='ipl_wins_plot.html')  
