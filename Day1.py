total = 0

for line in open("input.txt"):
    digits = [char for char in line if char.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)

# We open the document and read line by line
# Declare digits, use a list comprehension to find the digits
# Make sure the digits are ints, and take 1st and last sum