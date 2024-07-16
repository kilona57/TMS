class RealStr:
    def __init__(self, string):
        self.string = string
    def __len__(self):
        return len(self.string)
    def __eq__(self, other):
        if isinstance(other, RealStr):
            return len(self) == len(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, RealStr):
            return len(self) != len(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RealStr):
            return len(self) < len(other)
        else:
            NotImplemented

    def __gt__(self, other):
        if isinstance(other, RealStr):
            return len(self) > len(other)
        else:
            NotImplemented

    def __le__(self, other):
        if isinstance(other, RealStr):
            return len(self) <= len(other)
        else:
            NotImplemented

    def __ge__(self, other):
        if isinstance(other,RealStr):
            return len(self) >= len(other)
        else:
            NotImplemented

    def compare(self, other):
        if self == other:
            print(f'Строка "{self.string}" больше строки "{other.string}"')
        elif self < other:
            print(f'Строка "{self.string}" меньше строки "{other.string}"')
        else:
            print(f'Строка "{self.string}" больше строки "{other.string}"')
def get_strings():
    strings = []
    while True:
        string = input("Введите строку (или нажмите Enter, чтобы завершить): ")
        if not string:
            break

        strings.append(RealStr(string))
    return strings

def compare_strings(strings):
    print("Введите строки:")
    for i, s in enumerate(strings):
            print(f'{i+1}.{s.string}')
    while True:
        index1 = int(input("Введите номер первой строки для сравнения (или 0, чтобы выйти): "))
        if index1 == 0:
            break

        index2 = int(input("Введите номер второй строки для сравнения: "))

        if index1 < 1 or index1 > len(strings) or index2 < 1 or index2 > len(strings):
            print("Некорректные номера строк.")
            continue

        str1 = strings[index1 - 1]
        str2 = strings[index2 - 1]

        str1.compare(str2)


strings = get_strings()
compare_strings(strings)