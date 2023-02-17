class Album:

    def __init__(self, artist, title, year_released, genre, description, stock_qty, purchase_price, sell_price, id = None):
        self.artist = artist
        self.title = title
        self.year_released = year_released
        self.genre = genre
        self.description = description
        self.stock_qty = stock_qty
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.id = id
