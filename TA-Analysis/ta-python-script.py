import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('streams-views-likes-comments.csv', delimiter='>')

# Print column names to see what they are
print(df.columns)

# Extract all columns
streams = df.Stream
comments = df.Comments
likes = df.Likes
views = df.Views
duration = df.Duration_ms

duration_s = duration / 1000

print(duration_s)

# Scatter plot for Youtube Views vs Comments 
plt.xticks(range(1, 6))
plt.figure(figsize=(10, 6))
plt.scatter(views, comments, color='blue', alpha=0.5, s=1)
plt.title('Views vs Comments')
plt.xlabel('Streams')
plt.ylabel('Views')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()

# Scatter plot for Spotify Streams vs Youtube Views
plt.figure(figsize=(10, 6))
plt.scatter(streams, views, color='red', alpha=0.5, s=1)
plt.title('Streams vs Views')
plt.xlabel('Streams')
plt.ylabel('Views')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()

# Scatter plot for Duration vs Youtube Views
plt.figure(figsize=(10, 6))
plt.scatter(duration, views, color='red', alpha=0.5, s=1)
plt.title('Duration vs Views')
plt.xlabel('Duration')
plt.ylabel('Views')
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()

#Histogram for duration and frequency
plt.xlim(0, 700)
plt.ylim(0, 900)
plt.hist(duration_s, bins=1000, color='blue')
plt.title('Duration and Frequency')
plt.xlabel('Duration in Seconds')
plt.ylabel('Frequency')
plt.xscale('linear')
plt.yscale('linear')
plt.show()