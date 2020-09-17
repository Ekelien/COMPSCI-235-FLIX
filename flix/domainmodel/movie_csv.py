from flix.domainmodel.movie import Movie
from flix.domainmodel.director import Director
from flix.domainmodel.actor import Actor
from flix.domainmodel.genre import Genre
import csv
class MovieFileCSVReader:
    def __init__(self,filename):
        self.filename=filename
        self.dataset_of_movies=[]
        self.dataset_of_actors=[]
        self.dataset_of_directors=[]
        self.dataset_of_genres=[]

    def read_csv_file(self):
        csv_file=open(self.filename,encoding='utf-8')
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            temp=dict(row)

            movie=Movie(temp['Title'], temp['Year'])
            if movie not in self.dataset_of_movies:
                self.dataset_of_movies.append(movie)

            for i in temp['Actors'].split(","):
                actor=Actor(i.strip())
                if actor not in self.dataset_of_actors:
                    self.dataset_of_actors.append(actor)

            direct=Director(temp['Director'])
            if direct not in self.dataset_of_directors:
                self.dataset_of_directors.append(direct)

            for i in temp['Genre'].split(","):
                genre=Genre(i.strip())
                if genre not in self.dataset_of_genres:
                    self.dataset_of_genres.append(genre)

    def get_dict_by_genre(self):
        csv_file = open(self.filename, encoding='utf-8')
        csv_reader = csv.DictReader(csv_file)
        return_dic = {}
        for row in csv_reader:
            temp = dict(row)
            movie = Movie(temp['Title'], temp['Year'])
            for i in temp['Genre'].split(","):
                genre = Genre(i.strip())
                if genre not in return_dic:
                    return_dic[genre] = [movie]
                else:
                    return_dic[genre].append(movie)
                movie.add_genre(genre)
        return return_dic
