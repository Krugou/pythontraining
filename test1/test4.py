# calculate the area of triangle
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area
def main():
    print("Welcome to the area of triangle calculator")
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    print("Area of triangle: ", area_of_triangle(base, height))
main()

#



