class CountDown(object):
    """docstring for CountDown"""
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        print('__reversed__ is invoked')
        n = 1
        while n <= self._start:
            yield n
            n += 1


cd = CountDown(10)
print(next(iter(cd)))
print(list(cd))
print(list(reversed(cd)))
