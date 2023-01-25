def add(*args):
    print(f"\nargs: {args} of type {type(args)}")
    total = 0;
    for arg in args:
        total += arg
    print(f"sum : {total}")

def calculate(n , **kwarks):
    print(f"\nargs: number {n} and {kwarks} of type {type(kwarks)}")
    print(f"{n} + {kwarks['add']} = {n + kwarks['add']}")
    print(f"{n} * {kwarks['multiply']} = {n * kwarks['multiply']}")

add(1,2)
add(1,2,3)
add(1,2,3,4)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, make="Citroen", model="C5", color="gray", **kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
        self.model=kw.get("color")
    def __init__(self, make="Citroen", model="C5", color="gray"):
        self.make=make
        self.model=model
        self.color=color

#my_car=Car(make="Citroen", model="C5")
my_car=Car()
print()
print(my_car.make)
print(my_car.model)
print(my_car.color)