from decimal import *

from datetime import datetime

class Parkomat:

    def __init__(self):
        self._List_Money = []
        self._Actual_Time = datetime.now()
        self._Leaving_Time = self._Actual_Time
        self._Registration = ''
        self._Sum = 0


def counting_coins(self, value, number):


class Coin():

    List_Money = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50]


class Money(Coin):

    def __init__(self, value):
        super().__init__()
        if value in self.List.Money:
            self._Value = Decimal(str(value))
        else:
            self._Value = Decimal('0')
            print('Unknown coin')
        self._Currency = 'PLN'

    def get_value(self):
        return self.value

    def get_currency(self):
        return self._Currency


