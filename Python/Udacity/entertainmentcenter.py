import movietrailer

ironman = movietrailer.MovieTrailer("Iron Man","It is a story about Iron Man!!","Great","https://www.youtube.com/watch?v=8hYlB38asDY") 
print ironman.title
#ironman.show_trailer()

print movietrailer.MovieTrailer.VALID_RATINGS 
print movietrailer.MovieTrailer.__doc__  #Root variable to print out whats in triple quotes