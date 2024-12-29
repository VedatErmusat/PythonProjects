#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])  # Kaç tane gri varsa
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])  # Kaç tane kırmızı
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])  # Kaç tane siyah
print(grey_squirrels_count)  # Tüm gri sincap verilerini gösterir(Tablo benzeri)
print(red_squirrels_count)  # Tüm kırmızı sincap verilerini gösterir
print(black_squirrels_count)  # Tüm siyah sincap verilerini gösterir

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],  # Kürk renkleri
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]  # sayıları
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
