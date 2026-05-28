import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Reading and cleaning the database

df = pd.read_csv('heart.csv')

print("     --- Data Shape ---     ")
print(f"Rows: {df.shape[0]}     Columns: {df.shape[1]}")

#Missing values and datatypes
print("     --- Missing values and Data types ---   ")
print(df.info())


#Data-summary
summary = df.groupby('target')[['age','thalach','trestbps','chol']].agg(['mean','median'])

print(summary)


#Checking for duplicates and inspecting them

duplicate_count = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicate_count}")

#inspect
duplicate_rows = df[df.duplicated(keep=False)]
print("\n     ---Duplicated rows---\n")
print(duplicate_rows)

#Dropping duplicates

df_cleaned = df.drop_duplicates()

#Final shape of dataframe
print("     ---Shape after dropping---")
print(f"Rows: {df_cleaned.shape[0]}     Columns: {df_cleaned.shape[1]}")


#Visualising the dataset

plt.figure(figsize=(10, 5))
sns.set_theme(style='darkgrid')

sns.kdeplot(data=df_cleaned, x='thalach', hue='target', fill=True, common_norm=False,palette='crest',alpha=0.5)

plt.title('Max Heart Rate Achieved (thalach) Distribution by Heart Disease Status', fontsize=14, pad=15)
plt.xlabel('Max Heart Rate (bpm)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(title='Condition', labels=['Heart Disease (1)', 'Healthy (0)'])
plt.tight_layout()
plt.savefig('thalach_distribution.png')

plt.show()

#Correlational matrix
plt.figure(figsize=(12,8))
corr_df = df_cleaned.corr()
sns.heatmap(data=corr_df,annot=True,fmt=".2f",cmap="coolwarm", vmin=-1, vmax=1, linewidths=0.5)
plt.title('Feature Correlation Matrix (UCI Heart Disease)', fontsize=14, pad=15)
plt.tight_layout()
plt.savefig('correlational_heatmap.png')
plt.show()


# Verify if Age is confounding our Maximum Heart Rate (thalach)
age_thalach_check = df_cleaned.groupby('target')[['age', 'thalach']].mean()
print("--- Confounder Audit: Age vs Max Heart Rate ---")
print(age_thalach_check)

# Let's check the correlation directly between Age and Max Heart Rate
correlation = df_cleaned['age'].corr(df_cleaned['thalach'])
print(f"\nOverall Correlation between Age and Max Heart Rate: {correlation:.2f}")