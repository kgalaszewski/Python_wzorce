class StworzPosilek:
    def przygotuj(self): pass
    def ugotuj(self): pass
    def zjedz(self): pass
    def start(self):
        self.przygotuj()
        self.ugotuj()
        self.zjedz()


class StworzPizze(StworzPosilek):
    def przygotuj(self):
        print("Przygotuj Pizze")

    def ugotuj(self):
        print("Ugotuj Pizze")

    def zjedz(self):
        print("Zjedz")


class StworzNalesniki(StworzPosilek):
    def przygotuj(self):
        print("Przygotuj Nalesniki")

    def ugotuj(self):
        print("Ugotuj Nalesniki")

    def zjedz(self):
        print("Zjedz")


stworzPizze = StworzPizze()
stworzPizze.start()

stworzNalesniki = StworzNalesniki()
stworzNalesniki.start()