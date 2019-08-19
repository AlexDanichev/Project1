class Dec1:

    def __init__(self, f):
        self._f = f

    def __call__(self, *args, **kwargs):
        print("START DECORATING")
        self._f()
        print("END DEOCRATING")



@Dec1
def hi():
    print("SAY HELLO!")

