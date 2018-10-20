searchfile = open("twitter_data.txt", "r")
for line in searchfile:
    if "sentiment" in line: print line
searchfile.close()
