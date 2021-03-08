class Town:
    
    goods_list = ['salt', 'fish', 'cloth', 'copper', 'furs']
    
    '''I couldn't think of a more convenient way to declare an instance of the class 
    than to pass the list of prices in the right order and generate a corresponding dictionary'''
    def __init__(self, prices):
        self.price_list = dict(zip(Town.goods_list, prices))
    
    
    #but I have added a method for easy editing of the price if a mistake is made
    def set_price(self, good, new_price):
        self.price_list[good] = new_price
    
    
    #a method to simplify a merchant's life, and get needed goods price easily
    def get_price(self, good):
        return self.price_list[good]
        
class Trader:
    
    COINS = 50
    
    '''When an instance of the merchant class is initialized, the amount of coins 
    specified in the COINS constant will be assigned to it. I also refer to the 
    Town class to find out what kind of goods the merchant will trade in'''
    def __init__(self):
        self.coins = Trader.COINS
        self.goods_to_trade = Town.goods_list
    
    def trade(self, towns_list):
        for town in towns_list:
            for good in self.goods_to_trade:
                pass
    
'''Unfortunately, I have not been able to come up with the right algorithm to solve the
problem with trading. I wanted to call a list of all prices for each city, which I would
pass in an array, and by comparing prices determine the most profitable route.'''
    
Lubek = Town([20, 50, 60, 46, 96])
Bergen = Town([62, 15, 18, 82, 54])
Reval = Town([35, 50, 40, 60, 45])

Trader1 = Trader()
Trader1.trade([Lubek, Bergen, Reval])
