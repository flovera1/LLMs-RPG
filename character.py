class Character:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.level = 1
        self.experience = 0
        self.skills = {"attack": 10, "defense": 5}
    
    def create_character(self):
        self.name = input("Enter your character's name: ")
        print(f"Welcome, {self.name}! Your journey begins now.")

    def level_up(self):
        self.level += 1
        self.health += 20
        self.skills["attack"] += 5
        self.skills["defense"] += 5
        print(f"{self.name} leveled up to level {self.level}!")

    def is_alive(self):
        return self.health > 0
