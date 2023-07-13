#area of triangle
# hb=int(input("enter the number :"))
# b=int(input("enter the number :"))
def triangle(hb,b):
    area_of_triangle=(hb*b/2)
    return area_of_triangle
print(triangle(22,12))

# area_of_triangle=(hb*b/2)
# print(area_of_triangle)

# AREA OF SQUARE
def square(a):
    area_of_square=a**2
    return area_of_square
print(square(5))


#AREA OF RECTANGLE
def rectangle(w,l):
    area_of_rectangle=w*l
    return area_of_rectangle
print(rectangle(10,25))

#AREA OF CIRCLE
def circle(r):
    area_of_circle=(3.14*r**2)
    return area_of_circle
print(circle(10))

#AREA OF TRAPEZIUM
def trapeizum(a,b,h):
    area_of_trapezium=(((a+b)/2)*h)
    return area_of_trapezium
print(trapeizum(2,12,6))