password = input("Enter your password: ")

length = len(password)
has_upper = False
has_lower = False
has_number = False
has_symbol = False

symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_number = True
    if ch in symbols:
        has_symbol = True

score = 0
if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_number:
    score += 1
if has_symbol:
    score += 1

print("\n----- Password Report -----")
print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Number:", has_number)
print("Symbol:", has_symbol)

if score <= 2:
    print("Password Strength: Weak")
elif score in (3, 4):
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")