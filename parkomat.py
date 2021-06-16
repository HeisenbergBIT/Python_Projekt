from decimal import *
from myexceptions import *
from re import compile
from datetime import datetime
from datetime import timedelta

getcontext().prec = 3

class Coin():

    ListOfCoins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50]


class Money(Coin):

    def __init__(self, value):
        super().__init__()

        if value in self.ListOfCoins:

          self._value = Decimal(str(value))

        else:

            self._value = Decimal('0')
            raise NegativeNumberOfCoins

        self._currency = 'PLN'


    def get_value(self):
        return self._value


    def get_currency(self):
        return self._currency


class Parkomat:

    def __init__(self):
        self._ListOfCoins = []
        self._Actual_Time = datetime.now()
        self._Leaving_Time = self._Actual_Time
        self._Registration = ''
        self._Sum = 0
        self._Number_Value = {0.01:0, 0.02:0, 0.05:0, 0.1:0, 0.2:0, 0.5:0, 1:0, 2:0, 5:0}



    def counting_coins(self, value, number):

        value = Decimal(str(value))

        for x in range(len(self._ListOfCoins)):

            if value == self._ListOfCoins[x].get_value():

                if value < Decimal(str(10)):
                    self._Number_Value[value] = number

                    if self._Number_Value[value] > 200:
                        raise ParkomatOverflow


    def number_coins_checking(self, number):

        try:
            int(number)

        except ValueError:
            raise NonintigerNumberOfCoins

        if int(number) <= 0:
            raise WrongValue


    def leaving_time(self, seconds):



        if self._Leaving_Time.hour >= 20:
            sek = self._Leaving_Time.second
            self._Leaving_Time += timedelta(days=1)
            self._Leaving_Time = self._Leaving_Time.replace(hour=8, minute=0, second=0)
            if self._Sum != 0:
                self._Leaving_Time += timedelta(seconds=sek)

        if self._Leaving_Time.hour < 8:
            self._Leaving_Time = self._Leaving_Time.replace(hour=8, minute=0, second=0)

        tillwhen = self._Leaving_Time.weekday()

        if tillwhen == 5:
            sek = self._Leaving_Time.second
            self._Leaving_Time += timedelta(days=2)
            self._Leaving_Time = self._Leaving_Time.replace(hour=8, minute=0, second=0)
            if self._Sum != 0:
                self._Leaving_Time += timedelta(seconds=sek)

        if tillwhen == 6:
            sek = self._Leaving_Time.second
            self._Leaving_Time += timedelta(days=1)
            self._Leaving_Time = self._Leaving_Time.replace(hour=8, minute=0, second=0)

            if self._Sum != 0:
                self._Leaving_Time += timedelta(seconds=sek)
        self._Sum += Decimal(0.01)
        self._Leaving_Time += timedelta(seconds=seconds)


    def add_coins(self, coin, number):

        try:
            self.number_coins_checking(number)

        except NegativeNumberOfCoins:
            raise NegativeNumberOfCoins

        pennies = int(coin * 100)

        number = int(number)

        Mon = Money(coin)

        self._ListOfCoins.append(Mon)

        for i in range(number):

            for x in range(pennies):

                if self._Sum < 2.0:
                    self.leaving_time(18)

                elif self._Sum < 6.0:
                    self.leaving_time(9)

                else:
                    self.leaving_time(7.2)

        self.counting_coins(coin, number)


    def get_license_plate(self, value):

        value = value.rstrip('\n')
        format = compile("^[\w\ ]*$")

        if format.match(value) is not None and 4 < len(
                value) <= 11 and value:

            value = value.replace(' ', '').upper()

            self._rejestracja = value

        else:
            raise WrongLicensePlate

        return self._rejestracja


    def actual_time_change(self, year, month, day, hour, minutes, seconds):

        a = datetime.strptime(str(year + ' ' + month + ' ' + day), '%Y %m %d')
        b = a.replace(hour=hour, minute=minutes, second=seconds)

        self._Actual_Time = b

        self._Leaving_Time = self._Actual_Time

        self._Sum = 0

        return self._Leaving_Time


    def get_actual_time(self):
        return self._Actual_Time


    def get_leaving_time(self):
        return self._Leaving_Time


    def confirm(self,license_plate):

        self.get_license_plate(license_plate)

        if self._Sum == 0:
            raise NoMoneyGiven

        lic = 'License plate: ' + self.get_license_plate(license_plate) + '\nDate of purchase: ' + str(self.get_actual_time()) \
              + '\nDate of departure: ' + str(self.get_leaving_time())

        self._Sum = 0

        self._Leaving_Time = self._Actual_Time

        return lic