class Rectangle:
  width = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return type(self).__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def get_area(self):
    return self.width * self.height

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return type(self).__name__ + "(side=" + str(self.width) + ")"
