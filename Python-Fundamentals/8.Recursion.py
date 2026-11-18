#a function calling itself is known as recursion
num= int(input("Enter a number: "))
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
if num <0:
    print("Factorial not defined")
else:
    print(f"Factorial is {fact(num)}")