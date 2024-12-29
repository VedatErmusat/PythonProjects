from turtle import Turtle, Screen
from snake import Snake
import time

# Ekran ayarları
screen = Screen()
screen.setup(width=600, height=600)  # Ekran boyutunu ayarlar
screen.bgcolor("black")  # Ekran arkaplan rengini ayarlar
screen.title("MY SNAKE GAME")  # Ekran başlığını ayarlar
screen.tracer(0)  # Ekran güncellemelerini manuel olarak kontrol etmeyi sağlar

# Yılan oluşturma
snake = Snake()

# Klavye dinleme ve yılanın yön değiştirme fonksiyonlarını bağlama
screen.listen()
screen.onkey(snake.up, "Up")  # Yukarı ok tuşu ile yukarı hareket
screen.onkey(snake.down, "Down")  # Aşağı ok tuşu ile aşağı hareket
screen.onkey(snake.left, "Left")  # Sol ok tuşu ile sola hareket
screen.onkey(snake.right, "Right")  # Sağ ok tuşu ile sağa hareket

# Oyun döngüsü
game_is_on = True
while game_is_on:
    screen.update()  # Ekranı günceller
    time.sleep(0.1)  # Kısa bir süre bekler (oyunun hızını kontrol eder)

    snake.move()  # Yılanı hareket ettirir

# Ekrana tıklama ile programı sonlandırma
screen.exitonclick()
