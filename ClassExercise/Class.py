#def User():
#    pass  # Bu sözcük fonksiyonu kullanmadan atlamamıza yarar


class User:  # Sınıf isimlerinde PascalCase her zaman kullanılır.
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "İcardi")

user_1.follow(user_2)
# user_2.follow(user_1)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


#car1 = Car(5)  # Bu kullanım eşittir "my_car.seats = 5
#car1.id = "1"
#car1.name = "passat"
