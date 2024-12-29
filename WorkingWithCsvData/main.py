# CSV = Comma Separated Values = Ayrılmış Değerler

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # print(data) dersek hemen sonrasında bir csv objesi oluşur = <_csv.reader object at 0x000002619fb4cf40>
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)  # temp değerlerimizi bu listeye atamış olduk append komutuyla

import pandas as pan 

# data = pan.read_csv("weather_data.csv")
# print(type(data))  # DataFrame object
# print(type(data["temp"]))  # Series object
# print(data), print(data["temp"]), print(data["day"]), print(data["condition"])


# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# Ortalama Hesaplarken Kullanılabilcek Metot
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())  # En yüksek sıcaklık değerini verir

""" Get Data in Columns"""
# print(data["condition"])
# print(data.condition)

""" Get Data in Columns"""
# print(data[data.day == "Monday"])  # Pazartesi satırındaki verileri yazar
# print(data[data.temp == data.temp.max()])  # Sıcaklığı en yüksek olan satırdaki verileri yazar

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

""" Create a DataFrame from scratch"""
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pan.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")


