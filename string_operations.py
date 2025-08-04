
# String concatenation
first_name = "Lakshmi"
last_name = "Reddy"
full_name = first_name + " " + last_name
print(full_name)

# String repetition
message = "problem ! " * 3
print(message * 4)

# String methods
print(message.upper())
print(message.lower())
print(message.strip() * 2)  # removes leading/trailing spaces
print(message.replace("problem", "error"))

# Quotes inside strings
name = "Lakshmi said 'hello'"
print(name)

name = 'Lakshmi said "hello"'
print(name)

name = '''Lakshmi said "hello"
Archi said "hii"'''
print(name)

# String length
print(len(message))

# String indexing and slicing
name = "Lakshmi"
print(name[2])       # 'k'
print(name[5])       # 'm'
print(name[2:5])     # 'ksh'
print(name[3:5])     # 'sh'
print(name[1:])      # 'akshmi'
print(name[:6])      # 'Lakshm'
print(name[3:])      # 'shmi'
print(name[-4])      # 'h'
print(name[3])       # 's'
print(name[::2])     # 'Lkhi'
print(name[::3])     # 'Lsi'

# Escape sequences
s = "Archi\nis a good girl"
print(s)

s = "Archi is a\tmy sis"
print(s)