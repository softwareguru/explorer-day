# Script to create the session content files for Hugo from a csv file.

import csv
import os
with open('dataday-speakers.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        title = row['title']
        slug = row['slug']
        url = row['url']
        date = row['date']
        events = row['events'].split(", ")
        image = row['image']
        bio = row['bio']

        dirname = "speakers/"+slug
        try:
            os.mkdir(dirname)
        except FileExistsError:
            print("Dir "+dirname+" exists")
        except OSError:
            print ("Creation of the directory "+dirname+" failed" )
        else:
            print ("Successfully created the directory "+dirname)

        filename = dirname+"/_index.md"

        with open(filename, "w") as f:

            f.write("---\n")
            f.write("title: \""+title+"\"\n")
            f.write("url: "+url+"\n")
            f.write("image: "+image+"\n")
            f.write("date: "+date+"\n")
            f.write("events:\n")
            for s in events:
                f.write(" - "+s+"\n")
            f.write("---\n\n")
            f.write(bio)


