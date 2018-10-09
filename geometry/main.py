import mina_math

a_x = 0
a_y = 7
a = a_x, a_y
b_x = 5
b_y = 2
b = b_x, b_y
c_x = 1
c_y = -2
c = c_x, c_y

print(f'slope of {a}, {b} is ' + str(mina_math.slope(a_x, a_y, b_x, b_y)))
print(f'slope of {b}, {c} is ' + str(mina_math.slope(b_x, b_y, c_x, c_y)))
print(f'distance of {a}, {b} is ' + str(mina_math.distance(a_x, a_y, b_x, b_y)))
print(f'distance of {b}, {c} is ' + str(mina_math.distance(b_x, b_y, c_x, c_y)))
