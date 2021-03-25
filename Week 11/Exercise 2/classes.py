class RightTriangle:
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
        if self.base <= 0 or self.height <= 0:
            print("\nERROR: Unexpected values, using default ones instead.")
            self.base = 1.0
            self.height = 1.0

    def getArea(self):
        return (self.base * self.height)/2
            