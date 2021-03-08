class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #These are attributes



    def sit(self):
        print("This is {}, and I'm sitting down here".format(self.name))

    def set_name(self, name):
        self.name = name
     #Both of thses functions are methods as they are in a class
    #If i define this functions outside the class, the attributes/objects will not work with them
    #def rollover(self):


ares = Dog('ares', 10)
print(ares)
toby = Dog('Toby', 21)
print(toby)
#ares.name = "trueno"
ares.set_name("trueno")
ares.age = 1
ares = toby
black = Dog('toby', 21)
black.name = 'troy'
print("toby is ares")