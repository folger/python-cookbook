def apply_sync(func, args, *, callback):
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

print('using class')
class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_sync(add, (2,3), callback=r.handler)
apply_sync(add, ('hello','world'), callback=r.handler)
print()

print('using closure')
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_sync(add, (2,3), callback=handler)
apply_sync(add, ('hello','world'), callback=handler)
print()

print('using coroutine')
def make_handler2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler2()
next(handler)
apply_sync(add, (2,3), callback=handler.send)
apply_sync(add, ('hello','world'), callback=handler.send)
print()

print('using partial function')
class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial
apply_sync(add, (2,3), callback=partial(handler, seq=seq))
apply_sync(add, ('hello','world'), callback=partial(handler, seq=seq))
print()

