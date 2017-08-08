import media
import fresh_tomatoes

# new instance "Ghost in the shell"
ghost_in_the_shell = media.Movie("Ghost in the shell",
                        "A human who is cyber-enhanced to be a perfect soldier devoted to stopping the world's most dangerous criminals.",
                        "http://www.impawards.com/2017/posters/ghost_in_the_shell.jpg",
                        "https://www.youtube.com/watch?v=G4VmJcZR0Yg"
                        )


# new instance "Avatar"
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8"
                        )

# new instance "Pacific Rim"
pacific_rim = media.Movie("Pacific Rim",
                          "Human directly control robot to fight the ailences.",
                          "http://www.impawards.com/2013/posters/pacific_rim_ver3.jpg",
                          "https://www.youtube.com/watch?v=B7-EqMGOM4E")


# new instance "Transformers: Age of Extinction"
age_of_extinction = media.Movie("Transformers: Age of Extinction",
                          " A new group of humans, led by Cade Yeager (Mark Wahlberg), helps Optimus Prime (Peter Cullen) and the Autobots rise up to meet their most fearsome challenge yet: a worldwide war of good versus evil.",
                          "http://www.impawards.com/2014/posters/transformers_age_of_extinction_ver10.jpg",
                          "https://www.youtube.com/watch?v=dYDGqmxMZFI")

# new instance "Titanic"
titanic = media.Movie("Titanic",
                          "A man who died for love",
                          "https://i.pinimg.com/736x/44/55/d9/4455d96357fb041d1cf3c8a5264ed593--titanic-leonardo-dicaprio-leonardo-dicaprio-kate-winslet.jpg",
                          "https://www.youtube.com/watch?v=s6mMvBeEPT4")

# new instance "WAR FOR THE PLANET OF THE APES "
apes = media.Movie("War For The Planet Of The Apes ",
                          "Apes fight human.",
                          "http://www.impawards.com/2017/posters/war_for_the_planet_of_the_apes_ver3_xlg.jpg",
                          "https://www.youtube.com/watch?v=e9Dpy3yvEyg")


# put all the movies to a list
movies = [ghost_in_the_shell, avatar, pacific_rim,age_of_extinction,titanic,apes]

# open a web page to show case the movies
fresh_tomatoes.open_movies_page(movies)


