from flix.domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.watch_list=[]

    def add_movie(self,movie):
        if type(movie) is Movie:
            if movie not in self.watch_list:
                self.watch_list.append(movie)

    def remove_movie(self,movie):
        try:
            self.watch_list.remove(movie)
        except:
            return

    def select_movie_to_watch(self,index):
        try:
            return self.watch_list[index]
        except:
            return None

    def size(self):
        return len(self.watch_list)

    def first_movie_in_watchlist(self):
        return self.select_movie_to_watch(0)

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<len(self.watch_list):
            self.n+=1
            return self.select_movie_to_watch(self.n-1)
        else:
            raise StopIteration