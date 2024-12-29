from turtle import Turtle

# Başlangıç pozisyonları ve hareket mesafesi sabitleri
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        # Yılanın segmentlerini içeren bir liste
        self.segments = []
        self.create_snake()
        # Yılanın baş segmenti
        self.head = self.segments[0]

    def create_snake(self):
        # Başlangıç pozisyonlarına göre yılanın segmentlerini oluşturur
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # Yılanın her segmentini bir önceki segmentin pozisyonuna taşır
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Yılanın başını ileri doğru hareket ettirir
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Yılanın başının aşağı yönde gitmediğinden emin olarak yukarı yönünü ayarlar
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        # Yılanın başının yukarı yönde gitmediğinden emin olarak aşağı yönünü ayarlar
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        # Yılanın başının sağa yönde gitmediğinden emin olarak sola yönünü ayarlar
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # Yılanın başının sola yönde gitmediğinden emin olarak sağa yönünü ayarlar
        if self.head.heading() != 180:
            self.head.setheading(0)
