"""with class method"""
class movie:
    def __init__(self,name,rating,genre,views):
        self.name = name
        self.rating = rating
        self.genre = genre
        self.views = views

    @staticmethod
    def sort_by_name(movies):
        return sorted(movies,key = lambda x: x.name)

    @staticmethod
    def sort_by_rating(movies):
        return sorted(movies,key = lambda x: x.rating,reverse=True)

    @staticmethod
    def sort_by_genre(movies):
        return sorted(movies,key = lambda x: x.genre)

    @staticmethod
    def sort_by_views(views):
        return sorted(movies,key = lambda x: x.views,reverse=True)


movies = [movie(  'Barbie',  4.5, 'Comedy',  1.500000 ),
        movie( 'Interstellar',  3,  'SiFi',  4.500000),
	       movie (  'The Godfather',  9.77,  'Crime',  12.000000)]


while True:
    print("wellcome\nto list movies by title press 1\nto list movies by rating press 2\nto list movies by genre press 3"
          "\nto list movies by views press 4\nto quit press 5")
    choice = input('enter the number of the operation you wnant to perform: ')

    if choice == '1':
        sorted_by_n = movie.sort_by_name(movies)
        for movie in sorted_by_n:
            print(f"{movie.name}:({movie.rating},{movie.genre},{movie.views})")

    if choice == '2':
        sorted_by_r = movie.sort_by_rating(movies)
        for movie in sorted_by_r:
            print(f"{movie.name}:({movie.rating},{movie.genre},{movie.views})")

    if choice == '3':
        sorted_by_g = movie.sort_by_genre(movies)
        for movie in sorted_by_g:
            print(f"{movie.name}:({movie.rating},{movie.genre},{movie.views})")

    if choice == '4':
        sorted_by_n = movie.sort_by_genre(movies)
        for movie in sorted_by_g:
            print(f"{movie.name}:({movie.rating},{movie.genre},{movie.views})")

    if choice == '5':
        print('quitting')
        break


# movies = [{ "movieName": 'Barbie', "rating": 4.5, "genre": 'Comedy', "views": 1.500000 },
#             { "movieName": 'Interstellar', "rating": 3, "genre": 'Fantastic', "views": 4.500000},
# 	        { "movieName": 'The Godfather', "rating": 9.77, "genre": 'Crime', "views": 12.000000}
#           ]
# """the easy way"""
# def sort_by_name(it):
#     return it['movieName']
# def sort_by_rating(it):
#     return it["rating"]
# def sort_by_genre(it):
#     return it["genre"]
# def sort_by_views(it):
#     return it["views"]
#
#
# def byname():
#     movies.sort(key=sort_by_name)
#     for i in movies:
#         print(i)
# def byrating():
#     movies.sort(key=sort_by_rating, reverse=True)
#     for i in movies:
#         print(i)
# def bygenre():
#     movies.sort(key=sort_by_genre)
#     for i in movies:
#         print(i)
# def byviews():
#     movies.sort(key=sort_by_views, reverse=True)
#     for i in movies:
#         print(i)
#
# while True:
#     print("wellcome\nto list movies by title press 1\nto list movies by rating press 2\nto list movies by genre press 3"
#           "\nto list movies by views press 4\nto quit press 5")
#     choice = input('enter the number of the operation you wnant to perform: ')
#
#     if choice == '1':
#         byname()
#     if choice == '2':
#         byrating()
#     if choice == '3':
#         bygenre()
#     if choice == '4':
#         byviews()
#     if choice == '5':
#         print('quitting')
#         break


