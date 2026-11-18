password=input("Create password: ")
if len(password)<6 :
    print(f"{password} is too short ")
elif password.isalnum():
    print(f"{password} should contain special character and symbol")
elif password.isalpha():
    print(f"{password} should contain numbers")
elif password.islower():
    print(f"{password} should contain capital letter")
else:
    print(f"{password} is created succesfully!")

