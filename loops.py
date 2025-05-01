value = int(input("Please enter a number 10: "))
while (value != 10):
    print("Entered number is not equal to 10")
    print("Please try it again")
    value = int(input("Enter number 10: "))
print("Thank you!")
print("You entered a value of 10")

x = int(input("Pls enter positive integer: "))
while x > 0:
    print("***")
    x = x - 3
print("The end!")

for i in range(5):
    print(i)

n = 8 
sum = 0
for i in range(n):
    sum = sum + i
    print("Adding: ",i, "to previous sum:", sum)

strval = "forever"
e_count = 0
for letter in strval:
    print(letter)
    if letter == "e":
        e_count = e_count+1
print("The letter e occured: ",e_count, "times")