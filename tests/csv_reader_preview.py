from linvie.adapters.flix_repository import FlixRepository
import os

from linvie.domainmodel.genre import Genre

repo=FlixRepository("../linvie/data/Data1000Movies.csv")
search_list = repo.find("Hongchen Lin")
print(search_list)

# for i in f.data.dataset_of_actors:
#     print(i.name)
# for i in f.data.dataset_of_director:
#     print(i.name)
# for i in f.data.dataset_of_genre:
#     print(i.genre_name)

# r=f.find("Billy Ral")
# for i in r:
#     print(type(i),i.name)
# lis=f.movie_filter()
# print(len(lis)==len(f.data.dataset_of_movie))
# lis=f.movie_filter(genre=[Genre("Sci-Fi")])
# print(lis)