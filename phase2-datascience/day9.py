import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')


# Correlation matrix — how strongly each variable relates to every other
corr = df.corr(numeric_only=True)
#print(corr['target'].sort_values(ascending=False))


def plot_correlation(corr):
    
    corr = df.corr(numeric_only=True)
    fig , ax = plt.subplots(figsize=(12,10))
    sns.heatmap(data = corr,annot=True, cmap='coolwarm', fmt = '.2f', ax = ax )
    plt.title('Feature Correlation Matrix - Heart Disease Dataset')
    
    plt.tight_layout()
    plt.savefig('correlation-heatmap.png')
    plt.show()



def predictor_summary(corr):
    print('='*50)
    print("         Heart Disease - Predictor Ranking")
    print('='*50)
    print("Rank    Feature       Correlation        Strength")
    sorted_corr = corr['target'].abs().sort_values(ascending=False)
    #Now what we need is the ability to identify which is positive and negative and print each one seperate
    keys = list(sorted_corr.keys())
    j=1
    for i in keys:
        if i == 'target':
            continue
        column = sorted_corr[i]
        Strength = "Strong"  if column >= 0.35 else "Moderate" if column >= 0.2 else "Weak"
        
        if (corr['target'][i]) >= 0:
            print(f"{j:<7} {i:<16} {column.round(3):<16} {Strength}")
        else:
            print(f"{j:<7} {i:<16}-{column.round(3):<16} {Strength}")
        j=j+1

    print('='*50)
    print(f"Strongest Predictor   : {keys[1]}")
    print(f"Weakest Predictor     : {keys[len(keys)-1]}")
    print('='*50)

plot_correlation(corr)
predictor_summary(corr)