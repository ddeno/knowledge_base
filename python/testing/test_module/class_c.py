class ClassC():
    def __init__(self, **kwargs):
        self._a = 3
        self._b = 'foobar'
        self._c = None
        self._d = {'a': True, 'b': 123}

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        if isinstance(value, dict):
            self._d = value
        else:
            raise TypeError()
