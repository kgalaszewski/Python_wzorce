from typing import NamedTuple

class Samochod(NamedTuple):
    rejestracja: int
    name: str = ''

class BudowniczySamochodu(object):
    def __init__(self, port):
        self.rejestracja = port
        self.name = "toyota"

    def build(self):
        print("zbudowano samochod : ", self.rejestracja, " o nazwie ", self.name)
        return Samochod(self.rejestracja, self.name)

b = BudowniczySamochodu(123123123)
b.protocol = 'UDP'
b.build()