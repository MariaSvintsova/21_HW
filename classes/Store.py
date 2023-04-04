from classes.Storage import Storage

"""Класс склада"""
class Store(Storage):
    def __init__(self, items: dict[str, int], capacity=100):
        super().__init__(items, capacity)


    def add(self, item, capacity):
        """Добавление товара на склад"""
        if item in self.items.keys():
            self.items[item] += capacity
        else:
            self.items[item] = capacity

    def remove(self, item, capacity):
        """Логика удаления товара со склада"""
        if item in self.items.keys():
            if self.items[item] > capacity:
                if self.items[item] < capacity:
                    self.items[item] = 0
                else:
                    self.items[item] -= capacity
            else:
                a = self.items[item]
                self.items[item] = 0
                return a
        else:
            raise Exception


    def get_free_space(self):
        """ количество товаров в сумме """
        summ = 0
        for i in self.items.values():
            summ += i
        return self._capacity - summ

    def get_items(self):
        """словарь со всеми товарами"""
        return self.items

    def get_unique_items_count(self):
        """количество уникальных товаров"""
        return len(self.items.keys())

