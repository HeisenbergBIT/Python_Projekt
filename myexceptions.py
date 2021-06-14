class NegativeNumberOfCoins(Exception):
    def __init__(self, massage="Negative number of coins"):
        self.massage = massage
        super().__init__(self.massage)

class NonintigerNumberOfCoins(Exception):
    def __init__(self, massage="Nonintiger number of coins"):
        self.massage = massage
        super().__init__(self.massage)

class NoMoneyGiven(Exception):
    def __init__(self, massage="No money given"):
        self.massage = massage
        super().__init__(self.massage)

class WrongLicensePlate(Exception):
    def __init__(self, massage="Wrong license plate"):
        self.massage = massage
        super().__init__(self.massage)

class ParkomatOverflow(Exception):
    def __init__(self, massage="Parkomat overflow"):
        self.massage = massage
        super().__init__(self.massage)

class WrongValue(Exception):
    def __init__(self, massage="Wrong value"):
        self.massage = massage
        super().__init__(self.massage)