print('Type a string:')
name = input() # brackets necessary
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