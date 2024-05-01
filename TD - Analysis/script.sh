
echo "Top 10 Artists by Total Streams on Spotify:"
echo "-----------------------------------------"

awk -F '^' 'NR > 1 {
    artist = $2
    streams = $23
    artist_streams[artist] += streams
} 
END {
    for (artist in artist_streams) {
        if (artist != "") {
            printf "%-30s %d\n", artist, artist_streams[artist]
        }
    }
}' "$1" | sort -k2,2nr | head -n 10

echo " "

echo "Top 10 Artists by Total Views on YouTube:"
echo "-----------------------------------------"
echo

awk -F '^' 'NR > 1 {
    artist = $2
    views = $19
    artist_views[artist] += views
}
END {
    for (artist in artist_views) {
        if (artist != "") {
            printf "%-30s %-15d\n", artist, artist_views[artist]
        }
    }
}' "$1" | sort -k2,2nr | head -n 10

