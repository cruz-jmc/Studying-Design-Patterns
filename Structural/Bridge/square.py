from shape import Shape

#Defining Square shape (that don't know concrete implementation of color)
class Square(Shape):

    def draw(self):
        return (f"Drawing square {self.color.fill()}")