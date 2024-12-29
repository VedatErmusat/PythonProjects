"""List"""

# food = ["Hamburger", "Pizza", "Hotdog", "Puding"]

# food[0] = "sushi"
# food.append("ice-cream")  # Yeni bir eleman ekler
# food.remove("Hotdog")  # Bir eleman siler
# food.pop()  # Son elemanı siler
# food.insert(0, "Cake")  # 0. indekse cake yazar
# food.sort()  # Bu da elemanları sıralar
# food.clear()  # Tüm elemanları#  siler


# for x in food:
#     print(x)

"""2D Lists"""

# drinks = ["coffe", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice-cream"]

# food = [drinks, dinner, dessert]
# print(food)
# print(food[0])
# print(food[0], [2])
# print(food[2], [2])  # İndeks hatası verir

"""Tuple"""

# student = ("Bro", 21, "Male")

# print(student.count("Bro"))
# print(student.index("Male"))

# for x in student:
#     print(x)

# if "Bro" in student:
#     print("Bro is here!")

"""Sets"""
# Bir değeri birden fazla yazsan bile birini yazdırır.(Kümeler)

utensils = {"fork", "spoon", "knife"}  # Rastgele sıralayarak yazar farketmeksizin.
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# utensils.update(dishes)
# for x in utensils:
#     print(x)

# dishes.update(utensils)
# for x in dishes:
#     print(x)

# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)

# print(dishes.difference(utensils))  # Bulaşıkların mutfak aletlerinden farklarını yazar
# print(utensils.difference(dishes))  # Mutfak aletlerinin bulaşıklardan farklarını yazar

# print(utensils.intersection(dishes))  # Kesişiminde olan elemanlarını yazar.


