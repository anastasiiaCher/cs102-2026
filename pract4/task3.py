def make_counter():
    i = 0

    def inside_counter():
        nonlocal i
        i += 1
        return i

    return inside_counter


counter = make_counter()
for a in range (0, 50):
    print(counter())