password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    print("Password length is good")
    score += 1
else:
    print("Password is too short")

# Number Check
if any(char.isdigit() for char in password):
    print("Contains number")
    score += 1
else:
    print("No number found")

# Uppercase Check
if any(char.isupper() for char in password):
    print("Contains uppercase letter")
    score += 1
else:
    print("No uppercase letter found")

# Lowercase Check
if any(char.islower() for char in password):
    print("Contains lowercase letter")
    score += 1
else:
    print("No lowercase letter found")

# Special Character Check
if any(not char.isalnum() for char in password):
    print("Contains special character")
    score += 1
else:
    print("No special character found")

print("Score =", score)

# Final Result
if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")