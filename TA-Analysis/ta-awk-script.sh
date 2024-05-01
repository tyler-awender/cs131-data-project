#!/bin/bash

#csv with streams,views,likes,comments,duration
awk -F'>' 'BEGIN{ OFS=">" } { print $23, $19, $20, $21, $16 }' ../Preprocessing+Dataset/data.csv > streams-views-likes-comments-duration.csv

