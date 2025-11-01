monsters = [["Mike", 349, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]
class Monster:
    def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour
    def is_scary(self):
        return self.number_of_teeth > 16 and self.colour == "red".upper()
    def __str__(self):
        return f"{self.name} {self.number_of_teeth} {self.colour} {self.is_scary()}"
scary_monster = [monster for monster in monsters if monster[1] > 16 or monster[2] == "red"]
print(scary_monster)
m1 = Monster("ABC", 34, "RED")
print(m1)
print(m1.is_scary())
print(m1.name)
