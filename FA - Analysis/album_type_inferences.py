import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('album_type_inferences.csv', delimiter='>')

filtered_albums = df.groupby('Album')['Album_type'].nunique()
filtered_albums = filtered_albums[filtered_albums == 2].index.tolist()
df2 = df[df['Album'].isin(filtered_albums)]

# 1. Popularity of tracks -- analyzing the correlation between Youtube views and Spotify streams

youtube_views = df['Views']
spotify_streams = df['Stream']
correlation = youtube_views.corr(spotify_streams)
print("Correlation between YouTube views and Spotify streams: ", correlation)


# 2. Album vs Single performance: compare the avg views/streams of tracks categorized as "album" vs "single"

print('\n')

album_views = df[df['Album_type'] == 'album']['Views']
single_views = df[df['Album_type'] == 'single']['Views']
album_streams = df[df['Album_type'] == 'album']['Stream']
single_streams = df[df['Album_type'] == 'single']['Stream']

avg_album_views = album_views.mean()
avg_single_views = single_views.mean()
avg_album_streams = album_streams.mean()
avg_single_streams = single_streams.mean()

print("Avg views for album tracks: ", avg_album_views)
print("Avg views for single tracks: ", avg_single_views)
print("Avg streams for album tracks: ", avg_album_streams)
print("Avg streams for single tracks: ", avg_single_streams)


#3. Compare performance within the same album based on album type 

print('\n')
albums = df2['Album'].unique()
# for album in albums:
#     album_data = df2[df2['Album'] == album]
#     album_single_views = album_data[album_data['Album_type'] == 'single']['Views']
#     album_album_views = album_data[album_data['Album_type'] == 'album']['Views']
#     album_single_streams = album_data[album_data['Album_type'] == 'single']['Stream']
#     album_album_streams = album_data[album_data['Album_type'] == 'album']['Stream']

#     print(f"Album: {album}")
#     print("Average views for single tracks:", album_single_views.mean())
#     print("Average views for album tracks:", album_album_views.mean())
#     print("Average streams for single tracks:", album_single_streams.mean())
#     print("Average streams for album tracks:", album_album_streams.mean())
#     print()
    

album_single_avg_views = []
album_album_avg_views = []
album_single_avg_streams = []
album_album_avg_streams = []
for album in albums:
    album_data = df2[df2['Album'] == album]
    album_single_avg_views.append(album_data[album_data['Album_type'] == 'single']['Views'].mean())
    album_album_avg_views.append(album_data[album_data['Album_type'] == 'album']['Views'].mean())
    album_single_avg_streams.append(album_data[album_data['Album_type'] == 'single']['Stream'].mean())
    album_album_avg_streams.append(album_data[album_data['Album_type'] == 'album']['Stream'].mean())

# Data Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].bar(['Singles', 'Albums'], [avg_single_views, avg_album_views], color=['blue', 'orange'])
axes[0].set_title('Average Views')
axes[0].set_ylabel('Views')
axes[0].set_xlabel('Track Type')

axes[1].bar(['Singles', 'Albums'], [avg_single_streams, avg_album_streams], color=['blue', 'orange'])
axes[1].set_title('Average Streams')
axes[1].set_ylabel('Streams')
axes[1].set_xlabel('Track Type')

plt.tight_layout()
plt.show()
