# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math
def distance_function(point1, point2):
    x1, y1, z1, *_ = point1
    x2, y2, z2, *_ = point2

    return math.sqrt((x2-x1)**2 + (y2 - y1)**2 + (z1 - z2)**2)


# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
def main():
    print("Hello! Please enter two sets of two coordinates. ")
    for n in range (2):
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        z = int(input("Enter z coordinate: "))
        if n == 0:
            point1 = (x,y,z)
        else:
            point2 = (x,y,z)


    distance = distance_function(point1, point2)
    print(f"The distance between the two points is: {format(distance, ".2f")}")

main()