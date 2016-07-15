import movietrailer
import render_page

ironman = movietrailer.MovieTrailer(
    "Iron Man",
    "It is a story about Iron Man!!",
    "Great",
    "https://www.youtube.com/watch?v=8hYlB38asDY")
# print ironman.title
# ironman.show_trailer()

# print movietrailer.MovieTrailer.VALID_RATINGS
# print movietrailer.MovieTrailer.__doc__  #Root variable to print out
# whats in triple quotes

shockandawe = movietrailer.Documentaries(
    "Shock and Awe",
    "It is a story about Electricity!!",
    "Great",
    "https://www.youtube.com/watch?v=Gtp51eZkwoI",
    "BBC")
# print shockandawe.channel
# print shockandawe.title
# shockandawe.show_trailer() #even child can inherit the functions created
# inside parent

movies = [ironman, shockandawe]

render_page.open_movies_page(movies)
