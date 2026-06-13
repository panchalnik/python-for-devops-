# 22/05/026
# Calculate area of a triangle
def area(a,b):
    area=1/2*a*b
    # print("The area of the triangle:")
    return area
res=area(10,6)
print("The area of the triangle:",res)


# Calculate perimeter of a square
def square_perimeter(a):
    print("Side of square is:",a)
    perimeter_of_square=4*a
    return perimeter_of_square
res=square_perimeter(9)
print("The Perimeter of square:",res)


# Calculate diameter of a circle
def dia(a):
    print("The radius of circle is:",a)
    x=a*2
    return x
res=dia(14)
print("The diameter of respective circle is:",res)


# Calculate volume of a cube
def volume(a):
    # pass
    print("The side of cube is:",a)
    vol=a**3
    return vol
res=volume(5)
print("The volume of cube is:",res)


# Calculate surface area of a cuboid
def surface_area(a,b,c):
    # pass
    print("The length of cuboid is:",a)
    print("The breadth of cube is:",b)
    print("The height of cuboid is:",c)
    x=2*(a*b + b*c + c*a)
    return x
res=surface_area(4,3,2)
print("The surface area of cuboid is:",res)

# MATHEMATICAL EXPRESSION
# Square of sum: (x + y)²
def square(x,y):
    # pass
    print("The value of x and y is :",x , y)
    exp=x**2 + y**2 + 2*x*y
    return exp

res=square(5,7)
print("The result of following expression is:",res)

# Simplify expression: x² - 4x + 4
def simplify(x):
    # pass
    print("The value of x is :",x)
    exp=x**2 - 4*x +4
    return exp

res=simplify(3)
print("The following expression after simplification:",res)


# Evaluate: (a + b)(a - b)
def evaluate(a,b):
    # pass
    print("The value of a and b is :",a  , b)
    e=(a + b)*(a - b)
    return e

res=evaluate(6,2)
print("The value of expression is:",res)


# Sum of cubes: a³ + b³
def sum_of_cube(a,b):
    # pass
    print("The value of a and b is :",a  , b)
    exp=a**3 + b**3
    return exp

res=sum_of_cube(1,2)
print("The sum of cubes:",res)


# Simplify: (x - y)²
def simplify(x,y):
    # pass
    print("The value of x and y is:",10 , 6)
    exp=(x - y)**2
    return exp

res=simplify(10,6)
print("The value of following expression is:",res)


# Difference of cubes: x³ - y³
def difference(x,y):
    # pass
    print("The value of x and y is:", x , y)
    exp=x**3 - y**3
    return exp
res=difference(4,1)
print("The differnece of cubes is:",res)
