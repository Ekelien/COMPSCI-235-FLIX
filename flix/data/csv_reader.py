import csv
from flix.domainmodel.movie import Movie
from flix.domainmodel.director import Director
from flix.domainmodel.actor import Actor
from flix.domainmodel.genre import Genre

class MovieFileCSVReader:
    def __init__(self,filename):
        self.filename=filename
        self.dataset_of_movie=[]
        self.dataset_of_genre={}
        self.dataset_of_director=[]
        self.dataset_of_actors=[]



    def read_csv_file(self):
        csv_file = open(self.filename, encoding='utf-8')
        csv_reader = csv.DictReader(csv_file)
        # reading csv like dictionary
        for row in csv_reader:
            # a row with dictionary form
            temp=dict(row)

            # dataset of movie
            movie=Movie(temp['Title'], temp['Year'])
            # add actor
            for item in temp['Actors'].split(","):
                actor=Actor(item)
                movie.add_actor(actor)
            # set director
            director=Director(temp['Director'])
            movie.director=director
            # add genre
            for item in temp['Genre'].split(","):
                genre=Genre(item)
                movie.add_genre(genre)
            self.dataset_of_movie.append(movie)

            # dataset of actor
            for item in temp['Actors'].split(","):
                actor=Actor(item)
                if actor not in self.dataset_of_actors:
                    actor.participate_in(movie)
                    self.dataset_of_actors.append(actor)
                else:
                    self.dataset_of_actors[self.dataset_of_actors.index(actor)].participate_in(movie)

            # dataset of genre
            for i in temp['Genre'].split(","):
                genre = Genre(i.strip())
                if genre not in self.dataset_of_genre:
                    self.dataset_of_genre[genre] = [movie]
                else:
                    self.dataset_of_genre[genre].append(movie)

            # dataset of director
            for item in temp['Director']:
                director=Director(item)
                if director not in self.dataset_of_director:
                    director.is_director_of(movie)
                    self.dataset_of_director.append(director)
                else:
                    self.dataset_of_director[self.dataset_of_director.index(director)].is_director_of(movie)
