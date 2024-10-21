class shape:
  def __init__(self,name,sides):
    self.name=name
    self.sides=sides

    def area(self):
      pass

    def perimeter(self):
      pass

class square(shape):
  def __init__(self,name,sides):
    super().__init__(name,sides)

    def area(self):
      return self.sides**2

    def perimeter(self):
      return 4*self.sides

class Circle(shape):
    def __init__(self,name,radius):
        super().__init__(name,radius)

    def area(self):
          return 3.14*self.sides**2

    def perimeter(self):
          return 2*3.14*self.sides

class Rectangle(shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    # For a generic triangle, we might need additional information to compute the perimeter
    # If the triangle is equilateral, we can simply do: 3 * side_length
    # Here we use the base as 'side_length' for simplicity in the case of an equilateral triangle
    def perimeter(self):
        # Assuming it's an equilateral triangle for simplicity
        return 3 * self.base