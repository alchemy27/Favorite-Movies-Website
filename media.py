import webbrowser

class Movie():
    ''' This init function is the first to be passed in, will instantiate the
    objects and each will have its own characteristics (like a different name,
    different picture, etc.'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube): #self is the object
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    ''' This is just a function to open the youtube url of the movie trailer
    for each particular movie.'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
