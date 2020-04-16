from datetime import datetime

def uruchom_pomiedzy_godzinami(_from=7, _to=22):
    def dekorator(func):
        def wrapper():
            if _from <= datetime.now().hour < _to:
                func()
            else:
                pass
        return wrapper
    return dekorator

@uruchom_pomiedzy_godzinami(20,  23)
def powiedz_cos():
    print("Dekorator wzorzec")

powiedz_cos()