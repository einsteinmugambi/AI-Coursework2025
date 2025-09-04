def calculate_area(side):
   
    return side ** 2

def calculate_perimeter(side):
    
    return 4 * side

side_length = float(input("Enter the side length of the square: "))

area = calculate_area(side_length)
perimeter = calculate_perimeter(side_length)


print(f"Area of the square: {area}")
print(f"Perimeter of the square: {perimeter}")