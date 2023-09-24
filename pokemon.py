# Step 1: Create the Pokemon class

class Pokemon:
    def __init__(self, name, level, type):
        # Initialize Pokemon attributes
        self.name = name            # Name of the Pokemon
        self.level = level          # Level of the Pokemon
        self.type = type            # Type of the Pokemon
        self.max_health = level * 10  # Calculate max health based on level
        self.current_health = self.max_health  # Set current health to max initially
        self.is_knocked_out = False  # Pokemon starts not knocked out

# Step 2: Add methods to the Pokemon class

    def lose_health(self, damage):
        # Decrease current health and handle knockouts
        if not self.is_knocked_out:
            self.current_health -= damage
            if self.current_health <= 0:
                self.current_health = 0
                self.knock_out()
            print(f"{self.name} now has {self.current_health} health.")
        else:
            print(f"{self.name} is knocked out and cannot take damage.")

    def gain_health(self, healing):
        # Increase current health, but not beyond max health
        if not self.is_knocked_out:
            self.current_health += healing
            if self.current_health > self.max_health:
                self.current_health = self.max_health
            print(f"{self.name} now has {self.current_health} health.")
        else:
            print(f"{self.name} is knocked out and cannot be healed.")

    def knock_out(self):
        # Set the Pokemon as knocked out
        self.is_knocked_out = True
        print(f"{self.name} is knocked out!")

    def revive(self):
        # Revive the knocked out Pokemon
        if self.is_knocked_out:
            self.is_knocked_out = False
            self.current_health = 1  # Revived Pokemon has 1 health
            print(f"{self.name} has been revived with 1 health.")

    def attack(self, other_pokemon):
        # Calculate damage and attack another Pokemon
        if not self.is_knocked_out:
            damage = self.calculate_damage(other_pokemon)
            print(f"{self.name} attacks {other_pokemon.name} for {damage} damage.")
            other_pokemon.lose_health(damage)
        else:
            print(f"{self.name} is knocked out and cannot attack.")

    def calculate_damage(self, other_pokemon):
        # Calculate damage based on type advantages/disadvantages
        advantage_types = {
            "Fire": ["Grass"],
            "Water": ["Fire"],
            "Grass": ["Water"]
        }
        disadvantage_types = {
            "Fire": ["Water"],
            "Water": ["Grass"],
            "Grass": ["Fire"]
        }

        if self.type in advantage_types.get(other_pokemon.type, []):
            return self.level * 2
        elif self.type in disadvantage_types.get(other_pokemon.type, []):
            return self.level // 2
        else:
            return self.level

# Step 3: Create the Trainer class

class Trainer:
    def __init__(self, name):
        # Initialize Trainer attributes
        self.name = name              # Name of the Trainer
        self.pokemon_team = []        # List to store Pokemon in the team
        self.potions = 5              # Number of potions
        self.current_active_pokemon = None  # Currently active Pokemon

# Step 4: Add methods to the Trainer class

    def use_potion(self):
        # Use a potion to heal the active Pokemon
        if self.potions > 0 and self.current_active_pokemon:
            self.potions -= 1
            self.current_active_pokemon.gain_health(20)  # You can adjust the healing amount
            print(f"{self.name} used a potion on {self.current_active_pokemon.name}.")

    def attack_trainer(self, other_trainer):
        # Attack the active Pokemon of another trainer
        if self.current_active_pokemon and other_trainer.current_active_pokemon:
            self.current_active_pokemon.attack(other_trainer.current_active_pokemon)

    def switch_pokemon(self, new_pokemon_index):
        # Switch to a different Pokemon in the team
        if 0 <= new_pokemon_index < len(self.pokemon_team):
            new_pokemon = self.pokemon_team[new_pokemon_index]
            if not new_pokemon.is_knocked_out:
                self.current_active_pokemon = new_pokemon
                print(f"{self.name} switched to {new_pokemon.name}.")
            else:
                print(f"{new_pokemon.name} is knocked out and cannot be switched to.")

# Step 5: Example Usage

# Create Pokémon
pikachu = Pokemon("Pikachu", 10, "Electric")
bulbasaur = Pokemon("Bulbasaur", 10, "Grass")
charmander = Pokemon("Charmander", 10, "Fire")

# Create Trainers
trainer1 = Trainer("Ash")
trainer2 = Trainer("Gary")

# Add Pokémon to Trainer's team
trainer1.pokemon_team.extend([pikachu, bulbasaur])
trainer2.pokemon_team.append(charmander)

# Set active Pokémon for each Trainer
trainer1.current_active_pokemon = pikachu
trainer2.current_active_pokemon = charmander

# Use methods
trainer1.attack_trainer(trainer2)
trainer2.use_potion()
trainer1.switch_pokemon(1)
