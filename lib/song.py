class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


song1 = Song("Heis", "Rema", "Afrobeat")
song2 = Song("Yawa", "FireBoy DML", "Afrobeat")
song3 = Song("Not Like Us", "Kendrick Lamar", "Rap")
song4 = Song("Lose Yourself", "Eminem", "Rap")
song5 = Song("God's Plan", "Drake", "Rap")
song6 = Song("Ring of Fire", "Johnny Cash", "Country")
song7 = Song("Hurt", "Johnny Cash", "Country")
song8 = Song("Old Town Road", "Lil Nas X", "Country")

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)
