import pandas as pd
#Data cleaning
df = pd.read_csv('heart.csv')

# 'fbs' is Fasting Blood Sugar


#fill in the empty values
median_bs= df['fbs'].median()
df['fbs']=df['fbs'].fillna(median_bs)

median_chol= df['chol'].median()
df['chol']=df['chol'].fillna(median_chol)

#drop the negative age
df=df[df['age']>=0]


def flag_clinical_outliers(df, column):
    new_column_name = f"{column}_outlier"
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    df[new_column_name]=( ((df[column] > upper_bound) | (df[column] < lower_bound)).astype(int))
    return df


for i in df.keys():
    if i=='target'or i=='sex'or i=='cp':
        continue
    flag_clinical_outliers(df,i)
print(df.head())