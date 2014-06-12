class Pair(object):
    """"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pairy({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
print(repr(p))
print(p)
