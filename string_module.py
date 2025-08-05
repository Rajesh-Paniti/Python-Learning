import string

# print(string.punctuation)   #special characters
# print(string.ascii_letters)
# print(string.digits)
# print(string.ascii_lowercase)
# print(string.whitespace)

email = input("Enter your email")
password = input("Enter your password")

has_digit = any(dgt in string.digits for dgt in password)
has_punctuation = any(pnt in string.punctuation for pnt in password)

if has_digit and has_punctuation:
    print("The password is strong")