
"""String Slice"""
name = "Vedo Baba"
# [start:stop:step]
# first_name = name[0]  # 0.indeksi yazdırır = V
first_name = name[0:4]  # 0.indeks ile 4. indekse kadar yazdırır = Ve --> first_name = name[:4]
last_name = name[5:9]  # 5.indeks ile 9. indeks arasını yazdırır = Baba --> last_name = name[5:]
funky_name = name[0:9:1]  # step yani adım adım atla ve yazdır diyoruz aslında. = Vedo Baba
punk_name = name[0:9:2]  # step yani 2 adım atla ve yazdır diyoruz aslında. = Vd aa
car_name = name[::3]  # step yani 3 adım atla ve yazdır diyoruz aslında = Voa
reversed_name = name[::-1]  # Geriye doğru değişkenimizi yazdırır = abaB odeV

print(first_name)
print(last_name)
print(funky_name)
print(punk_name)
print(car_name)
print(reversed_name)


website = "http://google.com"
website2 = "http://wikipedia.com"
dilimle = slice(7, -4)
print(website[dilimle])
print(website2[dilimle])
