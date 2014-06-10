class Natural:
    def __init__(self):
        self.num = 0
    def isNatural(self, num):
        self.num = num
        if (num > 1 and num%1 == 0):
            return True
        else:
            return False
