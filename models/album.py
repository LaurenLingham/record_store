class Album:

    def __init__(self, artist, title, year_released, genre, stock_qty, purchase_price, sell_price, id = None):
        self.artist = artist
        self.title = title
        self.year_released = year_released
        self.genre = genre
        self.stock_qty = stock_qty
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.id = id
        self.markup_value = self.markup(purchase_price, sell_price)

    def purchase_price_formatted(self):
        return f"£{self.purchase_price:.2f}"
    
    def purchase_price_two_decimal_places(self):
        return f"{self.purchase_price:.2f}"
    
    def sell_price_formatted(self):
        return f"£{self.sell_price:.2f}"
    
    def sell_price_two_decimal_places(self):
        return f"{self.sell_price:.2f}"
    
    def markup(self, purchase_price, sell_price):
        markup_percent = (sell_price / purchase_price) - 1
        markup_percent_rounded = round(markup_percent * 100)
        return f"{markup_percent_rounded}%"
    
    def stock_number(self):
        return ("{:05d}".format(self.id))
    