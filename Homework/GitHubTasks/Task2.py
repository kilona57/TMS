class Kettle:
    def __init__(self, ml):
        self.ml = max(ml, 300)  # Минимальный объем чайника - 300ml

    def __repr__(self):
        levels = self.ml // 100
        remaining = self.ml % 100
        kettle_str = "|******************|\n"
        for i in range(levels):
            kettle_str += "|                  |**/\n"
            break
        if remaining == 0:
            kettle_str += "|                  |" + "*/" "\n"
            kettle_str += "|                  |" + "/" "\n"

        for i in range(levels - 3):
            kettle_str += "|                  |" + "\n"
        kettle_str += "|******************|"
        return kettle_str


# Пример использования
kettle = Kettle(ml=1100)
print(kettle)

kettle1 = Kettle(ml=300)
print(kettle1)