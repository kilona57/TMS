import time

class SwimmingPool:
    def __init__(self, meters):
        if meters < 100:
            raise ValueError("Строители не берутся строить бассейн длиной менее 100 метров.")
        self.meters = meters

    def __str__(self):
        pool_length = self.meters
        pool_symbol = "="
        pool_display = pool_symbol * (pool_length // 10)
        return pool_display

class Swimmer:
    def __init__(self, speed):
        self.speed = speed

    def to_swim(self, pool, distance):
        print(f"Пловец начинает плыть {distance} метров.")
        pool_length = pool.meters
        pool_symbol = "*"
        pool_display = list(str(pool))

        # Анимация в прямом направлении
        for i in range(distance // 10):
            pool_display[i] = pool_symbol
            print("".join(pool_display))
            time.sleep(0.5)
            pool_display[i] = "="

        # Анимация в обратном направлении
        for i in range(distance // 10 - 2, -1, -1):
            pool_display[i] = pool_symbol
            print("".join(pool_display))
            time.sleep(0.5)
            pool_display[i] = "="

        print("Пловец достиг исходной точки.")

# Пример использования
spool = SwimmingPool(meters=110)
print(spool)

swimmer = Swimmer(speed=1.5)  # скорость 1.5 м/с
swimmer.to_swim(spool, 50)
