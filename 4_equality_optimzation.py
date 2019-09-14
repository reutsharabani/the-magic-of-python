a = [1, 2, 3]
b = [1, 2, 3]
assert a == b

x = float('nan')
xl = [x]
assert xl[0] == xl[0]  # AssertionError
assert xl == xl  # no AssertionError
