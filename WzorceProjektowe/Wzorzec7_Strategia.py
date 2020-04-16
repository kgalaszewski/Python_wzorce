import types

class Strategia:
   def __init__(self, func = None):
      self.name = 'Podstawowa nazwa'
      if func is not None:
         self.execute = types.MethodType(func, self)

   def execute(self):
      print(self.name)

def execute_wersja1(self):
   print("wersja 1", self.name)

def execute_wersja2(self):
   print("wersja 2", self.name)

if __name__ == '__main__':
   strat0 = Strategia()
   strat1 = Strategia(execute_wersja1)
   strat1.name = 'nazwa 1'
   strat2 = Strategia(execute_wersja2)
   strat2.name = 'nazwa 2'
   strat0.execute()
   strat1.execute()
   strat2.execute()