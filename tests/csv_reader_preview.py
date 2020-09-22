from flix.adapters.repository import FlixRepository
import os

from flix.domainmodel.genre import Genre

f=FlixRepository("../flix/data/Data1000Movies.csv")

# for i in f.data.dataset_of_movie:
#     print(i.name)
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
lis=f.movie_filter(genre=[Genre("Sci-Fi")])
print(lis)