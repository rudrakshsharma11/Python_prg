print(".........Enter the two numbers..........")
num1 = int(input("Enter the 1st nos="))
num2 = int(input("Enter thr 2nd nos="))
while num1 % num2 != 0:
    rem = num1 % num2
    num1 = num2
    num2 = rem

print("The HCF is=", num2)
