class FieldElements: 
  # Range(0, prime-1)
  def __init__(self, num, prime):
    self.num = num
    self.prime = prime
    if num >= prime or num < 0:
      raise ValueError("{} is not in the range 0 to {}".format(num, prime - 1))

  def __repr__(self) -> str:
      return "FieldElements_{}{}".format(self.num, self.prime)

  # 用__eq__來比較value. python中使用==來比較class的instance時，會自動call __eq__ method
  # object.__eq__(self, other)
  # x == y calls x.__eq__(y)
  '''
  注意比較時，搞清是比較值，還是內存
  '''
  def __eq__(self, other) -> bool:
      if other is None:
        return False
      return other.num == self.num and other.prime == self.prime 
      # == 比較'值'是否相等，equality
      ''' a = [1,2,3]
      b = a 
      c = a[:]
      a == b -> true, a == c -> true
      '''
      # a is b -> true, a is c -> false
      # 'is'比較兩個variables是否指向相同的reference, 如果兩個object的內存地址相同，則True
      # 'is' check identity
      

  def __ne__(self, other) -> bool:
      return not(self == other)

  def __add__(self, other):
    if self.prime != other.prime:
      raise ValueError("Cannot add two number in different field")
    
    # result = (self.num + other.num) % self.prime
    # return self.__class__(result, self.prime)
    '''
    我們希望return的是一個新的class，可以方便inheritance
    eg: a = FieldElements(3,11)
        b = FieldElements(4,11)
        c = a + b --> c = FieldElements(7,11)
    為了return an instance of a class, 所以用return self.__class__(num, self.prime)
    return self.__class__(result, self.prime)會error: 
    AttibuteError: "FieldElements" has no attribute 'result'
    '''
    num = (self.num + other.num) % self.prime
    return self.__class__(num, self.prime)

  def __sub__(self, other):
    if self.prime != other.prime:
      raise ValueError("Cannot add two number in different field")
    num = (self.num - other.num) % self.prime
    return self.__class__(num, self.prime)
    # return result

  def __mul__(self, other):
    if self.prime != other.prime:
      raise ValueError("Cannot add two number in different field")
    num = (self.num * other.num) % self.prime
    return self.__class__(num, self.prime)

  def __pow__(self, other):
    n = exponent % (self.prime - 1)
    num = pow(self.num, n, self.prime)
    return self.__class__(num, self.prime)
  
  def __truediv__(self, other):
    if self.prime != other.prime:
      raise ValueError("Cannot divide two numbers in different field")
    num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
    return self.__class__(num, self.prime)
