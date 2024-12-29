# file = open("my_text.txt")  # with open("my_text.txt") as file: with sözcüğü olduğu sürece dosyayı kapat komutuna gerek yok
# contents = file.read()             # contents = file.read()
# print(contents)                    # print(contents)
# file.close()

with open("my_text.txt", mode="w") as file:  # Eski veriler silinmesin dersek mode="a" olmalı
    file.write("\nHello can")  # Dosya içindeki veriyi siler ve yerine yeni verimizi yazar

# Eğer herhangi bir dosyamız yoksa open içerisine dosyamızın ismini yazarsak kendi kendine yenisi oluşturulur


# Herhangi bir dosyaya ulaşmak için dosya yolunu yazarak ulaşabiliriz

# with open("/Users/Vedat/Desktop/my_text.txt", mode="w") as file:
#     file.write("\nHello can")
# ../../Desktop/my_text.txt
