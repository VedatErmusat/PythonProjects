#import Another_Module
#print(Another_Module.Another_variable)

from turtle import Turtle, Screen
vedo = Turtle()
print(vedo) #Bu turtle nesneyi terminale yazdırır
vedo.shape("turtle") #Ekrana kaplumbağa şekli bastırır
vedo.color("DarkRed") #Ekrandaki şeklin rengini ayarlar
vedo.forward(100) #Şeklin istenilen sayı kadar ilerlemesini sağlar

my_screen = Screen()
print(my_screen.canvheight) #Bir pencere açar ve kapanır yüksekliği terminale yazılır.
my_screen.exitonclick() #Ekrana dokunduktan sonra açılan pencere kapanır

from prettytable import PrettyTable
table = PrettyTable()




