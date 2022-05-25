#Write /execute simple ‘Python’ program: calculate the area and perimeter of the Square, and the volume & perimeter of the cone
import math
s=int(input("Enter side of square: "))
area=s*s
perimeter=4*s
print("AREA OF SQUARE IS ",area,"AND PERIMETER IS ",perimeter)


# Calculate the Volume
radius=int(input("Radius of Cone : "))
height=int(input("Height of Cone : "))
Volume = (1.0 / 3) * math.pi * radius * radius * height
print("VOLUME OF CONE IS ",Volume)