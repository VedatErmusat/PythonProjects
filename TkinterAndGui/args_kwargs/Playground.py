# def add(*args):
#    for n in args
#        print(n)
# Çoklu parametreleri işleme daha kolay dökmek için *args (argümanlar)

# def add(*args):
#     # print(type(args))
#     print(args)
#
#
# add(3, 5, 6)

# def add(*args):
#     print(args[0])  # Argümanların ilkini yazar.
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(3, 5, 6))  # İçerisine istediğimiz kadar değer girebiliriz.


def calculate(n, **kwargs):
    print(kwargs)  # print(type(kwargs)) = <class 'dict'>
    # for key, value in kwargs.items():
    #     print(key, value)

    # print(kwargs["add"])
    # print(kwargs["multiply"])
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]  # kw.get("make")
        self.model = kw["model"]  # kw.get("make")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model)
