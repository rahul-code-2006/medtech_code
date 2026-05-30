import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier

from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix

#Got the database
df = pd.read_csv('heart.csv')

#Seperate the variables
X = df[['thalach','age','chol']]
Y = df['target']

#Seperate the training and testing data
X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

#Build a tree and XGboost

tuned_tree = DecisionTreeClassifier(
    max_depth=8,
    min_samples_leaf=10,
    random_state=42
) 

tuned_xgb = XGBClassifier(
    n_estimators = 50,
    learning_rate = 0.08,
    max_depth = 2,
    random_state = 42,
    eval_metric = 'logloss'
)

#train

tuned_tree.fit(X_train,Y_train)
tuned_xgb.fit(X_train,Y_train)

tree_probs = tuned_tree.predict_proba(X_test)[:,1]
xg_probs = tuned_xgb.predict_proba(X_test)[:,1]

tree_labelled = (tree_probs >= 0.5).astype(int)
xg_labelled = (xg_probs >= 0.5).astype(int)

#Confusion matrix of trees and XGboosts
ttp, tfn, tfp, ttn = confusion_matrix(Y_test,tree_labelled).ravel()
xtp, xfn, xfp, xtn = confusion_matrix(Y_test,xg_labelled).ravel()


print(f"Confusion Matrix Metrics of tree:")
print(f"➔ True Positives: {ttp} | False Negatives: {tfn}")
print(f"➔ True Negatives: {ttn} | False Positives: {tfp}\n")


print(f"Confusion Matrix Metrics of xgboost:")
print(f"➔ True Positives: {xtp} | False Negatives: {xfn}")
print(f"➔ True Negatives: {xtn} | False Positives: {xfp}\n")


#Test ROC-AUC
print(f"Tuned Tree ROC-AUC: {roc_auc_score(Y_test, tree_probs):.4f}")
print(f"Tuned XGBoost ROC-AUC: {roc_auc_score(Y_test, xg_probs):.4f}")

# Explicitly evaluate XGBoost using 5-Fold Cross-Validation
cv_scores = cross_val_score(
    tuned_xgb, X, Y, cv=5, scoring='roc_auc', n_jobs=-1
)

print(f"All 5 Fold AUC Scores: {cv_scores}")
print(f"Mean CV ROC-AUC:       {cv_scores.mean():.4f}")
print(f"Score Variance (Std):  {cv_scores.std():.4f}")


# Print the feature importance weights
importances = tuned_xgb.feature_importances_
for col, imp in zip(X.columns, importances):
    print(f"Feature: {col:<10} Importance: {imp:.4f}")

