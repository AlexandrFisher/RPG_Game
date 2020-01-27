class Character:
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Character):
    def __init__(self,health,power, defense):
        self.health =health
        self.power = power
        self.defense = defense
    def attack(self,Hero):
        Villain.health -= self.power
            

class Villain(Character):
    def __init__(self,health,defense, power):
        self.health =health
        self.defense =defense
        self.power = power
    def attack(self,Hero):
        Hero.health -= self.power

hero= Hero(100,90,100)
villian =Villain(90,75,120)
def main():
    print ("Welcome to my game!")
    print ("1.) Start")
    print ("2.) Load")
    print ("3.) Exit")
    raw_input = input()
    if raw_input == "1":
        print ("Welcome to the start")
        print ("What do you want to do?")
        print ("1.) Battle")
        print ("2.) Observe")
        print ("3.) Run away")
        raw_input = input()
        if raw_input == "1":
            hero.attack(Villain)
            print ("You dealt {} damage".format(hero.power))
            if villian.health <= 0:
                print ("The goblin is dead")
        elif raw_input == "2":
            print ("You are closing observing your surroundings")
        elif raw_input == "3":
            print (" You ran away, like a COWARD!")
            
        else:
            print ("Invalid input {}".format(raw_input))

        if villian.alive:
            villian.attack(hero)
            print ("The Villian does {} damage to you.".format(goblinpower))
            if hero.health <= 0:
                print ("You are DEAD!")

    else:
        main()
main()
