
class Request:

    def __init__(self, text: str):
        text = text.split()
        self._from = text[4]
        self._to = text[6]
        self._amount = int(text[1])
        self._product = text[2]
        self._verb = text[0]

    @property
    def from_(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product


    def __repr__(self):
        """обьект класса c данными"""
        return f'from = "{self.from_}",\n' \
               f' to =  "{self.to}",\n ' \
               f'amount = "{self.amount}",\n' \
               f' product = "{self.product}"'







