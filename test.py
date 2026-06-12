
class Remember:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return f"Remember({self.value})"

    value = property(lambda self: self._value, lambda self, value: setattr(self, '_value', value))
