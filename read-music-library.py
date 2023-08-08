'''
Scan the music library file structure and save it to .csv
'''
import os

path = "..\Music"
line = ""
lines = []

with os.scandir(path) as music:
    # iterate through first level of the music library; these should be "artists"
    for m in music:
        if m.is_dir():
            line += m.name

            # for each "artist", iterate through their "albums"
            with os.scandir(m.path) as artist:
                for a in artist:
                    if a.is_dir():
                        line += "," + a.name

                        # for each album, iterate through songs
                        with os.scandir(a.path) as album:
                            for song in album:
                                if song.is_file() and song.name.endswith(".mp3"):
                                    line += "," + song.name.rpartition(".")[0]

                                    lines.append(line)
                                    
                                    line = m.name + "," + a.name

                        line = m.name

            line =""
    
with open("library.csv", "w") as file:
    for line in lines:
        file.write(f"{line}\n")


        



