def is_even(num):
    print('Number is ', num)
    return num%2 == 0


def test():
    print('ABC')
    # return None


'''
    Internal function
'''

def calculator(a, b, ops):
    def add(a, b):
        return a+b

    def subtract(a, b):
        return a-b

    if ops == '+':
        print(add(a, b))
    elif ops == '-':
        print(subtract(a,b))

'''
    Functional Programming
    Immutable data
'''
def f(x):
    return lambda a : a**x


def g(x):
    return x+2


if __name__ == '__main__':
    calculator(1, 2, '+')
    calculator(1, 2, '-')

    # fog(x) == f(g(x))
    print(f(g(2)))

    # Anonymous function
    h = lambda x : x + 10
    h2 = lambda x, y : x+y
    print(h(10))
    print(h2(h(10), h(20)))

    power_2 = f(2)
    print(power_2(4))

    power_3 = f(3)
    print(power_3(3))
