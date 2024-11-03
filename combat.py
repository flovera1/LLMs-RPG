import random

class Combat:
    def __init__(self, character, inventory):
        self.character = character
        self.inventory = inventory

    def start_battle(self):
        enemy_health = random.randint(20, 50)
        print("An enemy approaches! Prepare for battle.")

        while enemy_health > 0 and self.character.is_alive():
            action = input("Choose an action (attack, defend, use item): ").lower()
            if action == "attack":
                damage = self.character.skills["attack"]
                enemy_health -= damage
                print(f"You dealt {damage} damage to the enemy.")
            elif action == "defend":
                print("You brace yourself and reduce incoming damage.")
            elif action == "use item":
                self.inventory.use_item()
            else:
                print("Invalid action.")
            
            # Enemy attacks back
            if enemy_health > 0:
                enemy_damage = random.randint(5, 15)
                self.character.health -= enemy_damage
                print(f"The enemy dealt {enemy_damage} damage to you!")
        
        if self.character.is_alive():
            print("You defeated the enemy!")
        else:
            print("You have been defeated.")
