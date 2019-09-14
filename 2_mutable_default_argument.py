def sort_into(source, target=[]):
    for item in sorted(source):
        target.append(item)
    return target


r1 = sorted_list = sort_into([2, 3, 1])
print(r1)  # [1, 2, 3]
r2 = sort_into([1, 2, 3])
print(r2)  # [1, 2, 3, 1, 2, 3]

r2.clear()
r2.append('sorcery')
r2 = sort_into([1, 2, 3])
print(r2)  # ['sorcery', 1, 2, 3]

print(r2 is r1)  # True


def sort_into(source, target=None):
    # target = target or [] # would break API with empty lists
    target = [] if target is None else target  # new list every call
    for item in sorted(source):
        target.append(item)
    return target


r1 = sort_into([2, 3, 1])
print(r1)  # [1, 2, 3]
r2 = sort_into([1, 2, 3])
print(r2)  # [1, 2, 3]

r2.clear()
r2.append('sorcery')
r2 = sort_into([1, 2, 3])
print(r2)  # [1, 2, 3]

print(r2 is r1)  # False
