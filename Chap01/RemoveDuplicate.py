def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ 1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
