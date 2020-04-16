class Mediator:
    def __init__(self):
        self._cosTakiego1 = CosTakiego1(self)
        self._cosTakiego2 = CosTakiego2(self)


class CosTakiego1:
    def __init__(self, mediator):
        self._mediator = mediator


class CosTakiego2:
    def __init__(self, mediator):
        self._mediator = mediator