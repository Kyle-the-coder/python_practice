class User:
    def __init__ (self, first_name, last_name, age, gold_points):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = gold_points

    def display_info(self):
        print(self.first + "\n" + self.last + "\n" + str(self.age) + "\n" + str(self.gold_card_points) + " points")
        return self

    def enroll(self):
        if(self.is_rewards_member == False):
            print("User already a member")
        else:
            print("True")
        return self
            

    def decrease_points(self, num):
        if(self.gold_card_points <= 0):
            return "You don't have points to spend"
        else:
            you_lost = self.gold_card_points - num
            return("You now have " + str(you_lost) + " gold points")


user_kyle = User("Kyle", "Mitchell", 31, 300)

user_bianca = User("Bianca", "Marshall", 45, 1005)

user_ben = User("Ben", "Marin", 13, 103456)

# print(user_kyle.decrease_points(100))

user_bianca.display_info().enroll()

# print(user_bianca.decrease_points(80))

# print(kyle.decrease_points(50))

# print(bianca.decrease_points(200))


# kyle.display_info()

# print(kyle.enroll())







