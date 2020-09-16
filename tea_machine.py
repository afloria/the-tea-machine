class TeaMachine:
    SHORT_ON_WATER = "Sorry, not enough water"
    SHORT_ON_HONEY = "Sorry, not enough honey"
    SHORT_ON_TEA = "Sorry, not enough tea"
    SHORT_ON_CUPS = "Sorry, not enough disposable cups"
    SHORT_ON_MONEY = "Sorry, not enough money"
    ENOUGH_RESOURCES = "I have enough resources, making you a tea!"
    def __init__(self,water,honey,tea_leaves,disposable_cups,money):
        self.water = water
        self.honey = honey
        self.tea_leaves = tea_leaves
        self.disposable_cups = disposable_cups
        self.money = money
    def buy_tea(self):
            type = input('What do you want to buy? 1 - matcha, unsweetened, 2 - earl grey, 3 - chamomile: ')
            if type == '1' and self.water >= 250 and self.tea_leaves >= 16 and self.disposable_cups >= 1:
                self.water -= 250
                self.tea_leaves -=  16
                self.disposable_cups -= 1
                self.money += 4
                print(self.ENOUGH_RESOURCES)
            elif type == '2' and self.water >= 350 and self.honey >= 75 and self.tea_leaves >= 20 and self.disposable_cups >= 1:
                self.water -= 350
                self.honey -= 75
                self.tea_leaves -= 20
                self.disposable_cups -= 1
                self.money += 7
                print(self.ENOUGH_RESOURCES)
            elif type == '3' and self.water >= 200 and self.honey >= 100 and self.tea_leaves >= 12 and self.disposable_cups >= 1:
                self.water -= 200
                self.honey -= 100
                self.tea_leaves -= 12
                self.disposable_cups -= 1
                self.money += 6
                print(self.ENOUGH_RESOURCES)
            elif self.water < 350:
                print(self.SHORT_ON_WATER)
            elif self.tea_leaves < 20:
                print(self.SHORT_ON_TEA)
            elif self.honey < 100:
                print(self.SHORT_ON_HONEY)
            elif self.disposable_cups < 1:
                print(self.SHORT_ON_CUPS)
            elif self.money < 7:
                print(self.SHORT_ON_MONEY)
    def fill_tea(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.honey += int(input("Write how many grams of honey do you want to add:\n"))
        self.tea_leaves += int(input("Write how many grams of tea leaves do you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    def take(self):
        print('I gave you $',self.money)
        self.money = 0
    def rem_tea(self):
        print('The tea machine has: ')
        print(self.water,'of water')
        print(self.honey,'of honey')
        print(self.tea_leaves,'of tea leaves')
        print(self.disposable_cups,'of disposable cups')
        print('$',self.money,'of money')  
    def user_input(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): ')
            if action == 'buy':
                self.buy_tea()
            elif action == 'fill':
                self.fill_tea()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.rem_tea()
            elif action == 'exit':
                print("Exiting Program")
                break
the_tea_machine = TeaMachine(400, 540, 120, 9, 550)
the_tea_machine.user_input()


    
            
