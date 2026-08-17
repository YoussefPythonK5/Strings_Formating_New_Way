name = "Youssef"
age = 17
rank = 10
print("My Name is: " + name)
#print("My name is: " + name + "My age is: " + age) # Error
print("My Name is: {:s}".format(name))
print("My Name is: {:s} And My Age is: {:d}And My rank is: {:f}".format(name, age, rank))

# {:s} = String
# {:d} = Number
# {:f} = Float
print("*"*10)

n = "Youssef"
l = "Python"
y = 10
print("My Name is {:s} And Iam {:s} Developer with {:d} Years Exp" .format(n, l, y))
print("*"*15)
# Control Floating Point Number
myNumber = 10
print("myNumber is: {:d}".format(myNumber))

print("myNumber is: {:f}".format(myNumber))

print("myNumber is: {:.2f}".format(myNumber))
print("*"*20)

# Truncate String اشيل الحاجات الي انا مش عايزها واسيب الي انا عايزه

myLongString = "Hello peoples of Elzero Web School I Love you All"
print("Massage is {:s}".format(myLongString))

print("Massage is {:.5s}".format(myLongString))

print("Massage is {:.13s}".format(myLongString))
print("*"*25)

# Format Money
myMoney = 500828264938
print("My Money in Bank Is: {:d}".format(myMoney))

print("My Money in Bank is: {:_d}".format(myMoney))

print("My Money in Bank is: {:,d}".format(myMoney))

# print("My Money in Bank is: {:&d}".format(myMoney)) # Wrong
print("*"*30)

# ReArrange Items
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))
print("Hello {2} {0} {1}".format(a, b, c))
print("Hello {1} {2} {0}".format(a, b, c))

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {2:d} {0:d} {1:d}".format(x, y, z))
print("Hello {1:f} {2:f} {0:f}".format(x, y, z))
print("Hello {1:.2f} {2:.5f} {0:.4f}".format(x, y,z))
print("*"*35)

# Format in Version 3.6+
myName = "Osama"
myAge = 17
print("My Name is :  {myName} and myAge is : {myAge} ")
print(f"My Name is : {myName} and myAge is : {myAge}")