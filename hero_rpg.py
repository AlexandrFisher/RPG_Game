import random
import sys
import secrets

class Character:
    def __init__(self, health, power, probability):
        self.health = health
        self.power = power
        self.probability = probability

    def alive(self):
        if self.health > 0:
            return True
            # hello
        else:
            return False

    def attack(self, enemy):
        if (random.random() <= self.probability):
            damage = self.power * 2
            print("Attack doubled")
        else:
            damage = self.power
            print("attack was not doubled")
        enemy.health -= self.power
        if(self.character_name == "Batman"):
            print(f"You do {self.power} damage to {enemy.character_name}.")

        elif(self.character_name == "Joker"):
            print(f"The {self.character_name} does {self.power} damage to you.")

    def print_status(self):
        if self.character_name == "Batman":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "Joker":
            print(
                f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "Bane":
            print(f"{self.character_name} has {self.health} health")
        elif self.character_name == "Penguin":
            print(f"{self.character_name} has {self.health} health remaining")


class Batman(Character):
    def __init__(self, health, power,probability):
        self.character_name = "Batman"
        super(Batman, self).__init__(health, power, probability)


class Joker(Character):
    def __init__(self, health, power, probability):
        self.character_name = "Joker"
        super(Joker, self).__init__(health, power, probability)


class Bane(Character):
    def __init__(self, health, power,probability):
        self.character_name = "Bane"
        super(Bane, self).__init__(health, power, probability)


class Penguin(Character):
    def __init__(self, health, power,probability):
        self.character_name = "Penguin"
        super(Penguin, self).__init__(health, power, probability)

class Catwomen(Character):
    def __init__(self, health,power, probability):
        self.character_name = "Catwomen"
        super(Catwomen,self).__init__(health, power, probability)
        if (random.random() <= self.probability):
            heal = self.health + 2
            print("Health Increased")
        else:
            print("NO health increase")

catwomen = Catwomen(20,9,0)
batman = Batman(25, 8,2) 
joker = Joker(22, 4,0)
bane = Bane(float('Inf'), 7,.10)
penguin = Penguin(9, 7,0)


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
    print("3. Enter The Docks\n")
    print("4. Search Gotham\n")
    print("Q. Quit")
    raw_input = input()
    if raw_input == "1":
        joker_battle()
    elif raw_input == "2":
        bane_battle()
    elif raw_input == "3":
        Penguin_battle()
    elif raw_input == "4":
        random_battle()()
    elif raw_input == "Q":
        print("***GameOver***")
        sys.exit()


def Penguin_battle():
    while penguin.alive() > 0 and batman.alive() > 0:
        print()
        print("While exploring Gotham..\n")
        print("You see suspicious activity by the docks\n")
        print("You spot Penguin and his goons terrorizing the workers\n")
        print("What do you do?\n")
        print("1. Fight!!\n")
        print("2. Call Superman\n")

        raw_input = input()
        if raw_input == "1":
            batman.attack(penguin)
            batman.print_status()
            if not penguin.alive():
                print()
                print("The Penguin has been defeated\n")
                print("Back to the Batmobile!\n")
                battle()
            penguin.print_status()
        elif raw_input == "2":
            print()
            print("****Don't worry a REAL superhero will take care of this****")
            battle()


def bane_battle():
    while bane.alive() > 0 and batman.alive() > 0:
        print()
        print("You arrived to find an angry BANE! What do you do\n")
        print("1. Fight\n")
        print("2. Run Away!\n")
        print()
        raw_input = input()
        if raw_input == "1":
            batman.attack(bane)
            batman.print_status()
            bane.print_status()
        elif raw_input == "2":
            print()
            print("Superman isn't a quitter")
            print()
            battle()
        if bane.alive():
            batman.health -= bane.power
            if not batman.alive():
                print("You are dead.")
                print("GAME OVER")

def catwomen_battle():
    while catwomen.alive() > 0 and batman.alive() > 0:
        print()
        print("**You ended up in the alleyway**\n")
        print(f"Out of the shadows you are attacked by {catwomen.character_name}")
        catwomen.attack(batman)
        batman.print_status()
        print("**What do you do**\n")
        print("1. Attack")
        print("2. Run Away")
        raw_input = input()
        if raw_input == "1":
            batman.attack(catwomen)
            batman.print_status()
            if not catwomen.alive():
                print("Catwomen is defeated")
                print("you earned 12")
                battle()

def joker_battle():
    while joker.alive() > 0 and batman.alive() > 0:
        print()
        print("You arrive at Arkham and spot The Joker!\n")
        print("What do you do?\n")
        print("1.Attack\n")
        print("2.Run away\n")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            batman.attack(joker)
            batman.print_status()
            if not joker.alive():
                print("The Joker is dead.")
                game_over()
            joker.print_status()
        elif raw_input == "2":
            print()
            print("******* Harley has more balls than you ********")
            print()
            battle()
        elif raw_input == "3":
            game_over()
        else:
            print(f"Try Again {raw_input}")
        if joker.alive():
            batman.health -= joker.power
            if not batman.alive():
                print("You are dead.")

def random_battle():
    print("Look what you found")
    Villains = [joker_battle, Penguin_battle, bane_battle, catwomen_battle]
    randomInt = random.randint(0,3)

    print(f" Random num from random battle {randomInt}")
    return Villains[randomInt]
    


def game_over():
    print("GAME OVER!")
    sys.exit()


main()
# battle()
# joker_battle()
# bane_battle()
# game_over()
