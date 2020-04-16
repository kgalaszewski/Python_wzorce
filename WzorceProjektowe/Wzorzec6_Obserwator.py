import threading
import time
import pdb


class Pobieracz(threading.Thread):
    def run(self):
        print('sprawdzanie')
        for i in range(1, 5):
            self.i = i
            time.sleep(2)
            print('dziala')


class Pracownik(threading.Thread):
    def run(self):
        for i in range(1, 5):
            print('instancja pracownika dziala : %i (%i)' % (i, t.i))
            time.sleep(1)
            t.join()


t = Pobieracz()
t.start()

time.sleep(1)

i1 = Pracownik()
i1.start()

i2 = Pracownik()
i2.start()

i3 = Pracownik()
i3.start()
