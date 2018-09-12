class Dog(Animal):
    def run(self):
        print('Dog is running...')


myanimal = Animal
myanimal.show()
myanimal.run()
myanimal.go()


mydog = dog('Lucy')
mydog.show()
mydog.run()
mydog.go()
