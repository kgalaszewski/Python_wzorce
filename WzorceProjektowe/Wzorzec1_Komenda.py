def demo(a, b, c):
    print(a)
    print(b)
    print(c)


class Command:
    def __init__(self, cmd, *args):
        self._cmd = cmd
        self._args = args

    def __call__(self, *args):
        return print("Wywoluje komende : ", self._cmd, " ", self._args + args)

cmd = Command(demo, 1, 2)
print(cmd.__call__())
