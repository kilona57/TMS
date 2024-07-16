class Movie:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title == other.title

    def __hash__(self):
        return hash(self.title)

class Cinema:
    def __init__(self, name):
        self.name = name
        self.poster = set()

    def add_movie(self, movie):
        if movie in self.poster:
            print(f"Фильм '{movie.title}' уже есть в афише кинотеатра '{self.name}'.")
        else:
            self.poster.add(movie)
            print(f"Фильм '{movie.title}' добавлен в афишу кинотеатра '{self.name}'.")

    def remove_movie(self, movie_title):
        movie = Movie(movie_title)
        if movie in self.poster:
            self.poster.remove(movie)
            print(f"Фильм '{movie_title}' удален из афиши кинотеатра '{self.name}'.")
        else:
            print(f"Фильм '{movie_title}' не найден в афише кинотеатра '{self.name}'.")

    def __str__(self):
        movie_list = "\n".join([movie.title for movie in self.poster])
        return f"Кинотеатр '{self.name}' показывает следующие фильмы:\n{movie_list}"

def main():
    print("Добро пожаловать в систему управления кинотеатрами!")
    cinemas = []

    while True:
        print("\nДоступные команды:")
        print("1. Создать новый кинотеатр")
        print("2. Добавить фильм в афишу")
        print("3. Удалить фильм из афиши")
        print("4. Показать афишу кинотеатра")
        print("5. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            name = input("Введите название нового кинотеатра: ")
            cinema = Cinema(name)
            cinemas.append(cinema)
            print(f"Создан новый кинотеатр '{cinema.name}'.")
        elif choice == "2":
            if cinemas:
                for i, cinema in enumerate(cinemas, 1):
                    print(f"{i}. {cinema.name}")
                try:
                    cinema_choice = int(input("Выберите кинотеатр (1-{}): ".format(len(cinemas)))) - 1
                    if 0 <= cinema_choice < len(cinemas):
                        title = input("Введите название фильма: ")
                        movie = Movie(title)
                        cinemas[cinema_choice].add_movie(movie)
                    else:
                        print("Некорректный выбор кинотеатра.")
                except ValueError:
                    print("Некорректный ввод. Введите число.")
            else:
                print("Сначала создайте кинотеатр.")
        elif choice == "3":
            if cinemas:
                for i, cinema in enumerate(cinemas, 1):
                    print(f"{i}. {cinema.name}")
                try:
                    cinema_choice = int(input("Выберите кинотеатр (1-{}): ".format(len(cinemas)))) - 1
                    if 0 <= cinema_choice < len(cinemas):
                        title = input("Введите название фильма для удаления: ")
                        cinemas[cinema_choice].remove_movie(title)
                    else:
                        print("Некорректный выбор кинотеатра.")
                except ValueError:
                    print("Некорректный ввод. Введите число.")
            else:
                print("Сначала создайте кинотеатр.")
        elif choice == "4":
            if cinemas:
                for i, cinema in enumerate(cinemas, 1):
                    print(f"{i}. {cinema.name}")
                try:
                    cinema_choice = int(input("Выберите кинотеатр (1-{}): ".format(len(cinemas)))) - 1
                    if 0 <= cinema_choice < len(cinemas):
                        print(cinemas[cinema_choice])
                    else:
                        print("Некорректный выбор кинотеатра.")
                except ValueError:
                    print("Некорректный ввод. Введите число.")
            else:
                print("Сначала создайте кинотеатр.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Неверная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()