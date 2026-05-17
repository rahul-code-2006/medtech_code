import pandas as pd

df = pd.read_csv('heart.csv')

group = df.groupby(['target','cp']).size()

print(group[group.index == (0, 3)])