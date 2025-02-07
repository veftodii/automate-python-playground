print('Type a string:')
name = input() # brackets necessary
print('String:', name)
print('Value separator:', name, 'hgjh') # default value separator is space
print('Concatenate string: ' + name + 'kldf') # concatenates the strings
print('Repeat string:', name * 3) # repeats the string N times
print('String length:', len(name)) # string length

print('\nType a number:')
age = input() # returns a string
print('Number:', age)
print('Number to string:', str(age))
print('Number add string, to string:', str(age + '1'))
print('Number add integer, to string:', str(int(age) + 1)) # variable is a string
print('Number to float:', float(age))

print('\nBool expressions:')
b = True # Python is case-sensitive
print('1 = 2:', 1 == 2)
print('1 = 1:', 1 == 1)
print('1 != 2:', 1 != 2)
print('1 != 1:', 1 != 1)
print('Int and float 1 = 1.0:', 1 == 1.0)
print('Int and string 1 = \'1\':', 1 == '1') # no implicit cast observed