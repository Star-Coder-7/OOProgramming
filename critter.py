import random


class Critter(object):
    """
    A virtual pet to interact with.
    """

    def __init__(self, name, hunger=0, boredom=0, dirt=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.dirt = dirt

        self.options = (
            {0: "Quit"},
            {1: f"Listen to {self.name}"},
            {2: f"Feed {self.name}"},
            {3: f"Play with {self.name}"},
            {4: f"Clean {self.name}"},
            {5: f"Ignore {self.name}"},
            {6: f"Check your status with {self.name} so far."}
        )

    def __passTime(self):
        self.hunger += random.randint(1, 4)
        self.boredom += random.randint(1, 4)
        self.dirt += random.randint(1, 4)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom + self.dirt
        if unhappiness < 5:
            m = 'happy'
        elif 5 <= unhappiness < 10:
            m = 'okay'
        elif 10 <= unhappiness < 15:
            m = 'frustrated'
        else:
            m = 'mad'

        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__passTime()

    def eat(self, food=random.randint(1, 4)):
        print("Delicious. Thank you for feeding me!\n")
        self.hunger -= food
        print("I feel", self.mood, "now.\n")
        if self.hunger < 0:
            self.hunger = 0
        self.__passTime()

    def play(self, fun=random.randint(1, 4)):
        print("Woohoo, I'm having so much fun!\n")
        self.boredom -= fun
        print("I feel", self.mood, "now.\n")
        if self.boredom < 0:
            self.boredom = 0
        self.__passTime()

    def clean(self, cleaned=random.randint(1, 4)):
        print("Haaaaa, thank you for cleaning me.")
        self.dirt -= cleaned
        print("I feel", self.mood, "now.\n")
        if self.dirt < 0:
            self.dirt = 0
        self.__passTime()

    def ignore(self):
        self.__passTime()

    def status(self):
        print("Here is your status so far:\n")
        print("Boredom = ", self.boredom)
        print("Hunger = ", self.hunger)
        print("Dirt = ", self.dirt)
        print(self.name, "is currently feeling ", self.mood, "\n")
        self.__passTime()

    def interact(self, choice):
        if choice == '0':
            print("Thank you for interacting with ", self.name)
        elif choice == '1':
            self.talk()
        elif choice == '2':
            self.eat()
        elif choice == '3':
            self.play()
        elif choice == '4':
            self.clean()
        elif choice == '5':
            self.ignore()
        elif choice == '6':
            self.status()


def mainRun():
    critterName = input("What do you want to name your virtual critter?: ")
    critter = Critter(critterName)
    print()
    choice = None
    while choice != '0':
        for index, option in enumerate(critter.options):
            print(f"{index} - {option}")

        choice = input("\nPlease enter your choice from 0-6: ")
        print()

        critter.interact(choice)


if __name__ == '__main__':
    mainRun()
