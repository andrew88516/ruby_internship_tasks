class Order:
    
    def __init__(self, items, discounts):
        self.items = items
        self.discounts = discounts
    
    def total_sum(self):
        return sum([x - (y / 100 * x) for x, y in zip(self.items, self.discounts)])

order1 = Order([100.0, 112.2, 301.1], [10.0, 0.0, 0.0])

order1.total_sum()