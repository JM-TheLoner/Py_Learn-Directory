#having the first letter in the class name capitalized is called pascal naming convention 
#conventions used to name classes is different than for lists and others. eg: List name = point_system
                                                                             #class name = PointSystem

class Point:

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


Point1 = Point()
Point1.x = 10
Point1.y = 20             
print(Point1.x)
Point1.move()

