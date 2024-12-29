import time  # Zamanla ilgili işlemler yapmak için time modülünü içe aktarıyoruz

# Şu anki zamanı alıp ekrana yazdırıyoruz
current_time = time.time()
print(current_time)


# Çalışma süresini hesaplayan ve ekrana yazdıran bir dekoratör fonksiyon tanımlıyoruz
def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()  # İşlevin çalışmaya başladığı zamanı alıyoruz
        function()  # İşlevi çalıştırıyoruz
        end_time = time.time()  # İşlevin çalışmayı bitirdiği zamanı alıyoruz
        # İşlevin çalışma süresini hesaplayıp ekrana yazdırıyoruz
        print(f"{function.__name__} run speed: {end_time - start_time:.4f}s")

    return wrapper_function  # Dekoratörün süslenmiş işlevi döndürmesini sağlıyoruz


# Hızlı çalışan bir işlev tanımlıyoruz ve bu işlevi dekoratör ile süslüyoruz
@speed_calc_decorator
def fast_function():
    for i in range(1000000):  # 1.000.000 kez bir hesaplama yapıyoruz
        i * i  # Basit bir çarpma işlemi (sonuç kullanılmıyor)


# Yavaş çalışan bir işlev tanımlıyoruz ve bu işlevi dekoratör ile süslüyoruz
@speed_calc_decorator
def slow_function():
    for i in range(10000000):  # 10.000.000 kez bir hesaplama yapıyoruz
        i * i  # Basit bir çarpma işlemi (sonuç kullanılmıyor)


# Hızlı işlevi çalıştırıyoruz
fast_function()

# Yavaş işlevi çalıştırıyoruz
slow_function()
