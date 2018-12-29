'''
    Data Structure
    - List
    - Tuple
    - Dictionary
    - Set
'''
# 1
# List --> []
# List is contain any types
# Create
my_list = [1, 2, 'apple', 3.14, 3-5j]
print(my_list)

# Read = Access
print(my_list[2])

# Update
my_list[2] = 'Apple2'
print(my_list[2])

# Update - Append
my_list.append(2.71)
my_list.append([2.71, 2.77])
print(my_list)

# Update - Extend
my_list.extend(['a', 'b', 'c'])
print(my_list)


# Delete
del my_list[2]
print(my_list)

# 2
# Tuple = List + read-only
# Notaion = ()
my_tuple = (255, 180, 0)
print(my_tuple)


# 3
# Dictionary --> key and value
# Notation --> {key: value}
# JSON --> JavaScriptObJectNotation

# Create
tech_dict = {
    'Microsoft': 990.25,
    'Apple': 125.45,
    'Amazon': 1501.60
}

# Read
print(tech_dict['Microsoft'])

# Update
tech_dict['Microsoft'] = 1200.99
print(tech_dict['Microsoft'])

# Update by add new key
new_key = 'Google'
tech_dict[new_key] = 3476.76
print(tech_dict)

# Delete
del tech_dict['Apple'] 
print(tech_dict)


# Set --> Mathematical Set
# Non-repeat
# Notation --> {}
my_set = {1, 1, 1, 2, 3}
print(my_set)

A = {1, 2, 3, 4 , 5}
B = {1, 2, 3, 'a'}

# Union
C = A.union(B)
print(C)

# Insection
print(A.intersection(B))

# Different
print(A-B)
print(B-A)

# Conversion List <-> Set
I = [1, 2, 2, 2, 3, 3]
set_I = set(I)
I = list(set_I)
print(I)
print(set_I)
print(I)