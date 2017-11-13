import fresh_tomatoes
import media

#Defining Movie objects.
trainspotting = media.Movie("Akira",
                            """A secret military project endangers Neo-Tokyo
                             when it turns a biker gang member into a rampaging
                             psychic psychopath that only two teenagers and a
                             group of psychics can stop.""",
                            "https://upload.wikimedia.org/wikipedia/en/5/5d/AKIRA_%281988_poster%29.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=-UhLderbuGI")

fear_and_loathing = media.Movie("Fear and Loathing in Las Vegas",
                   """An oddball journalist and his psychopathic lawyer travel
                       to Las Vegas for a series of psychedelic escapades.""",
                   "https://upload.wikimedia.org/wikipedia/en/6/6f/FandlinLV.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=8m662obIvhY")

pulp_fiction = media.Movie("Pulp Fiction",
                           """The lives of two mob hit men, a boxer, a
                           gangster's wife, and a pair of diner bandits
                           intertwine in four tales of violence and redemption.
                           """,
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=Mnb_3ibUp38")
# List of objects to be passed to fresh_tomatoes.py.
movies = [trainspotting, fear_and_loathing, pulp_fiction]

fresh_tomatoes.open_movies_page(movies)
