class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instanc

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Blad, to jest singleton")
        else:
            Singleton.__instance = self