class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False        
    def attack(self,enemy):
        # Batman attacks Joker
        enemy.health -= self.power
        if(self.character_name == "Batman"):
            print(f"You do {self.power} damage to {enemy.character_name}.")

        elif(self.character_name == "Joker"):
            print(f"The {self.character_name} does {self.power} damage to you.")
    def print_status(self):
        if self.character_name == "Batman":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "Joker":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "Bane":
            print(f"{self.character_name} has {self.health} health")

class Batman(Character):
    def __init__(self,health, power):
        self.character_name = "Batman"
        super(Batman,self).__init__(health, power)
    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


class Joker(Character):
    def __init__(self, health, power):
        self.character_name = "Joker"
        super(Joker, self).__init__(health, power)

class Bane(Character):
    def __init__(self, health, power):
        self.character_name = "Bane"
        super(Bane,self).__init__(health,power)

Batman = Batman(15,5)
Joker = Joker(13,2)
Bane = Bane(float('inf '),7)
def main():
    while Joker.alive() > 0 and Batman.alive() > 0:
        print()
        print("Welcome to Gotham!")
        print("1. Fight The Joker")
        print("2. Fight Bane")
        print("3. Pop Smoke")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            Batman.attack(Joker)
            Batman.print_status()
            Joker.print_status()
            if not Joker.alive():
                print("The Joker is dead.")
        elif raw_input == "2":
            Batman.attack(Bane)
            Batman.print_status()
            Bane.print_status()
        elif raw_input == "3":
            print("Deuces!.")
            break
        else:
            print(f"Try Again {raw_input}")

        if Joker.alive():
            # Joker attacks Batman
            Batman.health -= Joker.power
            if not Batman.alive():
                print("You are dead.")

main()
