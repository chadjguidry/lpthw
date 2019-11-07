# Function to caclulate area of a triangle
def calculate_triangle_area(base, height):
    return (base * height) / 2

# Ask the user for the triangle dimensions
tri_base = int(input("Enter the length of the base of your triangle: "))
tri_height = int(input("Enter the height of your triangle: "))

# Print the area of the triangle
print(f"\nThe area of the triangle is {calculate_triangle_area(tri_base, tri_height)}.")
