# String formatting in Python
# There are several ways to format strings in Python:
# 1. Using % operator (old style)
# 2. Using .format() method (new style)
# 3. Using f-strings (Python 3.6+)

# 1. Using % operator
name = "ABC"  
age = 30
str = "My name is %s and I am %d years old." % (name, age)
print(str)

# 2. Using .format() method
str = "My name is {} and I am {} years old.".format(name, age)
print(str)


# 3. Using f-strings
str = f"My name is {name} and I am {age} years old."
print(str) 

# Formatting Numbers in Python:  Number formatting means controlling how numbers look when printed
#                                (like decimals, width, commas, currency, alignment, etc.)

# Decimal places (float precision)
# Syntax : {value:.nf} where n is the number of decimal places
pi = 3.141592653589793
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

# Width and alignment
# Syntax : {value:width} for right alignment (default)
#          {value:<width} for left alignment
#          {value:^width} for center alignment

print(f"Right aligned: '{name:>10}'")
print(f"Left aligned: '{name:<10}'")
print(f"Center aligned: '{name:^10}'")

# Zero padding 
# Syntax : {value:0width}
number = 42
print(f"Zero padded number: {number:05}")

# Comma as thousand separator
# Syntax : {value:,}
large_number = 1234567890
print(f"Large number with commas: {large_number:,}")

# Currency formatting
# Syntax : {value:,.2f} for 2 decimal places and commas
price = 1234.567
print(f"Price formatted as currency: Rs{price:,.2f}")

# Percentage formatting
# Syntax : {value:.2%} for percentage with 2 decimal places
percentage = 0.8567
print(f"Percentage formatted: {percentage:.2%}")

#combine multiple formatting options together. For example:
print(f"Combined formatting: {name:<10} | {pi:>10.2f} | {large_number:,.2f}")

