"""While Loop"""
import time

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello " + name)

# name = None
# while not name:
#     name = input("Enter your name: ")

# print("Hello " + name)

"""For Loop"""
# for i in range(10):  # 0'dan başlar
#     print(i + 1)  # 0'a 1 ekler ve 1 2 3 ... 10 diye alt alta yazar

# for i in range(50, 100 + 1, 2):  # 50'den başlayıp 2 şer ekleyerek 100 e kadar yazar
#     print(i)

# for i in "Vedo Baba":  # Vedo Baba diye karakterleri yan yana yazdırır end="" dediğimizde
#     print(i, end="")  # Eğer sadece i yazdır deseydik alt alta Vedo Baba'yı yazcaktı

# for sec in range(10, 0, -1):
#     print(sec, end=", ")
#     time.sleep(1)
# print("Happy new year!")

"""Nested Loop"""
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()


"""Loop Control Statements"""
# while True:
#     name = input("What's your name?: ")
#     if name != "":
#         break  # Veriyi girdikten sonra döngümüzü bitirir

# phone_number = "123-456-789"
# for i in phone_number:
#     if i == "-":
#         continue  # Veride istenilen değerin veya herhangi bir şeyin yazdırmadan atlar
#     print(i, end="")

for i in range(1,6):
    if i == 3:
        pass  # Verimizin istenilen değerini es yani pas geçer.
    else:
        print(i)

