list_of_lists = [[1, 2], [3, 4]]
print(sum(list_of_lists, []))


def flatten_with_sum(ll):
    return sum(ll, [])


def time_flattening(flat_func, sublists_count):
    return flat_func([[1]] * sublists_count)


counts = (10, 100, 1000)


for count in counts:
    import timeit
    t = timeit.timeit('time_flattening(flatten_with_sum, count)',
                      setup="from __main__ import time_flattening,"
                            "flatten_with_sum, count", number=1000)
    print('flattening of %d sublists took %f seconds' % (count, t))


def flatten_standard(ll):
    from itertools import chain
    return list(chain.from_iterable(ll))


for count in counts:
    import timeit
    t = timeit.timeit('time_flattening(flatten_standard, count)',
                      setup="from __main__ import time_flattening,"
                            "flatten_standard, count", number=1000)
    print('flattening of %d sublists took %f seconds' % (count, t))

