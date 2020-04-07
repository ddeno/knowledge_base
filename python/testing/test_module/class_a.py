class ClassA():
    def __init__(self, **kwargs):
        self._a = 1
        self._b = 'foo'
        self._c = False
        self._d = {'a': 'bar', 'b': 'foo'}

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if isinstance(value, str):
            self._b = value
        else:
            raise TypeError()
