class Inventory:
    def __init__(self):
        self.items = {"potion": 3, "elixir": 1}

    def manage_inventory(self):
        print("Your inventory:", self.items)
        action = input("Choose an item to use or 'exit': ").lower()
        if action in self.items and self.items[action] > 0:
            self.use_item(action)
        elif action == "exit":
            return
        else:
            print("Invalid choice or item not available.")

    def use_item(self, item="potion"):
        if self.items.get(item, 0) > 0:
            if item == "potion":
                print("You used a potion and restored health.")
            elif item == "elixir":
                print("You used an elixir and boosted your attack.")
            self.items[item] -= 1
        else:
            print("You don't have that item!")
