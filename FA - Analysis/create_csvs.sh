#!/bin/bash

# Creates csv with columns Track>Album_name>Album_type>Views>Likes>Comments>Stream
awk -F'^' 'BEGIN { OFS="^"} { print $3, $4, $5, $17, $19, $20, $21, $23 }' New_Spotify_Youtube.csv > album_type_inferences.csv 

# Creates csv with columns Danceability>Energy>Key>Loudness>Speechiness>Acousticness>Instrumentalness>Liveness>Valence>Tempo>Duration_ms>Views>Likes>Comments>Stream
awk -F'^' 'BEGIN { OFS="^"} { print $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $19, $20, $21, $23 }' New_Spotify_Youtube.csv > metrics_performance_inferences.csv


