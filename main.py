from classes.Store import Store
from classes.Shop import Shop
from classes.Request import Request



def main():
    storee = Store(
        {"мороженое": 11,
         "ноутбуки": 1,
         "капкейки": 3}
    )
    shopp = Shop(
        {"арбузы": 10,
         "зарядники": 7,
         "m&m's": 3}
    )

    """Приветствие и главная программа"""

    print('Добрый день. Добро пожаловать в shop')
    print('Имеется в наличии в магазине:')
    print(shopp.get_items())
    print('Товары на складе:')
    print(storee.get_items())
    print('Комнада чтобы сделать заказ from shop:')
    print('Доставить {кол-во товара} {сам товар} из магазина в склад')
    print('Комнада чтобы вернуть заказ на склад :')
    print('Доставить {кол-во товара} {сам товар} из склада в магазин')
    print('для завершения программы команда - "Завершить" ')


    while True:  # цикл главной программы
        user = input().lower()
        if user == 'завершить':
            print('End)')
            break

        request = Request(user)
        if request._to == 'магазин': # действия для доставки в магазин
            try:
                remainder = storee.remove(request.product, request.amount)  # в случае нехватки товара для отправки отдается то, что есть в наличии
                if remainder is not None:
                    shopp.add(request.product, remainder)
                else:
                    shopp.add(request.product, request.amount) #
            except Exception:
                print('Товары на скалде закончились')

        else: # действия для доставки на склад
            try:
                remainder = shopp.remove(request.product, request.amount)
                if remainder is not None:
                    storee.add(request.product, remainder)
                else:
                    storee.add(request.product, request.amount)
            except Exception:
                print('Товара на складе нет или закончился')
        print(f'Осталось на складе: {storee.get_items()}')
        print(f'Осталось в магазине: {shopp.get_items()}')


# Доставить 9 арбузы из склада в магазин




if __name__ == '__main__':
    main()