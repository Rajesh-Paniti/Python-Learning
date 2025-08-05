a = int(input("Enter a number"))

if a > 10:
    print(a)

else:
    print("Number is very small")

s = input("Enter your name: ")
l = len(s)

print("Your name is ")
for i in s:
    print(i, end= "")

numbers = [0, 1, 0, 0, 0]

if any(num > 0 for num in numbers):
    print("At least one number is not 0")