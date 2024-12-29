""" List Comprehension"""
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_list = n + 1
#     new_list.append(add_list)
# print(new_list)

# Üstteki 4 satır kodu aşağıdaki gibi daha okunur yazabiliriz.
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list) ve çıktımız da = [2, 3, 4]

# name = "Vedat"
# letter_list = [letter for letter in name]
# print(letter_list)
#
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [n for n in names if len(n) < 5]
# upper_names = [n.upper() for n in names if len(n) > 5]
# print(short_names)
# print(upper_names)

"""Squaring Numbers Example"""
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num*num for num in numbers]
# print(squared_numbers)


"""Filtering Even Numbers Example"""
list_of_strings = input("Enter num with: ").split(',')
numbers = [int(x) for x in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)


