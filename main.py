from decimal import *


dzienTygodnia = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

class Pieniadze():

    def __init__(self, val):
        val = Decimal(float(val)).quantize(Decimal('.01'), rounding = ROUND_DOWN)
        nominaly = list(map(Decimal, ['0.01', '0.02', '0.05', \
                                     '0.1', '0.2', '0.5', '1', '2', '5', '10', '20', '50']))
        if val in nominaly:
            self._val = val
        else:
            raise Exception

    def get_val(self):
        return self._val


