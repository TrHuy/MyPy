class Animal:
    name = ''
    age = 0

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def show(self):
        print('My name is ', self.name)

    def run(self):
        print('Animal is running...')

    def go(self):
        print('Animal is going...')




