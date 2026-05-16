import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('heart.csv')
def data_profile(df):
    print('='*50)
    print("         Heart disease dataset profile")
    print('='*50)
    print(f"total patients: {len(df)}")
    total = len(df)
    hd = len(df[df['target'] == 1])
    no_hd = len(df[df['target'] == 0])
    print(f"Heart disease: {hd}  ({round( hd/total*100,1)}%)")
    print(f"No heart disease: {no_hd}  ({round( no_hd/total*100,1)}%)")

    print('\n', "--- Patient demographics ---")
    print(f"Age range: {df['age'].min()} - {df['age'].max()} years")
    print(f"Mean age: {df['age'].mean():.1f} years")
    male_patients = len(df[df['sex']==1])
    female_patients = len(df[df['sex']==0])
    print(f"Male patients: {male_patients}  ({round( male_patients/total*100,1)}%)")
    print(f"Female patients: {female_patients}  ({round( female_patients/total*100,1)}%)")

    print('\n', "--- Key Clinical Markers---")
    print(f"Mean resting BP: {df['trestbps'].mean():.1f} mm Hg")
    print(f"Mean cholesterol: {df['chol'].mean():.1f} mg/dL")
    print(f"Mean max HR: {df['thalach'].mean():.1f} bpm")

    print('\n', "--- Risk Flags ---")
    high_BP = len(df[df['trestbps']>140])
    high_chol = len(df[df['chol']>240]) 
    high_sugar = len(df[df['fbs']==1])
    print(f"High BP (>140): {high_BP}  ")
    print(f"High chol (>240): {high_chol}  ")
    print(f"High sugar (>120): {high_sugar}  ")

    critical = df[(df['trestbps']>140) & (df['chol']>240) & (df['fbs']==1)]

    critical_patients = len(critical)
    print(f"Critical patients: {critical_patients}  ")
    print(critical['target'].value_counts())

data_profile(df)