import csv
from linvie.domainmodel.movie import Movie
from linvie.domainmodel.genre import Genre
from linvie.domainmodel.people import People


class MovieFileCSVReader:
    def __init__(self, filename):
        self.filename = filename
        self.dataset_of_movie = []
        self.dataset_of_people = []
        self.dataset_of_director = []
        self.dataset_of_actors = []
        self.dataset_of_genre = {}

    def read_csv_file(self):
        csv_file = open(self.filename, encoding='utf-8')
        csv_reader = csv.DictReader(csv_file)  # reading csv like dictionary

        print("Start processing csv file ...")
        for row in csv_reader:
            # a row with dictionary form
            temp = dict(row)

            # movie
            movie = Movie(temp['Title'], temp['Year'])
            # add actor
            for item in temp['Actors'].split(","):
                actor = People(item)
                movie.add_actor(actor)
                if actor not in self.dataset_of_people:
                    actor.is_actor()
                    actor.participate_in(movie)
                    self.dataset_of_people.append(actor)
                else:
                    index = self.dataset_of_people.index(actor)
                    self.dataset_of_people[index].is_actor()
                    self.dataset_of_people[index].participate_in(movie)

            # set director
            director = People(temp['Director'])
            movie.director = director
            if director not in self.dataset_of_people:
                director.direct(movie)
                self.dataset_of_people.append(director)
            else:
                index = self.dataset_of_people.index(director)
                self.dataset_of_people[index].is_director()
                self.dataset_of_people[index].direct(movie)
            # add genre
            for item in temp['Genre'].split(","):
                genre = Genre(item)
                movie.add_genre(genre)
                if genre not in self.dataset_of_genre:
                    self.dataset_of_genre[genre] = [movie]
                else:
                    self.dataset_of_genre[genre].append(movie)
            # set url
            movie.url = temp['Image']
            movie.file = temp['File']
            # add movie into dataset
            self.dataset_of_movie.append(movie)

        print("Processing directors and actors...")
        for person in self.dataset_of_people:
            if person.if_is_director():
                self.dataset_of_director.append(person)
            if person.if_is_actor():
                self.dataset_of_actors.append(person)
        print("Done!")


class UserCsvIO:
    def __init__(self,filename):
        self.filename = filename
        self.dataset_of_user = []

    def read(self):
        csv_file = open(self.filename, encoding='utf-8')
        csv_reader = csv.DictReader(csv_file)  # reading csv like dictionary
        for row in csv_reader:
            self.dataset_of_user.append(dict(row))
        csv_file.close()

    def write(self):
        csv_file = open(self.filename, encoding='utf-8', mode='w')

        field_names = ['id', 'username', 'password']
        csv_writer = csv.DictWriter(csv_file, field_names=field_names)
        csv_writer.writeheader()
        for i in self.dataset_of_user:
            csv_writer.writerow(i)
