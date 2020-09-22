import math

class Vector:

  def __init__(self, dim, f):
    self.n = dim
    self.f = {} #initialize set for dict
    for key, value in f.items():
      if value != 0:
        self.f[key] = value

  def __neg__(self):
    result = {}
    for key in self.f.keys(): #just iterate over the keys of self.f, nonzero only!
      result[key] = -1 * self.f[key]
    return Vector(self.n, result)

  def __add__(self, other):
    try:
      result = {}
      for key in range(self.n): #simple way to iterate over the keys of both vectors
        if self.f.get(key) in self.f.values():
          if other.f.get(key) in other.f.values():
            result[key] = self.f[key] + other.f[key]
          else:
            result[key] = self.f[key]
        else:
          if other.f.get(key) in other.f.values():
            result[key] = other.f[key]
          else:
            continue
      return Vector(self.n, result)
    except AttributeError:
      print("AttributeError: Object does not have attribute for addition operation")
    except TypeError:
      print("TypeError: Cannot convert object to vector class for addition operation")

  def __sub__(self,other):
    try:
      result = {}
      for key in range(self.n): #simple way to iterate over the keys of both vectors
        if self.f.get(key) in self.f.values():
          if other.f.get(key) in other.f.values():
            result[key] = self.f[key] - other.f[key]
          else:
            result[key] = self.f[key]
        else:
          if other.f.get(key) in other.f.values():
            result[key] = -other.f[key]
          else:
            continue
      return Vector(self.n, result)
    except AttributeError:
      print("AttributeError: Object does not have attribute for subtraction operation")
    except TypeError:
      print("TypeError: Cannot convert object to vector class for subtraction operation")

  def __mul__(self, other):
    result = {}
    if type(other) == Vector: #check if both are vectors, then calc dot prod
      for key in self.f.keys(): #just iterate over the keys of self.f, nonzero only!
        if key in other.f.keys():
          result[key] = self.f[key] * other.f[key]
        else:
          continue
      return sum(result.values())
    elif type(other) == int or type(other) == float:
      for key in self.f.keys(): #just iterate through keys of self.f
        result[key] = other * self.f[key]
      return Vector(self.n, result)

  def __rmul__(self, other):
    return self.__mul__(other)

  def __truediv__(self, other):
    try:
      result = {}
      if type(other) == int or type(other) == float:
        for key in self.f.keys(): #just iterate through keys of self.f
          result[key] = self.f[key] / other
      return Vector(self.n, result)
    except ZeroDivisionError:
      print("ZeroDivisionError: Cannot divide by zero")

  def norm(self):
    return math.sqrt(sum(self.f[key]**2 for key in self.f.keys()))

  def proj(self, other):
    return ((self * other) / (other.norm()**2)) * other

  def __str__(self):
    dimenString = ''
    valString = ''
    for key,val in sorted(self.f.items()):
      tempDimen = '  ' + str(key)
      tempVal = '  ' + str('{:>-0.5g}'.format(val))
      tempDimen = (len(tempVal) - len(tempDimen))*' ' + tempDimen
      dimenString += tempDimen
      valString += tempVal
    bar = len(dimenString)*'-'
    return dimenString[2:] + '\n' + bar + '\n' + valString[2:] + '\n' + 'dimension = ' + str(self.n) + '\n'
