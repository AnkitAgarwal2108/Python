class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

        # Sample Method

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Jon Doe')
p.say_hi()