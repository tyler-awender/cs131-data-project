#!/bin/bash

#create csv with following data: Artist^Track^Danceability^Valence
awk -F '^' 'BEGIN{OFS="^"} {print $2,$3,$6,$14}' New_Spotify_Youtube.csv > dance-val.csv

#create csv with following data: Artist^Track^Tempo^Stream
awk -F '^' 'BEGIN{OFS="^"} {print $2,$3,$15,$23}' New_Spotify_Youtube.csv > tempo-stream.csv
