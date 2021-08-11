print(".........Enter the numbers for LCM........")

a = int(input("Enter the 1st Number="))
b = int(input("Enter the 2nd Number="))


for z in range(1, a * b + 1):
    if z % a == 0 and z % b == 0:
        print("The LCM of the Two Num. is=", z)
        break
