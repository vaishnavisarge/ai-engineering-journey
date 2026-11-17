# Strings is immutable collection of character that means we cannot change individual characters of string
str1= "Welcome Yash"
print(str1)

#string slicing
print(str1[0:7])            #it exclude last index

#accessing characters of string
for char in str1:
    print(char)

#length of string
print(len(str1))

#STRING METHODS:

str2="Mango"

#Upper case:
print("Upper Case:",str2.upper())

#Lower case:
print("Lower Case:",str2.lower())

#Remove trailing characters fromg string eg. !
str3="Hello World...!"
print("Removing special characters:",str3.rstrip("!"))

#Replacing all occurence of string with another
print("Replacing World with India:", str3.replace("World","India"))

#Split is used to split given string at specified instance & returns separated string as list
print("Splitting string into list",str3.split(" "))

#Capitialize is used to capitialize only first character of string rest first letter of words
# gets converts into small letter
str4="hi Vaishnavi"
print("Capitalize string:", str4.capitalize())

#center is used to align string to center as per parameters given by user
print(f"Center method: {str4.center(50)}")

#count returns the number of times given value has occured within given string
str5="Helllooo Jimmmmyyy"
print(f"Count occurence of characters:{str5.count("l")} {str5.count("m")}")

#endswith checks if string ends with given value and return true or false
print(f"endswith(): {str5.endswith("y")}")

#find() searches for first occurence of given value and returns index where it is present
#if value is not present it returns -1
print(f"Find value J in string: {str5.find("J")}")

#index() it is similar to find() except it throws error if the given value is not present in string

#isalnum() returns true only if entire string contains only alphabets and 0-9 numbers
# Spaces and special characters are not allowed.
str6="hello"
print(f"hecking whether string is alpha: {str6.isalnum()}")

#isapha() returns true only if entire string contains only alphabets 
#Spaces, numbers and special characters are not allowed.
str7="HI WELCOME TO PYTHON Learning"
print(f"Checking whether string contains only alphabets: {str7.isalnum()}")

