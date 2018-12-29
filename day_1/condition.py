'''
Docs string
syntax if-else-elseif

if condition:
    [code]
elif condition2:
    [code]
else:
    [code]
'''

# input --> str
# x = input('Enter a number: ')
# x = int(x)
x = int(input('Enter a number: '))

if x%2 == 0:
    print(x, 'is an even.')
elif x%2 == 1:
    print('Reminder is 1')
else:
    print(x, 'is an odd.')
