class Store:
    _name = None
    _realised = 0
    _realisedsumm = 0

    def __init__(self, name,):
        self._name = name

    def set_name(self, name):
         self._name = name

    def get_name(self):
        return self._name

    def set_realised(self, realised):
        self._realised = realised

    def get_realised(self):
        return self._realised

    def sell(self):
        self._realised +=1
        Store._realisedsumm += 1

    def seesumm(self):

        print(format.self._realised)

        print(self.get_realisedsumm)


metro = Store("METPO")
metro.sell()
metro.seesumm()

ashan = Store("ASHAN")
ashan.sell()
ashan.seesumm()

