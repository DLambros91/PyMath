class Natural:
    def __init__(self):
        self.num = 0
    def isNatural(self, num):
        self.num = num
        if (self.num > 1 and self.num%1 == 0):
            return True
        else:
            return False
