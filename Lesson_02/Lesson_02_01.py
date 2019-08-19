class Animal:
    name= None
    animal_type = None
    animals_created = 0
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        Animal.animals_created +=1

    def __del__(self):
        print("Instance is deleted from memory")

    def move(self):
        print("i'am moving")

    def eat(self):
        print("I'am eating")

    def sleep(self):
        print("I'am sleeping")

    def who_am_i(self):
        print("I'am the {0}.My type is {1}".format(self.name, self.animal_type))


animal_object = Animal("Human", "Mammal")
animal_object1 = Animal("Human", "Mammal")
#animal_object.name = "Human"
#animal_object.animal_type = "Mammal"
#animal_object.eat()
#animal_object.sleep()
#animal_object.move()
#animal_object.who_am_i()

print(Animal.animals_created)