"""FileNotFoundError"""
# with open("data.txt") as file:
#     file.read()
# try:
#     file = open("file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["omerfi"])
# except FileNotFoundError:
    # print("There was an error!")
    # Burda tüm işlemlerimizi yazıp try bloğu içerisinde çalışmayınca buraya geçer
    # Ve burda olan işlemleri gerçekleştirir
    # file = open("file.txt", "w")
    # file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist!")
# else:
#     content = file.read()
#     print(content)  # Buranın çalışması için try bloğu içerisinde bilinen bir key girmemiz gerek
#                     # O da omerfi yerine key yazmak
# finally:
#     file.close()
#     print("File was closed")

# KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]

# IndexError: list index out of range
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# TypeError: can only concatenate str (not "int") to str
# text = "Vedo"
# print(text + 5)

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise TypeError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)





