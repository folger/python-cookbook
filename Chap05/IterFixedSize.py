from functools import partial

RECODE_SIZE = 32

with open('somefile', 'rb') as f:
    recodes = iter(partial(f.read, RECODE_SIZE), b'')
    for r in recodes:
        print(r)
