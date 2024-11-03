import random

def random_event(character):
    if random.random() < 0.1:  # 10% chance for an event
        print("A random event occurs!")
        # Add event consequences, such as stat changes or story progression
        character.health -= 10
        print("You tripped and lost 10 health.")
        return True
    return False
