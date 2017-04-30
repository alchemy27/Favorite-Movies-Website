import media #importing from the
import fresh_tomatoes

''' Each of the six movies below will store the movies' name, description,
picture, and trailer url. They are the objects to be instantiated with
their own properties.'''

inception = media.Movie("Inception",
                        "Secret missions that takes place in the mind",
                        "https://i.ytimg.com/vi_webp/E1iqGiX0lSg/movieposter.webp", # noqa
                        "https://www.youtube.com/watch?v=E1iqGiX0lSg") # noqa

interstellar = media.Movie("Interstellar",
                           "Exploring space for another shot at human survival",
                           "https://i.ytimg.com/vi_webp/Df7IEKqimOY/movieposter.webp", # noqa
                           "https://www.youtube.com/watch?v=Df7IEKqimOY") # noqa

the_martian = media.Movie("The Martian",
                          "A lone human alive on Mars trying to survive to the point to get rescued",
                          "https://i.ytimg.com/vi_webp/TeZDLAaDYos/movieposter.webp", # no qa
                          "https://www.youtube.com/watch?v=TeZDLAaDYos") # noqa

spirited_away = media.Movie("Spirited Away",
                            "A girl that was trapped in another dimension",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcS6MveoDoJOg9-wMvtHE4ak_-HDZeYS1egb9PwRcf8lhrtcppMc", # noqa
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk") # noqa

the_maze_runner = media.Movie("The Maze Runner",
                              "A group of people trapped within a dungeon trying to get out",
                              "https://i.ytimg.com/vi_webp/TwA8ea_XqkM/movieposter.webp", # noqa
                              "https://www.youtube.com/watch?v=TwA8ea_XqkM") # noqa

jurassic_world = media.Movie("Jurassic World",
                             "Humans against dinosaurs",
                             "https://i.ytimg.com/vi_webp/e6d0VF3TCiQ/movieposter.webp", # noqa
                             "https://www.youtube.com/watch?v=e6d0VF3TCiQ") # noqa

''' This puts all the movies into a list, which will be easier to pass in
later.'''
movies = [inception, interstellar, the_martian,
          spirited_away, the_maze_runner, jurassic_world]

fresh_tomatoes.open_movies_page(movies)
