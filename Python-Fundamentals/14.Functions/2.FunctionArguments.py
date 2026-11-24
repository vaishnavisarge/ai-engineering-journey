# 1.Default Arguments
# We can provide default values while creating a function. 
# This way the function assumes default values even if it is not provided in function
# call for that argument
def avg(a=9,b=10):
    print((a+b)/2)
avg(1,5)  
#here output is based on final argument passed during function calling if values are not at
# function calling then function will take default arguments
def avg(a=9,b=1):
    print((a+b)/2)
avg(b=5)



# 2.Keyword Argument
# Here we can change the order of arguments by providing key-value argument
def name(fname, mname,lname):
    print(fname,mname,lname)
name(mname="Peter", lname="Wesker",fname="Jade")
#Here we dont need to remeber the order of argument but output will we printed as per 
# it is defined at function declaration


# 3.Required Argument
# In case we dont pass argument wiyh key-value syntax, then it is necessary to pass argument
# in correct positional order and number of arguments passed should match with actual function definition
# def name(fname,mname,lname):
#     print(fname,mname,lname)
# name("Peter","Quil")


# 4.Variable length argument
# we can pass multiple values here, than the which is defined in function
# There are 2 sub-types of Variable length argument

# i)Arbitrary Arg
# it is tuple type we can add multiple values here
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(f"Average: {sum/len(numbers)}")
average(10,20,30)

# ii)Keyword Arbitrary Arg
# it is dict type we can pass values in key-value pair here
def name(**name):
    print(
        name["fname"], name["mname"], name["lname"]
    )
name(mname="xyz",lname="pqr",fname="abc")

