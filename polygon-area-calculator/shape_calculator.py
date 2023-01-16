class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * (self.width + self.height))

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width >50 or self.height>50:
      return "Too big for picture."
    return (self.width * "*" + "\n") * self.height

  def get_amount_inside(self, rectangle):
    n1=self.width//rectangle.width
    n2=self.height//rectangle.height
    return n1*n2

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

# the Square class where i was dying ;)
class Square(Rectangle):
  def __init__(self, side):
    super(Square, self).__init__(side, side)
    self.width=side
    self.height=side

  def set_side(self, new_side):
    self.width=new_side
    self.height=new_side
    

  def __repr__(self):
    return f"Square(side={self.width})"
