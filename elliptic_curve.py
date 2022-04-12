class Point:
  # y**2 = x**3 + ax + b
  def __init__(self, x, y, a, b):
    self.x = x 
    self.y = y 
    self.a = a
    self.b = b
    if y**2 != x**3 + a*x + b:
      raise ValueError("({}, {}) is not on the curve".format(x, y))
    
  def __eq__(self, other) -> bool:
      return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

  def __ne__(self, other) -> bool:
      return self.x != other.x or self.y != other.y or self.a != self.a or self.b != other.b

      


