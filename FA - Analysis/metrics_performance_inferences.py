import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
data = pd.read_csv("metrics_performance_inferences.csv", delimiter='>')

# 1. Visualizing correlation of metrics with Spotify views in a spider chart
features = ['Danceability', 'Energy',  'Speechiness', 'Acousticness', 'Instrumentalness', 'Valence']

avg_values = data[features].mean().values

num_vars = len(features)

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

avg_values=np.concatenate((avg_values,[avg_values[0]]))
angles+=angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, avg_values, color='skyblue', alpha=0.6)

ax.set_yticklabels([])
plt.xticks(angles[:-1], features)

ax.fill(angles, avg_values, color='skyblue', alpha=0.6)

plt.show()

# 2. Visualizing correlation of metrics with Spotify views in a bar graph

correlation = df2.corr()['Stream']

print(correlation)

correlation.drop('Stream', inplace=True)  # Drop the 'Stream' itself
correlation.plot(kind='bar', figsize=(10, 6))
plt.title('Correlation of Metrics with Streams')
plt.xlabel('Feature')
plt.ylabel('Correlation Coefficient')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Visualizing correlation of metrics with YouTube views in scatterplots

youtube_metric = 'Views'
spotify_metrics = ['Danceability', 'Energy', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Valence']

fig, axs = plt.subplots(len(spotify_metrics), 1, figsize=(5,15))
fig.subplots_adjust(hspace=0.5, wspace=0.5)

for j, spotify_metric in enumerate(spotify_metrics):
    axs[j].scatter(data[youtube_metric], data[spotify_metric], alpha=0.5)
    axs[j].set_xlabel(youtube_metric)
    axs[j].set_ylabel(spotify_metric)

plt.show()
