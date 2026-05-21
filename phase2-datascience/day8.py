import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')
# Add this once after loading df, before the function
df['target'] = df['target'].map({0: 'No Disease', 1: 'Disease'})

# Now 1 = Disease, 0 = No Disease — standard convention
def visualise_findings(df):
    # Set a clean style
    sns.set_style("whitegrid")

    # Simple distribution plot
    fig, axes = plt.subplots(2,2,figsize=(14,10))

    sns.histplot(data=df, x='age', hue='target', ax=axes[0][0])
    axes[0][0].set_title('Age Distribution by Heart Disease Status')
    axes[0][0].set_xlabel('Age')
    axes[0][0].set_ylabel('Count')
    
    sns.histplot(data=df, x='thalach', hue='target', ax=axes[0][1])
    axes[0][1].set_title('Max HR Distribution by Heart Disease Status')
    axes[0][1].set_xlabel('Max HR')
    axes[0][1].set_ylabel('Count')

    sns.countplot(data=df, x='cp', hue='target', ax=axes[1][0])
    axes[1][0].set_title('Chest Pain type count by Heart Disease Status')
    axes[1][0].set_xlabel('Chest Pain type')
    axes[1][0].set_ylabel('Count')


    sns.histplot(data=df, x='chol', hue='target', ax=axes[1][1])
    axes[1][1].set_title('Cholesterol Distribution by Heart Disease Status')
    axes[1][1].set_xlabel('Cholesterol')
    axes[1][1].set_ylabel('Count')




    plt.tight_layout()
    plt.savefig('findings.png')
    plt.show()


visualise_findings(df)