from shape import Shape

class Circle(Shape):
    def draw(self):
        return (f"Drawing circle {self.color.fill()}")