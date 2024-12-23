class Parrot:

    #class atribute
    species = "bird"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#instantiate the parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 10)

#access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

#access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))