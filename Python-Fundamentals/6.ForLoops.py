#basic example
# for k in range(1,5):
#     print(k+1)

# for k in range(1,12,2):         # 1=start, 12=end , 2= updation or constant 
#     print(k)

# 1.students attendance short program
# students=["neha","priya","yash","abhi","seema"]
# attendance=["P","A","A","P","P"]
# present=0
# absent=0

# for i in range(len(students)):
#     if(attendance[i]=="P"):
#         present=present+1
#     else:
#         absent+=1

#     print(f"{students[i]}: {attendance[i]}")

# print(f"Total present count: {present}")
# print(f"Total absent count: {absent}")


#2. Dupliacte character checker:
# word = input("Enter word: ")
# checked = []

# for char in word:
#     if word.count(char) > 1 and char not in checked:
#         print(f"{char} is repeated {word.count(char)} times")
#         checked.append(char)


#3. Occurence of each character in string
string = input("Enter string: ").lower()

#python is case-sensitive so it create capital and small character differently that's why
# we need lower()

# we will use dictionary here to store occurence of character in key value pair each
frequency={}
for char in string:
    if char in frequency:
        frequency[char]=frequency[char]+1
    else:
        frequency[char]=1 

print(frequency)