class Hero:
    x = 90

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_fight(self, a):
        self.a = a

    def show_fight(self):
        return self.a

    def run(self):
        print(self.name)
        print("hero can run fastly")


class Queen(Hero):

    def __init__(self, name, age, pet):
        super().__init__(name, age)

        self.pet = pet

    def rani(self):
        print("i have  a queen")


p1 = Queen("majed", 20, "cat")
p2 = Hero("nitol", 200)


p1.set_fight("fight")
# fight = p1.show_fight()
# print(fight)
# print(p1.age)
# print(p1.pet)
# print(p2.age)
print(p2.x)
# p1.run()
