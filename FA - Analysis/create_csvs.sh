#!/bin/bash

# Creates csv with columns Track>Album_name>Album_type>Views>Likes>Comments>Stream
awk -F'>' 'BEGIN { OFS=">"} { print $3, $4, $5, $17, $19, $20, $21, $23 }' data.csv > album_type_inferences.csv 

# Creates csv with columns Track>Key>Views>Likes>Stream
awk -F'>' 'BEGIN { OFS=">"} { print $3, $8, $19, $20, $23 }' data.csv > key_popularity_inferences.csv

