class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.money = 550
        self.beans = 120
        self.milk = 540
        self.cups = 9

        self.user_input = None
        self.add_water = None
        self.add_milk = None
        self.add_cups = None
        self.add_beans = None

        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None

        self.coffee_num = None

    def actions(self):
        while True:
            self.user_input = input('Write action (buy, fill, take, remaining, exit):')
            if self.user_input == 'buy':
                self.buy()
            elif self.user_input == 'take':
                self.take()
            elif self.user_input == 'fill':
                self.fill()
            elif self.user_input == 'remaining':
                self.remaining()
            elif self.user_input == 'exit':
                break

    def remaining(self):
        print(f'The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.beans} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money')

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def fill(self):
        self.add_water = int(input("Write how many ml of water do you want to add: "))
        self.add_milk = int(input("Write how many ml of milk do you want to add: "))
        self.add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
        self.add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

        self.water += self.add_water
        self.milk += self.add_milk
        self.beans += self.add_beans
        self.cups += self.add_cups

    def coffee(self):
        if (self.water - self.a) < 0:
            print("Sorry, not enough water!")
        elif (self.milk - self.b) < 0:
            print("Sorry, not enough milk!")
        elif (self.beans - self.c) < 0:
            print("Sorry, not enough beans!")
        elif (self.cups - self.e) < 0:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= self.a
            self.milk -= self.b
            self.beans -= self.c
            self.money += self.d
            self.cups -= self.e

    def buy(self):
        self.coffee_num = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if self.coffee_num == '1':
            self.a = 250
            self.b = 0
            self.c = 16
            self.d = 4
            self.e = 1
            self.coffee()
        elif self.coffee_num == '2':
            self.a = 350
            self.b = 75
            self.c = 20
            self.d = 7
            self.e = 1
            self.coffee()
        elif self.coffee_num == '3':
            self.a = 200
            self.b = 100
            self.c = 12
            self.d = 6
            self.e = 1
            self.coffee()
        elif self.coffee_num == 'back':
            pass


coffee_machine = CoffeeMachine()
coffee_machine.actions()
