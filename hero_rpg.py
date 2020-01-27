import random
import sys



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
    print("Listen Batman, The Joker and Bane are on the loose!, The city needs you...\n")
    print("1. Suit up\n")
    print("2. Let Superman take care of it\n")
    raw_input = input()
    if raw_input == "1":
        # print(battle())
        battle()
    if raw_input == "2":
        print("You're not a real superhero anyway.")
        game_over()
def battle():
        print("What is our first stop?\n")
        print("1. Arkham Asylum.\n")
        print("2. Poison Ivys Hideout\n")
        print("3. Quit")
        raw_input = input()
        if raw_input == "1":
            joker_battle()
        elif raw_input == "2":
            bane_battle()
        elif raw_input == "3":
            game_over()
            
        
def bane_battle():
    while Joker.alive() > 0 and Batman.alive() > 0:
        print()
        print("You arrived to find an angry BANE! What do you do\n")
        print("1. Fight\n")
        print("2. Run Away!\n")
        print()
        raw_input = input()
        if raw_input == "1":
            Batman.attack(Bane)
            Batman.print_status()
            Bane.print_status()
        elif raw_input == "2":
            print()
            print("Superman isn't a quitter")
            print()
            battle()
        if Bane.alive():
            Batman.health -= Bane.power
            if not Batman.alive():
                print("You are dead.")
                print("GAME OVER")

def joker_battle():
    while Joker.alive() > 0 and Batman.alive() > 0:
        print()
        print("You arrive at Arkham and spot The Joker!\n")
        print("What do you do?\n")
        print("1.Attack\n")
        print("2.Run away\n")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            Batman.attack(Joker)
            Batman.print_status()
            Joker.print_status()
            if not Joker.alive():
                print("The Joker is dead.")
        elif raw_input == "2":
            print()
            print("*******Harley has more balls than you********")
            print()
            battle()
        elif raw_input == "3":
            game_over()           
        else:
            print(f"Try Again {raw_input}")
        if Joker.alive():
            Batman.health -= Joker.power
            if not Batman.alive():
                print("You are dead.")
def game_over():
    print ("GAME OVER!")
    sys.exit()
    



main()
# battle()
# joker_battle()
# bane_battle()
# game_over()