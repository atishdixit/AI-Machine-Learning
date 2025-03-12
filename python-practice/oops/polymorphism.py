class Square:

    def __init__(self, height=0, width=0):

        self.height = height
        self.width = width

    @property
    def height(self):
        print("retrieving height")
        return self.height

    @property
    def width(self):
        print("retrieving width")
        return self.width

    def getArea(self):
        return int(self.height) * int(self.width)


def main():
    square = Square()
    square.width = 100
    square.height = 100
    # print("height", square.height)
    # print("width", square.width)
    print("Area ", square.getArea())


main();
