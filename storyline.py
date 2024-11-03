import openai

class Storyline:
    def __init__(self, character):
        self.character = character
        self.story_state = []
        openai.api_key = "your_openai_api_key"

    def generate_story(self):
        prompt = (
            f"Character {self.character.name}, level {self.character.level}, "
            f"is in the middle of an adventure. {self.story_state} "
            "What challenges does the character face next?"
        )
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.8
        )
        
        story_segment = response.choices[0].text.strip()
        print(story_segment)
        self.story_state.append(story_segment)

        # Prompt user for choice and return action based on response
        choice = input("Choose an action (explore, combat, inventory): ").lower()
        return choice
