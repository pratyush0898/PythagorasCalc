import math

print("Pythagorean theorem calculator \n  \n")


while True:
        h = int(input("Enter the height of the triangle: "))
        b = int(input("Enter the base of the triangle: "))  

        hs = h**2
        bs = b**2

        hb = hs+bs

        ans = math.sqrt(hb)

        print("\n The Hypotenuse of Pythagorean theorem is " , ans, "\n \n \n \n")
 