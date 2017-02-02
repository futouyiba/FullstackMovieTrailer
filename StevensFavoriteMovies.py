import csv
import media
import fresh_tomatoes

movies = []
csv_file = open('srcData.csv', 'rb')
movieReader = csv.reader(csv_file, dialect='excel')
print type(movieReader)
movieReader = movieReader

for row in movieReader:
    movie = media.Movie(row[0], row[1], row[2], row[3])
    movies.append(movie)

movies = movies[1:]

# This line is generating the webpage using fresh tomatoes.
fresh_tomatoes.open_movies_page(movies) 
