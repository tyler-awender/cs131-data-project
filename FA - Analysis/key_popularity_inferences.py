import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('key_popularity_inferences.csv', delimiter='>')

# Create scatter plots
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

# Scatter plot for Key vs Views
axes[0].scatter(df['Key'], df['Views'], alpha=0.5)
axes[0].set_title('Key vs Views')
axes[0].set_xlabel('Key')
axes[0].set_ylabel('Views')

# Scatter plot for Key vs Likes
axes[1].scatter(df['Key'], df['Likes'], alpha=0.5)
axes[1].set_title('Key vs Likes')
axes[1].set_xlabel('Key')
axes[1].set_ylabel('Likes')

# Scatter plot for Key vs Stream
axes[2].scatter(df['Key'], df['Stream'], alpha=0.5)
axes[2].set_title('Key vs Stream')
axes[2].set_xlabel('Key')
axes[2].set_ylabel('Stream')

plt.tight_layout()
plt.show()
