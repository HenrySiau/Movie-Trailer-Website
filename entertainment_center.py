import media
import fresh_tomatoes

# new instance "Ghost in the shell"
ghost_in_the_shell = media.Movie(
    "Ghost in the shell",
    '''A human who is cyber-enhanced to be a\
    perfect soldier devoted to stopping\
    the world's most dangerous criminals.''',
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMzJiNTI3MjItMGJiMy00YzA1LTg2MTItZmE1ZmRhOWQ0NGY1XkEyXkFqcGdeQXVyOTk4MTM0NQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=G4VmJcZR0Yg"
    )

# new instance "Avatar"
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",  # noqa
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
    )

# new instance "Pacific Rim"
pacific_rim = media.Movie(
    "Pacific Rim",
    "Human directly control robot to fight the ailences.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3MTI5NjQ4Nl5BMl5BanBnXkFtZTcwOTU1OTU0OQ@@._V1_SY1000_CR0,0,676,1000_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=B7-EqMGOM4E")

# new instance "Transformers: Age of Extinction"
age_of_extinction = media.Movie(
    "Transformers: Age of Extinction",
    '''A new group of humans,\
    led by Cade Yeager (Mark Wahlberg),\
    helps Optimus Prime (Peter Cullen) and the Autobots rise up\
    to meet their most fearsome challenge yet:\
    a worldwide war of good versus evil.''',
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1OTMyODA5M15BMl5BanBnXkFtZTgwMjc2MDk3MTE@._V1_.jpg",  # noqa
    "https://www.youtube.com/watch?v=dYDGqmxMZFI")

# new instance "Titanic"
titanic = media.Movie(
    "Titanic",
    "A man who died for love",
    "https://i.pinimg.com/736x/44/55/d9/4455d96357fb041d1cf3c8a5264ed593--titanic-leonardo-dicaprio-leonardo-dicaprio-kate-winslet.jpg",  # noqa
    "https://www.youtube.com/watch?v=s6mMvBeEPT4")

# new instance "WAR FOR THE PLANET OF THE APES "
apes = media.Movie(
    "War For The Planet Of The Apes",
    "Apes fight human.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOGIxMjIxNDYtOGU5Ny00OWE5LWEwMjEtY2U5NTE0YzY4YTUyXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=e9Dpy3yvEyg")

# put all the movies to a list
movies = [
    ghost_in_the_shell,
    avatar,
    pacific_rim,
    age_of_extinction,
    titanic,
    apes]

# open a web page to show case the movies
fresh_tomatoes.open_movies_page(movies)
