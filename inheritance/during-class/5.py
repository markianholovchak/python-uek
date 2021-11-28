class Song():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f"Performer: {self.artist}\nSong: {self.title}\nAlbum: {self.album}\nYear: {self.year}"

firstSong = Song("Ed Sheeran", "Hearts Don't Break Aroung Here", "Divide", 2017)
secondSong = Song("Alan Walker", "Faded", "Different World", 2015)
thirdSong = Song("Tiesto", "The Motto", "The Motto", 2021)
print(firstSong)
print(thirdSong)
print(secondSong)