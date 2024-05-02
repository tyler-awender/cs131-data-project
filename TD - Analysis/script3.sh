
awk -F '^' 'BEGIN { official_likes = 0; official_comments = 0; unofficial_likes = 0; unofficial_comments = 0; official_count = 0; unofficial_count = 0; }
NR > 1 {
    if ($22 == 1) {
        official_likes += $20;
        official_comments += $21;
        official_count++;
    } else {
        unofficial_likes += $20;
        unofficial_comments += $21;
        unofficial_count++;
    }
}
END {
    if (official_count > 0) {
        official_likes_avg = official_likes / official_count;
        official_comments_avg = official_comments / official_count;
        print "Average Likes for Official Videos:", official_likes_avg;
        print "Average Comments for Official Videos:", official_comments_avg;
    }

    if (unofficial_count > 0) {
        unofficial_likes_avg = unofficial_likes / unofficial_count;
        unofficial_comments_avg = unofficial_comments / unofficial_count;
        print "Average Likes for Unofficial Videos:", unofficial_likes_avg;
        print "Average Comments for Unofficial Videos:", unofficial_comments_avg;
    } 

}' "New_Spotify_Youtube.csv" > analysis3.txt

