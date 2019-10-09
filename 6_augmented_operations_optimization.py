def mutate_list_1(l, items):
    for item in items:
        l = l + [item] # does not mutate references of `l`
    return l


l1 = []
print("mutated 1: {}".format(mutate_list_1(l1, [1, 2, 3])))
print(f"original 1: {l1}")


def mutate_list_2(l, items):
    for item in items:
        l += [item]  # does not mutate references of `l`
    return l


l2 = []
print("mutated 2: {}".format(mutate_list_2(l2, [1, 2, 3])))
print(f"original 2: {l2}")

a = []
a.extend({1})
a += {1}
print(a)