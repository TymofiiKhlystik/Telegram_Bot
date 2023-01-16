from Music import roc, rep, pop, all_music
import Movie
from guess_the_number import game
import books


def menu_bot():
    while True:
        print("1 - Музика \n"
              "2 - Фільми \n"
              "3 - Гра відгадай число \n"
              "4 - Книги")
        arg = input("Введіть цифру")
        if arg == "1":
            # Import Music
            while True:
                print("""
                1 - Pop
                2 - Rep
                3 - Roc
                4 - Показати всю музику
                0 - Повернутися назад
                """)
                music = input("Виберіть цифру")
                if music == "1":
                    print(pop)
                elif music == "2":
                    print(rep)
                elif music == "3":
                    print(roc)
                elif music == "4":
                    for i in all_music:
                        print(i)
                elif music == "0":
                    break
                else:
                    print("Введіть коректне значення")
        elif arg == "2":
            # Import Movie
            while True:
                print("""
                Рекомендації по філмах
                Виберіть жанр 
                1 - Фантастика 
                2 - Комедії
                3 - Пригоди
                4 - Екшен
                0 - Повернутися назад
                """)
                film = input("Введіть цифру")
                if film == "1":
                    print(Movie.fantasy)
                elif film == "2":
                    print(Movie.comedies)
                elif film == "3":
                    print(Movie.adventures)
                elif film == "4":
                    print(Movie.action)
                elif film == "0":
                    break
                else:
                    print("Введіть коректне значення")
        elif arg == "3":
            # Import guess_the_number
            game()
        elif arg == "4":
            for i in books.book:
                print(i)


menu_bot()
