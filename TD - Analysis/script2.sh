
awk -F '^' 'BEGIN { official_comments = 0; official_likes = 0; unofficial_comments = 0; unofficial_likes = 0 }
NR > 1 && NR <= 11 {
    if ($22 == 1) {
        official_comments += $21
        official_likes += $20
    } else {
        unofficial_comments += $21
        unofficial_likes += $20
    }
}
END {
    print "Official Videos - Comments:", official_comments, "Likes:", official_likes
    print "Unofficial Videos - Comments:", unofficial_comments, "Likes:", unofficial_likes

    if (official_comments > unofficial_comments) {
        print "Official videos typically have more comments."
    } else if (official_comments < unofficial_comments) {
        print "Unofficial videos typically have more comments."
    } else {
        print "Official and unofficial videos have the same number of comments."
    }

    if (official_likes > unofficial_likes) {
        print "Official videos typically have more likes."
    } else if (official_likes < unofficial_likes) {
        print "Unofficial videos typically have more likes."
    } else {
        print "Official and unofficial videos have the same number of likes."
    }
}' "$1"

