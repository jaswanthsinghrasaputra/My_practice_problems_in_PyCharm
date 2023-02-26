
# program to line that passing through given points
# def Line(p,q):
#     a = q[1] - q[0]
#     b = p[0] - p[1]
#     c = a * (p[0]) + b * (p[1])
#     if(b<0):
#         print(a,-1*b,c)
#     else:
#         print(a,b,c)

# p = list(map(int,input().split()))
# q = list(map(int,input().split()))
# Line(p,q)

# Program for Point of Intersection of Two Lines

# def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
#     # calculate the slopes of the lines
#     m1 = (y2 - y1) / (x2 - x1)
#     m2 = (y4 - y3) / (x4 - x3)
#
#     # check if the lines are parallel
#     if m1 == m2:
#         return None
#
#     # calculate the y-intercepts of the lines
#     b1 = y1 - m1 * x1
#     b2 = y3 - m2 * x3
#
#     # calculate the x and y coordinates of the point of intersection
#     x = (b2 - b1) / (m1 - m2)
#     y = m1 * x + b1
#
#     return (x, y)
#
# x1, y1, x2, y2 = list(map(int,input().split()))
# x3, y3, x4, y4 = list(map(int,input().split()))
# print(intersection(x1, y1, x2, y2, x3, y3, x4, y4))

# import math
# def find_points(x0, y0, L, M):
#     # calculate the angle between the line and the x-axis
#     angle = math.atan(M)
#
#     # calculate the x and y coordinates of the points
#     x1 = x0 + L * math.cos(angle)
#     y1 = y0 + L * math.sin(angle)
#     x2 = x0 - L * math.cos(angle)
#     y2 = y0 - L * math.sin(angle)
#
#     return (x1, y1), (x2, y2)
#
# x0, y0 = list(map(int,input().split()))
# L = int(input())
# M = int(input())
# print(find_points(x0, y0, L, M))

# Check whether a given point lies inside a triangle or not
""""
Let the coordinates of three corners be (x1, y1), (x2, y2) and (x3, y3).
And coordinates of the given point P be (x, y)
Calculate area of the given triangle, i.e., area of the triangle ABC in the above diagram.
Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2
Calculate area of the triangle PAB. We can use the same formula for this. Let this area be A1.
Calculate area of the triangle PBC. Let this area be A2.
Calculate area of the triangle PAC. Let this area be A3.
If P lies inside the triangle, then A1 + A2 + A3 must be equal to A.
"""



# Number of parallelograms when n horizontal parallel lines intersect m vertical parallel lines

n = 5
m = 5
num_parallelograms = (n-1) * (m-1)
print(num_parallelograms)

"""
need to learn all shapes areas and perimeters and volumns including 3D shapes carefully 
"""