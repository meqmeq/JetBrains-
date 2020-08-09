def tracklist(**kwargs):
    for title in kwargs:
        print(title)
        for i, j in kwargs[title].items():
            print(f'ALBUM: {i} TRACK: {j}')

# tracklist(Woodkid={"The Golden Age": "Run Boy Run",
#                    "On the Other Side": "Samara"},
#           Cure={"Disintegration": "Lovesong",
#                 "Wish": "Friday I'm in love",
#                 "Seventeen Seconds": "A Forest"})
