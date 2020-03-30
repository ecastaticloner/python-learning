class Point:
    def __init__(self ,x ,y):

        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print("draw")


point1 = Point(23,5)
point1.draw()
#point1.x = 12
#point1.y = 23
print(point1.x)
print(point1.y)

point2 = Point(5,2)
#point2.x = 2
print(point2.x)

point = Point(23,56)
point.x = 11
print(point.x)