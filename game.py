from character import Character
from storyline import Storyline
from combat import Combat
from inventory import Inventory
from events import random_event

class RPGGame:
    def __init__(self):
        self.character = Character()
        self.storyline = Storyline(self.character)
        self.inventory = Inventory()
        self.combat = Combat(self.character, self.inventory)

    def start_game(self):
        print("Welcome to the RPG Adventure Game!")
        self.character.create_character()
        while self.character.is_alive():
            self.progress_story()

    def progress_story(self):
        # Random event occurs with a small probability
        if random_event(self.character):
            return  # Skip story progression if random event is triggered

        choice = self.storyline.generate_story()
        if choice == "combat":
            self.combat.start_battle()
        elif choice == "inventory":
            self.inventory.manage_inventory()
        else:
            print("You continue your journey.")

if __name__ == "__main__":
    game = RPGGame()
    game.start_game()
