x = 1
# ...
assert x is 1

x = 10
assert x is 10  # OK


# if you compile the entire file it will not throw the assertion error
# because the reader uses the same `1000`, to solve this I've added a second
# part where it doesn't optimize it
x = 1000
assert x is 1000  # only works if evaluated separately
# always works
x = 999
assert (x + 1) is 1000  # AssertionError :(

