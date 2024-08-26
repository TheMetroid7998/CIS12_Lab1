import math
print ("Problem 1: Arithmetic Operations")
print ("The area of a circle with a radius of 5 is", round((math.pi*5**2), 2), ".")
print ("The volume of a sphere with a radius of 3 is", round(((4/3)*math.pi*3**3), 2), ".")
#For some reason this took ages to get right and even now I still don't know what I did that fixed it...
print ("The hypotenuse of a right-angled triangle with sides 3 and 4 is", str(math.sqrt(3**2 + 4**2)), ".")
print ("Problem 2: String Manipulation")
FullName = "Conrad Jazen Salazar"
print ("My name,", "Conrad", "Jazen", "Salazar,", "consists of", len(FullName), "characters.")
#You would think that I would have to put the variable in the parentheses but that didn't work.
print ("This is my name in uppercase:", FullName.upper())
print ("This is my name in lowercase:", FullName.lower())
print ("Problem 3: Variable & Data Types")
Age = 19
Height = 6
Weight = 185
print ("Age is:", type(Age), ".")
print ("Height is:", type(Height), ".")
print ("Weight is:", type(Weight), ".")
BMI = (Weight/(Height*12)**2)*703.
print ("My BMI is", round(BMI, 2), ".")