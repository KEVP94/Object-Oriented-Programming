class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("WHEE! This is fun.")
        elif self.ratio == 1:
            print("Damn this is hard work.")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, Waddle Waddle")

    def swim(self):
        print("Come on in! The water is lovely")

    def quack(self):
        print("Quack! Quack! Quack!")

    def fly(self):  # this is where polymorphism and composition are being used
        self._wing.fly()


class Penguin(object):

    def __init__(self):  # created new data attribute, called fly and assigned to reference aviate method 
        self.fly = self.aviate

    def walk(self):
        print("Waddle, Waddle! i Waddle too.")

    def swim(self):
        print("Come on in! But its a bit chilly this far south.")

    def quack(self):
        print("Are you having a laugh? I am a penguin.")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):  # A subclass of duck
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # this parameter is being annotated.  After semicolon is the type and shows the type of the parameter
        fly_method = getattr(duck, 'fly', None)  # this checks objects dict'y 4 specified attribute. Better test
        # if isinstance(duck, Duck):  # this is test to check if object is a duck
        if callable(fly_method):  # Better test
            self.flock.append(duck)
        else:
            raise TypeError("Can't add duck, are you sure its not a" + str(type(duck).__name__))  # exception raised

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One assumed duck down")
                problem = e
                # raise
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    danald.fly()
