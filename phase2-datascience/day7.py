import pandas as pd

df = pd.read_csv('heart.csv')

def get_pct(part, whole):
    return round(part / whole * 100, 1) if whole > 0 else 0


def disease_analysis(df):

    means = df.groupby('target').mean().round(1)
    diseased = means.loc[1]
    no_disease = means.loc[0]
    print('='*50)
    print("         Heart Disease - Group Analysis Report")
    print('='*50)

    
    print("\n--- Mean vitals by disease status ---")
    print("                No disease   Disease    Difference")
    
    print(f"Age (years):    {no_disease['age']:.1f}      {diseased['age']:.1f}        {diseased['age'] - no_disease['age']:.1f}")
    print(f"Max HR (bpm):   {no_disease['thalach']:.1f}      {diseased['thalach']:.1f}        {diseased['thalach'] - no_disease['thalach']:.1f}")
    print(f"Resting BP:     {no_disease['trestbps']:.1f}      {diseased['trestbps']:.1f}        {diseased['trestbps'] - no_disease['trestbps']:.1f}")
    print(f"Cholesterol:    {no_disease['chol']:.1f}      {diseased['chol']:.1f}        {diseased['chol'] - no_disease['chol']:.1f}")
    print(f"ST depression:  {no_disease['oldpeak']:.1f}      {diseased['oldpeak']:.1f}        {diseased['oldpeak'] - no_disease['oldpeak']:.1f}")
    
    
    
    print("\n--- Chest Pain Distribution ---")

    cp_group = df.groupby(['target', 'cp']).size()
    
    for i in range(4):
        no_disease_count = cp_group.get((0, i), 0)
        disease_count = cp_group.get((1, i), 0)
        print(f"Chest Pain Type {i}:  No disease: {no_disease_count}   |  Disease: {disease_count}")

    print("\n--- Gender Analysis ---")

    sex_group = df.groupby(['target','sex']).size()

    total_male_patients = len(df[df['sex']==1])
    total_female_patients = len(df[df['sex']==0])
    male_diseased = sex_group.get((1, 1),0)
    female_diseased = sex_group.get((1, 0),0)
    male_no_disease = sex_group.get((0, 1),0)
    female_no_disease = sex_group.get((0, 0),0)
    male_diseased_pct = get_pct(male_diseased, total_male_patients)
    female_diseased_pct = get_pct(female_diseased, total_female_patients)
    male_no_disease_pct = get_pct(male_no_disease, total_male_patients)
    female_no_disease_pct = get_pct(female_no_disease, total_female_patients)

    print(f"{'Male patients':<16}: No disease: {male_no_disease:<4}   ({male_no_disease_pct}%) | Disease:  {male_diseased:<4}   ({male_diseased_pct}%)")
    print(f"{'Female patients':<16}: No disease: {female_no_disease:<4}   ({female_no_disease_pct}%) | Disease: {female_diseased:<4}   ({female_diseased_pct}%)")

    print("\n--- Key Insights ---")
    differences = (diseased - no_disease).abs()
    most_predictive = differences.idxmax()
    print(f"Most predictive factor by group difference: {most_predictive}")
    print(f"Patients with cp type 3 and disease: {cp_group.get((1,3),0)}")
    print('='*50)

disease_analysis(df)
print(df.groupby('sex')['age'].mean().round(1))