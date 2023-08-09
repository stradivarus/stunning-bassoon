'''
Scan the music library file structure and save it to .csv
'''
import os
from tinytag import TinyTag


path = r"..\muzik"
lines = []


def scan_folder(_path):

    with os.scandir(_path) as folder:
        for f in folder:
            if f.is_file() and f.name.endswith((".mp3", ".m4a", ".aac", ".wav", ".flac")):
                tag = TinyTag.get(f)
                lines.append(f"{tag.artist},{tag.album},{tag.title},{tag.track},{tag.year},{tag.genre}")
            
            elif f.is_dir():
                scan_folder(f"{_path}\{f.name}")


scan_folder(path)


with open("library.csv", "w") as file:
    file.write("Artist,Album,Title,Track,Year,Genre\n")
    for line in lines:
        file.write(f"{line}\n")






        



