# t-tests and p-value in scipy.stats()

import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('heart.csv')

group_disease = df[df['target']==1]['chol']
group_no_disease = df[df['target']==0]['chol']

t_stat, p_value = stats.ttest_ind(group_disease,group_no_disease,equal_var=False)

print(f"Calculated T-Statistic: {t_stat:.4f}")
print(f"Calculated P-Value: {p_value:.6f}")