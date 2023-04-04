from classes.Store import Store

class Shop(Store):
    def __init__(self, items: dict[str, int], capacity=20):
        super().__init__(items, capacity)

    def add(self, item, capacity):
        if item not in self.items.keys():
            if self.get_unique_items_count() > 5:
                return 'No place more'
            self.items[item] = capacity
        else:
            self.items[item] += capacity



    def get_unique_items_count(self):
        return len(self.items.keys())