class Song:
    #class variables shared by all the songs
    count=0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}

    def __init__(self,name,artist,genre):
        #instance varables unique to each song
        self.name=name
        self.artist=artist
        self.genre=genre

        #update total song count
        self.add_song_to_count()

        #update genres(avoid duplicates)
        Song.add_to_genres(genre)

        #update artist(avoid duplicates)
        Song.add_to_artists(artist)

        #update genre count in dictionary
        Song.genre_count[genre]=Song.genre_count.get(genre,0)+1
        #update artist count in dictionary
        Song.artist_count[artist]=Song.artist_count.get(artist,0)+1

    @classmethod
    def add_song_to_count(cls, increment=1):
        #increase total number of songs
        cls.count+=increment

    @classmethod
    def add_to_genres(cls,genre):
        #add genre if its not in the list to avoid duplicates
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        #add artist  if they aren't already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)




