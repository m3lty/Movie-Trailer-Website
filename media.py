class Movie():
    """Movie() is a class for initilizing Movie objects within the
    entertainment_center.py file, for use with fresh_tomatoes.py.

    Attributes:
        movie_title(str): The title of the movie.
        movie_storyline(str): A short synopsis of the movie.
        poster_image_url(str): A link to an image of the movie's poster or boxart
        trailer_youtube_url(str): A link to a Youtube trailer for the movie.
        """
    #Initializes movie objects.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
