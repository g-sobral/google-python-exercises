from math import sqrt

class Vector:

    # __slots__ = ['x', 'y']

    def __init__(self, x, y):
        super().__setattr__('x', x)
        super().__setattr__('y', y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __repr__(self):
        return ''.join(('Vector(', str(self.x), ', ', str(self.y), ')'))

    def __str__(self):
        return ''.join(('(', str(self.x), ', ', str(self.y), ')'))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __bool__(self):
        return not self.x == self.y == 0

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __setattr__(self, key, value):
        msg = "'%s' does not support attribute assignment" % (self.__class__)
        raise AttributeError(msg)

def main():
    assert Vector(2, 4)
    assert (Vector(2, 4).x, Vector(2, 4).y) == (2, 4)
    assert repr(Vector(2, 4)) == 'Vector(2, 4)'
    assert str(Vector(2, 4)) == '(2, 4)'
    assert Vector(2, 4) == Vector(2, 4)
    assert Vector(2, 4) + Vector(1, 2) == Vector(3, 6)
    assert Vector(2, 4) * 2 == Vector(4, 8)
    assert abs(Vector(3, 4)) == 5.0
    assert bool(Vector(0, 0)) == False
    assert bool(Vector(0, 1)) == bool(Vector(1, 0)) == bool(Vector(1, 1))
    assert Vector(2, 2).dot(Vector(3, 4)) == 14


if __name__ == '__main__':
    main()