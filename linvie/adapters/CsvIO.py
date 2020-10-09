import csv
from abc import ABC, abstractmethod

from linvie.domainmodel.Comment import Comment
from linvie.domainmodel.Genre import Genre
from linvie.domainmodel.Movie import Movie
from linvie.domainmodel.People import People
from linvie.domainmodel.User import User


class AbstractCsvIO(ABC):

    @abstractmethod
    def read(self):
        raise NotImplementedError


class CsvIO(AbstractCsvIO):
    def __init__(self, movie_file_path, user_file_path, comment_file_path):
        self.movie_file_path = movie_file_path
        self.user_file_path = user_file_path
        self.comment_file_path = comment_file_path
        self.dataset_of_movie = []
        self.dataset_of_people = []
        self.dataset_of_director = []
        self.dataset_of_actors = []
        self.dataset_of_genre = {}
        self.dataset_of_user = []
        self.dataset_of_comment = []

    def read(self):
        self.read_movie_file()
        self.read_user_file()
        self.read_comment_file()

    def read_movie_file(self):
        csv_file = open(self.movie_file_path, encoding='utf-8')
        csv_reader = csv.DictReader(csv_file)  # reading csv like dictionary

        for row in csv_reader:
            # a row with dictionary form
            temp = dict(row)

            # movie
            movie = Movie(temp['id'], temp['Title'], temp['Year'])
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

        for person in self.dataset_of_people:
            if person.if_is_director():
                self.dataset_of_director.append(person)
            if person.if_is_actor():
                self.dataset_of_actors.append(person)

    def read_user_file(self):
        self.dataset_of_user = []
        csv_file = open(self.user_file_path, encoding='utf-8')
        csv_reader = csv.DictReader(csv_file)  # reading csv like dictionary
        for row in csv_reader:
            temp = dict(row)
            user = User(temp['id'], temp['username'], temp['password'])
            for movie_id in temp['favorite'].split(","):
                if movie_id:
                    user.like(self.dataset_of_movie[int(movie_id)])
            self.dataset_of_user.append(user)
        csv_file.close()

    def read_comment_file(self):
        self.dataset_of_comment = []
        csv_file = open(self.comment_file_path, encoding='utf-8')
        csv_reader = csv.DictReader(csv_file)  # reading csv like dictionary
        for row in csv_reader:
            temp = dict(row)
            comment = Comment(temp['id'], temp['user-id'], temp['movie-id'], temp['comment-text'], temp['time'])
            comment.user = self.dataset_of_user[int(comment.user_id)]
            comment.movie = self.dataset_of_movie[int(comment.movie_id)]
            self.dataset_of_comment.append(comment)
            self.dataset_of_user[int(comment.user_id)].add_comment(comment)
            self.dataset_of_movie[int(comment.movie_id)].add_comment(comment)
        csv_file.close()

    def write_user(self):
        csv_file = open(self.user_file_path, encoding='utf-8', mode='w', newline='')
        field_names = ['id', 'username', 'password', 'favorite']
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        csv_writer.writeheader()
        for user in self.dataset_of_user:
            csv_writer.writerow({'id': user.ID, 'username': user.name, 'password': user.password,
                                 "favorite": ",".join([i.ID for i in user.favorite])})
        csv_file.close()

    def write_comment(self):
        csv_file = open(self.comment_file_path, encoding='utf-8', mode='w', newline='')
        field_names = ['id', 'user-id', 'movie-id', 'comment-text', 'time']
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        csv_writer.writeheader()
        for com in self.dataset_of_comment:
            csv_writer.writerow(
                {'id': com.ID, 'user-id': com.user_id, 'movie-id': com.movie_id, 'comment-text': com.comment_text,
                 'time': com.time})
        csv_file.close()
