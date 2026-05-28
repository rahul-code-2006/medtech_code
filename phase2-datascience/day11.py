import pandas as pd

df = pd.read_csv("heart.csv")



# Calculate baseline statistics for Cholesterol
chol_mean = df['chol'].mean()
chol_std = df['chol'].std()

# Apply Standardization
df['cholesterol_scaled'] = (df['chol'] - chol_mean) / chol_std
print(df[['chol', 'cholesterol_scaled']])



# Apply One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['cp'])
print(df_encoded)