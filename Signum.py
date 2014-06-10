class Signum:
    def __init__(self):
        self.x = 0
    def sgn(self, x):
        self.x = x
        if self.x < 0 :
            return -1
        elif self.x == 0 :
            return 0
        else:
            return 1
