import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')

# Set a clean style
sns.set_style("whitegrid")

# Simple distribution plot
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='age', hue='target', bins=20, kde=True)
plt.title('Age Distribution by Heart Disease Status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(['No Disease', 'Disease'])
plt.tight_layout()
plt.show()