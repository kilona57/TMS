class Child:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

    def take_my_hand(self, other_child):
        if self.next is None:
            self.next = other_child
            other_child.prev = self
            other_child.next = self
            self.prev = other_child
        else:
            last_child = self
            while last_child.next != self:
                last_child = last_child.next
            last_child.next = other_child
            other_child.prev = last_child
            other_child.next = self
            self.prev = other_child

    def __str__(self):
        return self.name

def create_child():
    name = input("Введите имя ребенка: ")
    return Child(name)

def add_to_circle(circle, child):
    if not circle:
        return child
    else:
        circle.take_my_hand(child)
        return circle

def print_circle(circle):
    if not circle:
        print("Хоровод пуст.")
    else:
        current = circle
        while True:
            print(current, end=" -> ")
            current = current.next
            if current == circle:
                break

def print_child_info(child):
    print(f"Имя: {child.name}")
    print(f"Предыдущий ребенок: {child.prev.name}")
    print(f"Следующий ребенок: {child.next.name}")

def main():
    circle = None
    while True:
        print("\nДействия:")
        print("1. Добавить ребенка в хоровод")
        print("2. Вывести текущий хоровод")
        print("3. Посмотреть информацию о ребенке")
        print("4. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            child = create_child()
            circle = add_to_circle(circle, child)
            print(f"Ребенок {child.name} добавлен в хоровод.")
        elif choice == "2":
            print("Текущий хоровод:")
            print_circle(circle)
        elif choice == "3":
            if not circle:
                print("Хоровод пуст.")
            else:
                child_name = input("Введите имя ребенка, о котором хотите получить информацию: ")
                current = circle
                while current.name != child_name:
                    current = current.next
                    if current == circle:
                        print("Ребенок не найден в хороводе.")
                        break
                else:
                    print_child_info(current)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()