'''
1. For-in loop
2. While loop
'''

# For-In loop
name_list = ['Mr.A', 'Ms.B']
for name in name_list:
    print(name)

# range(start=0, end, step=1)
for x in range(5):
    print(x)

for x in range(1, 6, 2):
    print(x)


# While
x = 0
while x < 2:
    print('while', x)
    x += 1

# while True:
#     print('a')


# ==============================================
# Using index
a_list = ['a', 'b', 'c']
for index, val in enumerate(a_list):
    print('index=', index, 'val=', val)

# Loop for Dictionary
stock = {
    'Apple': 32.45,
    'Google': 78.09
}
for key, val in stock.items():
    print(key,'-', val)
