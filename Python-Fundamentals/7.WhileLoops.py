#simple program
# i=5
# while(i<10):
#     print(i)
#     i=i+1

#atm pin
pin= 146
attempts=0

while attempts<3:
    entered_pin = int(input("Enter pin: "))
    if(entered_pin==pin):
        print(f"Login successfull!")
        break
    else:
        attempts=attempts+1
        print(f"Login failed..")
if attempts==3:
    print("Maxiumu attempts reched. Accound Locked  ")

