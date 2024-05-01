#!/bin/bash

#csv with streams,views,likes,comments
awk -F'>' 'BEGIN{OFS=">"} NR>1 {print $23, $19, $20, $21}' ../Preprocessing+Dataset/data.csv > streams-views-likes-comments.csv

