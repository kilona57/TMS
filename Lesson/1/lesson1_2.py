a = 17 / 2 * 3 + 2
b = 2 + 17 / 2 * 3
c = 19 % 4 + 15 / 2 * 3
d = (15 + 6) - 10 * 4 
e = 17 / 2 % 2 * 3 ** 3

a_2 = (((17 / 2) * 3) + 2)
b_2 = (2 + ((17 / 2) * 3))
c_2 = ((19 % 4) + ((15 / 2) * 3))
d_2 = ((15 + 6) - (10 * 4)) 
e_2 = (((17 / 2) % 2) * (3 ** 3))

assert a == a_2
assert b == b_2
assert c == c_2
assert d == d_2
assert e == e_2
