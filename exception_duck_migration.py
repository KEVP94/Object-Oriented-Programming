import polymorphism_ducks

flock = polymorphism_ducks.Flock()
donald = polymorphism_ducks.Duck()
daisy = polymorphism_ducks.Duck()
duck1 = polymorphism_ducks.Duck()
duck2 = polymorphism_ducks.Duck()
duck3 = polymorphism_ducks.Duck()
duck4 = polymorphism_ducks.Duck()
duck5 = polymorphism_ducks.Duck()
percy = polymorphism_ducks.Mallard()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
flock.add_duck(duck5)


flock.migrate()