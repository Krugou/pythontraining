# calculate the area of circle  

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

def main():
    print("Welcome to the area of circle calculator")
    radius = int(input("Enter the radius of the circle: "))
    print("Area of circle: ", area_of_circle(radius))

main()






