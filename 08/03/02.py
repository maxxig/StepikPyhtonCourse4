from enum import Flag

class MovieGenres(Flag):
    ACTION = 1
    COMEDY = 2
    DRAMA = 4
    FANTASY = 8
    HORROR = 16

class Movie:
    def __init__(self, name, genres: MovieGenres):
        self.name = name
        self.genres = genres
    def in_genre(self, g):
        if isinstance(g, MovieGenres):
            if(len(g & self.genres)) > 0:
                return True
            else:
                return False
    def __repr__(self):
        return f'{self.name}'