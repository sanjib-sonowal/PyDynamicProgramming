# Initcap
print("***INITCAP***")
str1 = "hello, how are you?"
print(str1.capitalize())

# Count a specific word
print("***COUNT***")
str1 = """Elon Musk is inspiring
Elon created SpaceX and Tesla
Elon is genius"""
print(str1.count('Elon'))

# Ends with a specific string
print("***ENDS WITH***")
str1 = "sonowalzlabs.org"
print(str1.endswith('.com'))
print(str1.endswith('.org'))

# Find a substring
print("***FIND***")
str1 = "SonowalzLabs works on AI and Machine Learning models"
print(str1.find('AI'))
print(str1.find('C#'))

# Check if string is in lower case
print("***IS LOWER***")
str1 = "Hello! User"
print(str1.islower())
str1 = "hello! user"
print(str1.islower())

# Check if string is in upper case
print("***IS UPPER***")
str1 = "Hello User"
print(str1.isupper())
str1 = "HELLO USER"
print(str1.isupper())

# Converts the string to lower case
print("***TO LOWER***")
print(str1.lower())

# Converts the string to upper case
print("***TO UPPER***")
str1 = "Hello User"
print(str1.upper())

# Strip
print("***STRIP***")
str1 = "!!!I am the Joker!@@@"
print(str1.lstrip('!'))
print(str1.rstrip('@'))
str1 = "@@@I am Batman!@@@"
print(str1.strip('@'))

# Replace
print("***REPLACE***")
str1 = "Magic Box"
print(str1)
print(str1.replace('Box', 'Code'))

# Split
print("***SPLIT***")
str1 = "SonowalzLabs Inc."
print(str1.split())

# Swap Case
print("***SWAP CASE***")
str1 = "I LOVE programming"
print(str1.swapcase())

# Title
print("***TITLE***")
str1 = "see you again"
print(str1.title())

# Remove variable str1 from memory
del str1

