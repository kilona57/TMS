"""Дан прямоугольный треугольник с катетами cat_a и
cat_b. Найти площадь треугольника и его гипотенузу"""

cat_a = 3
cat_b = 15

gipotinize = (((cat_a ** 2) + (cat_b ** 2))) ** 0.5
s = ((cat_a * cat_b) / 2)

print(gipotinize, s, sep = '\n')