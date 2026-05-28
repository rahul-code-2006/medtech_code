import plotly.express as px
import pandas as pd

df = pd.read_csv('heart.csv')
df_cleaned = df.drop_duplicates()

fig = px.histogram(
    df_cleaned,
    x='thalach',
    color='target',
    marginal="box", # Adds a side-by-side boxplot directly on top of the distribution!
    barmode="overlay",
    opacity=0.6,
    color_discrete_map={0: "#2ca02c", 1: "#d62728"}, # Green for healthy, Red for diseased
    labels={"thalach": "Max Heart Rate Achieved (bpm)", "target": "Cardiac Status"},
    title="Interactive Distribution: Max Heart Rate vs Cardiac Disease Status"
)

# 2. Polishing the layout for a dark theme aesthetic
fig.update_layout(
    template="plotly_dark",
    legend_title_text="Condition",
    barmode="overlay"
)

# 3. Update legend labels for readability
new_names = {'0': 'Healthy (0)', '1': 'Heart Disease (1)'}
fig.for_each_trace(lambda t: t.update(name = new_names[t.name]))

# Render the interactive canvas directly inside your browser window
fig.show()