class Song:
    # Class attributes (shared by all Song objects)
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes (unique to each Song)
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level statistics whenever a song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # Class Methods

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

    # Instance method to display song info
    def display_info(self):
        return f"Song: {self.name}, Artist: {self.artist}, Genre: {self.genre}"

    # Class method to display all statistics
    @classmethod
    def display_statistics(cls):
        return {
            "Total Songs": cls.count,
            "Unique Genres": list(cls.genres),
            "Unique Artists": list(cls.artists),
            "Songs per Genre": cls.genre_count,
            "Songs per Artist": cls.artists_count
        }


# Example usage:

# Build song objects
song1 = Song("Blinding Lights", "The Weeknd", "Pop")
song2 = Song("Shape of You", "Ed Sheeran", "Pop")
song3 = Song("HUMBLE", "Kendrick Lamar", "Hip-Hop")

# See information about individual songs
print(song1.display_info())
print(song2.display_info())
print(song3.display_info())

print()

# See information about all songs
print(Song.display_statistics())