class Zdjecie:
    def __init__(self, filename):
        self._filename = filename

    def zaladuj_zdjecie(self):
        print("loading " + self._filename)

    def wyswietl_zdjecie(self):
        print("display " + self._filename)


class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxystate = None


class ProxyZdjecie(Proxy):
    def display_image(self):
        if self._proxystate == None:
            self._subject.wyswietl_zdjecie()
            self._proxystate = 1
        print("display " + self._subject._filename)

proxy_image1 = ProxyZdjecie(Zdjecie("Sciezka_Zdj1"))
proxy_image2 = ProxyZdjecie(Zdjecie("Sciezka_Zdj2"))