
def sum(x,y):
    """Returns the sum of two vectors. The inputs x and y are lists of floats
    representing vectors of the same length. Function uses list comprehension."""
    return [i+j for i,j in zip(x,y)]

def diff(x,y):
    """Returns the difference of two vectors (i.e. x-y). The inputs x and y are
    lists of floats representing vectors of the same length. Function uses 
    list comprehension."""
    return [i-j for i,j in zip(x,y)]

def scale(x,c):
    """Returns the scalar multiplication of a vector and a scalar.
    The input x is a list of floats representing a vector, and the
    input c is a float representing a scalar. Function ses list comprehension."""
    return [c*i for i in x]

def lincomb(xList, cList):
    """Returns the linear combination of a set of vectors and a set of scalars.
    The input xList is a list of lists of floats representing vectors.
    The input cList is a list of floats representing scalars. These lists
    should be of the same length. Function uses list comprehension."""  
    result=0.0
    for x,c in zip(xList,cList):
        for ele in x:
            result=result+(ele*c)
    return result

def dot(x,y):
    """Returns the dot product between two vectors. The inputs x and y are
    lists of floats representing vectors of the same length. Uses list comprehension."""
    result=0.0
    for i,j in zip(x,y):
        result=result+(i*j)
    return result

def proj(x,y):
    """Returns the projection of x onto y. The inputs x and y are lists of 
    floats representing vectors of the same length. Uses list comprehension."""
    return [(dot(x,y)*i)/dot(y,y) for i in y]

def perp(x,y):
    """Returns the perpendicular vector to y of length x. The inputs x and y are
    lists of floats representing vectors of the same length. Uses list comprehension."""
    projxOntoY=proj(x,y)
    return [i-j for i,j in x,projxOntoY]

def refl(x,y):
    """Returns the reflection of x across y. The inputs x and y are lists of 
    floats representing vectors of the same length. Uses list comprehension."""
    y_perp_by2=[2*i for i in perp(x,y)]
    return [i+j for i,j in zip(x,y_perp_by2)]

def angle(x,y,s=1):
    """Returns the angle between two vectors. The inputs x and y are
    lists of floats representing vectors of the same length. Uses list comprehension.
    The input s is an optional parameter: 'r' for radians, 'd' for degrees, none for default."""
    import math
    if s is 'r':
        return (math.acos(dot(x,y)/((dot(x,x)**(0.5))*(dot(y,y)**(0.5)))))*(math.pi/180)
    elif s is 'd':
        return math.acos(dot(x,y)/((dot(x,x)**(0.5))*(dot(y,y)**(0.5))))
    elif s is 1:
        return (math.acos(dot(x,y)/((dot(x,x)**(0.5))*(dot(y,y)**(0.5)))))*(math.pi/180)


