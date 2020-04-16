from copy import deepcopy


class Prototyp:
    def __init__(self):
        self.obiekty = {}

    def zarejestruj_obiekt(self, nazwa, obj):
        self.obiekty[nazwa] = obj

    def wyrejestruj_obiekt(self, nazwa):
        del self.obiekty[nazwa]

    def sklonuj_obiekt(self, nazwa, **attr):
        obj = deepcopy(self.obiekty[nazwa])
        obj.__dict__.update(attr)
        return obj