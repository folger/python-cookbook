from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(4)
d2['a'].add(5)
d2['a'].add(1)

print(d)
print(d2)
