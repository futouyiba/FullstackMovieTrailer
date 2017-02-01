class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        The initiation method of a Movie object. Arguments are
        :param movie_title: a string to represent the title of a movie
        :param movie_storyline:  a string to represent the storyline of a movie
        :param poster_image:  a string to represent the box image of a movie
        :param trailer_youtube:  a string to represent the  url of a movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

