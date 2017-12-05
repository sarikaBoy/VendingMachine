# Class => Vending Machine
#Layers of abstraction => Inser_coins,Select Product,Make Change

class Vending_Machine(object):
    accepted_coins = (0.25, 0.50, 1.00, 2.00)
    Products = {cola:1.00,chips:0.50,candy:0.65}
    
    def __init__(self):
        self.total = 0.00
 
    def insert_coin(self, coin):
        """ Vending machine accept coins"""
        if float(coin) not in self.accepted_coins:
            print('Vending machine accepts only: {}.'.format(self.accepted_coins), end=' ')
        else:
            self.total += coin
        print('Total of {:.2f} in the machine'.format(self.total))
 
    def selectProduct(self, buy_drink):
        """Select the product with right amount """
        buy_drink = buy_drink.lower()
        if buy_drink not in self.Products:
            print("We don't have {}. You can buy only:".format(buy_drink))
            for drink, price in sorted(self.Products.items()):
                print('{} for {:.2f}'.format(drink, price))
        elif self.total < self.Products[buy_drink]:
            print('Not enough money in the machine. Please insert {:.2f} more'.format(self.Products[buy_drink] - self.total))
        else:
            self.total -= self.Products[buy_drink]
            print('Take your {}. Total of {:.2f} in the machine'.format(buy_drink, self.total))

        def makeChangeExact(remainin_amount):
            """ the coins required to make change equal to amount"""
            coins = ["$1", "25c", "10c", "5c", "1c"]
            amounts = [int(coin[:-1]) if coin.endswith("c") 
                       else 100 * int(coin[1:]) 
                       for coin in coins]
            counts = [0 for _ in coins]
            for index, amount in enumerate(amounts):
                counts[index] = remainin_amount // amount
                remainder %= amount
            return ", ".join("{0} x {1}".format(count, coin) 
                             for count, coin in zip(counts, coins) 
                             if count)
            

VendingMachine = Vending_Machine()

print("Enter 1 to inset the coin into the vending machine")
print("Enter 2 to setect the product")
print("Enter 3 to make change")

userChoice = int(input())
if userCHoice is 1:
    Vending_Machine.insert_coin()
    
elif userChoice is 2:
    Vending_Machine.selectProduct()

elif userChoice is 3:
    Vending_Machine.makeChangeExact()

    

