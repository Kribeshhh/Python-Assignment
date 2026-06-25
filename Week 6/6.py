import random

class Playlist:
    def __init__(self):
        self.songs = []

    def shuffle(self):
        random.shuffle(self.songs)


playlist = Playlist()

for i in range(5):
    print(f"\nEnter Song {i+1}")
    title = input("Song Title: ")
    artist = input("Artist: ")

    playlist.songs.append({
        "title": title,
        "artist": artist
    })

playlist.shuffle()

print("\nShuffled Playlist:")

for song in playlist.songs:
    print("Title:", song["title"], "| Artist:", song["artist"])