class Kolobok:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.rank_value = self.get_rank_value()

    def get_rank_value(self):
        if self.rank == "старлей":
            return 1
        elif self.rank == "капитан":
            return 2
        elif self.rank == "генерал":
            return 3
        else:
            return 0

class Investigation:
    def __init__(self, complexity):
        self.complexity = complexity
        self.status = "not started"
        self.investigators = []

    def add_investigator(self, investigator):
        self.investigators.append(investigator)
        self.update_status()

    def remove_investigator(self, investigator):
        if investigator in self.investigators:
            self.investigators.remove(investigator)
            self.update_status()

    def update_status(self):
        total_rank_value = sum(inv.rank_value for inv in self.investigators)
        if not self.investigators:
            self.status = "not started"
        elif total_rank_value >= self.complexity:
            self.status = "solved"
        else:
            self.status = "in progress"

    def __str__(self):
        return f"Complexity: {self.complexity}, Status: {self.status}, Investigators: {', '.join(inv.name for inv in self.investigators)}"

def main():
    investigators = []
    investigations = []

    while True:
        print("\nМеню:")
        print("1. Добавить следователя")
        print("2. Добавить расследование")
        print("3. Добавить следователя к расследованию")
        print("4. Удалить следователя из расследования")
        print("5. Просмотреть состояние расследований")
        print("6. Просмотреть имеющихся следователей")
        print("7. Выйти")

        choice = input("Введите номер: ")

        if choice == "1":
            name = input("Введите имя следователя: ")
            rank = input("Введите звание следователя (старлей, капитан, генерал): ")
            if rank not in ["старлей", "капитан", "генерал"]:
                print("Неверное звание. Попробуйте еще раз.")
                continue
            investigator = Kolobok(name, rank)
            investigators.append(investigator)
            print(f"Добавлен следователь: {investigator.name} ({investigator.rank})")

        elif choice == "2":
            complexity = int(input("Введите сложность расследования (0-300): "))
            investigation = Investigation(complexity)
            investigations.append(investigation)
            print(f"Добавлено расследование со сложностью {complexity}")

        elif choice == "3":
            if not investigations:
                print("Нет активных расследований.")
            else:
                print("Список расследований:")
                for i, investigation in enumerate(investigations):
                    print(f"{i+1}. {investigation}")
                investigation_index = int(input("Выберите расследование (1-{}):" .format(len(investigations)))) - 1
                if 0 <= investigation_index < len(investigations):
                    print("Список следователей:")
                    for i, investigator in enumerate(investigators):
                        print(f"{i+1}. {investigator.name} ({investigator.rank})")
                    investigator_index = int(input("Выберите следователя (1-{}):".format(len(investigators)))) - 1
                    if 0 <= investigator_index < len(investigators):
                        investigations[investigation_index].add_investigator(investigators[investigator_index])
                        print(f"Следователь {investigators[investigator_index].name} добавлен к расследованию.")
                    else:
                        print("Неверный выбор следователя.")
                else:
                    print("Неверный выбор расследования.")

        elif choice == "4":
            if not investigations:
                print("Нет активных расследований.")
            else:
                print("Список расследований:")
                for i, investigation in enumerate(investigations):
                    print(f"{i+1}. {investigation}")
                investigation_index = int(input("Выберите расследование (1-{}):" .format(len(investigations)))) - 1
                if 0 <= investigation_index < len(investigations):
                    print("Список следователей:")
                    for i, investigator in enumerate(investigations[investigation_index].investigators):
                        print(f"{i+1}. {investigator.name} ({investigator.rank})")
                    investigator_index = int(input("Выберите следователя (1-{}):".format(len(investigations[investigation_index].investigators)))) - 1
                    if 0 <= investigator_index < len(investigations[investigation_index].investigators):
                        investigations[investigation_index].remove_investigator(investigations[investigation_index].investigators[investigator_index])
                        print(f"Следователь {investigations[investigation_index].investigators[investigator_index].name} удален из расследования.")
                    else:
                        print("Неверный выбор следователя.")
                else:
                    print("Неверный выбор расследования.")

        elif choice == "5":
            if not investigations:
                print("Нет активных расследований.")
            else:
                print("Состояние расследований:")
                for investigation in investigations:
                    print(investigation)

        elif choice == "6":
            if not investigators:
                print("Нет добавленных следователей.")
            else:
                print("Список следователей:")
                for investigator in investigators:
                    print(f"{investigator.name} ({investigator.rank})")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()