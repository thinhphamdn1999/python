def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def run(name):
    print(f"Run {name}")

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(add(1, 2, 3))
print(calculate(n=2, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.modal = kw.get("modal")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", modal="123")
print(my_car.seats)