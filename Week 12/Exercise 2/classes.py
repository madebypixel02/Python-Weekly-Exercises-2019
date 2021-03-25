class Rectangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        if self.__base == self.__height:
            self.__square = True
            self.__shape = "square"
        else:
            self.__square = False
            self.__shape = "rectangle"

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self, value):
        self.__base = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    def area(self):
        return self.__base * self.__height

    def perimeter(self):
        return 2*self.__base + 2*self.height

    def biggestSide(self):
        if self.__base > self.__height:
            return self.__base
        else:
            return self.__height

    def squarefy(self):
        if self.__base > self.__height:
            self.height = self.__base
            return False
        elif self.__height > self.__base:
            self.base = self.__height
            return True


    def toString(self):
        return "A " + str(self.__base) + "x" + str(self.__height) + " " +self.__shape

    def equals(self, rectangle1, rectangle2):
        return (rectangle1.base == rectangle2.base and rectangle1.height == rectangle2.height) or (rectangle1.base == rectangle2.height and rectangle1.height == rectangle2.base)




