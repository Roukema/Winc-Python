class Fruit(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


fruitmandje = [Fruit("appel", 100), Fruit("peer", 50), Fruit("kiwi", 100)]

for fruit in fruitmandje:
    print(f"Een {fruit.name} weegt {fruit.weight} gram. ")
