def is_even(x):
    return x % 2 == 0


x = 3

parity_str = ('odd', 'even')[is_even(x)]

print('x is %s' % parity_str)
