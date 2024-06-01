a = [1, 3, 5, 7, 9]


def iadd(o, v):
    try:
        return o.__iadd__(v)
    except AttributeError:
        return o.__add__(v)


_a_iter = iter(enumerate(a))
while True:
    try:
        index, i = next(_a_iter)
    except StopIteration:
        break
    a.__setitem__(index, iadd(a.__getitem__(index), 1))

print(a)

# https://softwareengineering.stackexchange.com/questions/341179/why-does-python-only-make-a-copy-of-the-individual-element-when-iterating-a-list
