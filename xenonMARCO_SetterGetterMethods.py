class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value


# create object
rect = Rectangle(10, 5)

# getter
print("Width:", rect.width)
print("Height:", rect.height)

# setter
rect.width = 20
rect.height = 15

print("\nAfter changing values:")
print("Width:", rect.width)
print("Height:", rect.height)