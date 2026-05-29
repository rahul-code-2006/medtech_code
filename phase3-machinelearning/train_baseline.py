import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

df = pd.read_csv('heart.csv')
df.drop_duplicates(inplace=True)

#------Include dependency of thalach on age---------
df['max_hr_capacity']= (df['thalach'])/(220-df['age'])

#---------Seperate features--------------

X = df[['age','chol']]
Y = df['target']

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.20,stratify=Y,random_state=42)


#Generating interaction terms

# include_bias=False prevents adding a column of 1s

poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train_int = poly.fit_transform(X_train)
X_test_int = poly.transform(X_test)

feature_names = poly.get_feature_names_out(X.columns)

scaler = StandardScaler()

#Fit ONLY for training set, transform test set also

X_train_scaled = scaler.fit_transform(X_train_int)
X_test_scaled = scaler.transform(X_test_int)

print(f"Training set size: {X_train_scaled.shape[1]} patients")
print(f"Testing set size: {X_test_scaled.shape[1]} patients")

#Initialize and fit the baseline model
log_reg = LogisticRegression(solver='lbfgs', random_state=42)
log_reg.fit(X_train_scaled,Y_train)

#Extract intercept and coefficients
intercept = log_reg.intercept_[0]
coefficients = log_reg.coef_[0]

# Map back to feature names
coef_dict = dict(zip(X.columns, coefficients))
print(f"Model Intercept (Beta_0): {intercept:.4f}")

for feature, coef in coef_dict.items():
    print(f"Beta weight for {feature}: {coef:.4f}")


#Clinical interpretation and results
print("======= Clinical interpretation and it's result ========")

for feature, coef in coef_dict.items():
    odds_ratio = np.exp(coef)
    print(f"Feature : {feature}")
    print(f"Standardized Beta  (\beta): {coef:.4f}")
    print(f"Odds ratio: {odds_ratio:.4f}")

    if odds_ratio > 1:
        percent_increase = (odds_ratio-1)*100
        print(f"  Interpretation: Every 1 standard deviation increase in '{feature}' increases the odds of heart disease by {percent_increase:.1f}%.")
    
    else:
        percent_decrease = (1 - odds_ratio) * 100
        print(f"  Interpretation: Every 1 standard deviation increase in '{feature}' decreases the odds of heart disease by {percent_decrease:.1f}%.")



#Build the confusion matrix and compute the roc-auc score

#Step 1 predict and hard label as 1 or 0
y_proba = log_reg.predict_proba(X_test_scaled)[:,1]
y_labeled = (y_proba >= 0.485).astype(int)

#Step 2 Build the confusion matrix
tn, fp, fn, tp = confusion_matrix(Y_test,y_labeled).ravel()

#step 3 Compute the global discriminatory power
auc_score = roc_auc_score(Y_test,y_proba) 


print(f"Confusion Matrix Metrics:")
print(f"➔ True Positives: {tp} | False Negatives: {fn}")
print(f"➔ True Negatives: {tn} | False Positives: {fp}\n")
print(f"ROC-AUC Score: {auc_score:.4f}")