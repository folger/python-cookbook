items = ['a', 'b', 'c']

from itertools import permutations
print('permutations')
for p in permutations(items):
    print(p)
for p in permutations(items, 2):
    print(p)

print('combinations')
from itertools import combinations
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)
for c in combinations(items, 1):
    print(c)

print('combinations_with_replacement')
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
