#Simple Function
def greet():
    print("Hello, Vedat!")
    print("How do you do Vedat?")
    print("How  old are you?")
greet()

#Function  with parameters
def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How do you do {name}?")
    
greet_with_name("Vedat")

#Function with more  than one parameter
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with( "Vedat", "Istanbul")

