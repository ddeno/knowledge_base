class ClassB():
    def __init__(self, **kwargs):
        self._a = 2
        self._b = 'bar'
        self._c = True
        self._d = {'a': 'foo', 'b': 'bar'}

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if isinstance(value, int):
            self._a = value
        else:
            raise TypeError()
