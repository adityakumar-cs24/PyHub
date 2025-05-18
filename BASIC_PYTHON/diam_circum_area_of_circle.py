import math
radius = float(input("Enter radius of the circle : "))
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print("Diameter : ", diameter)
print(f"Circumference : {circumference:.2f}")
print(f"Area : {area:.2f}") 