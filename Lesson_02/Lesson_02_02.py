class Automobile:

    _seats = 4
    _wheels = 4
    _engine = "V8"
    _electro = False
    _weight = 1200
    _acceleration = None




    def set_seats(self, seats):
        self._seats = seats

    def get_seats(self):
        return self._seats

    def get_wheels(self):
        return self._wheels

    def get_engine(self):
        return self._engine

    def get_electro(self):
        return self._electro

    def set_weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight

    def set_acceleration(self, acceleration):
        self._acceleration = acceleration

    def get_acceleration(self):
        return self._acceleration
    def beep(self):
        print("BEEP!")

class Bus(Automobile):

    _seats = 40
    _wheels = 6

    def beep(self):
        print("BEEP!BEEP!")



class Tesla(Automobile):
    set._weight = 1500
    set._acceleration = 7
    def beep(self):
        print("WHOOOOOM")
    def giveinfo(self):
        print(Tesla.get_wheels(), Tesla.get_seats(), Tesla.get_acceleration())

class Fura(Automobile):
    set._weight = 180000
    set._acceleration = 30

    def beep(self):
        print("DUUUUUUUU")

#auto = Automobile()

#print(auto.__class__)
#print(auto.get_seats())
#print(auto.get_wheels())
#auto.beep()

#bus = Bus()
#print(bus.__class__)
#print(bus.get_seats())
#print(bus.get_wheels())
#bus.beep()
#car = Automobile()

#car.set_seats(8)
#print(car.get_seats())

#print(Automobile._seats)