def count(n):
    while True:
        yield n
        n += 1

c = count(1)

import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

