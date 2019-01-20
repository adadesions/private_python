'''
    Pythonic Class
'''
class Animal:
    def __init__(self, name, color):
        # Instance Variable
        self.name = name
        self.color = color
        self.speicy = ''
    
    # Instance Methods
    def get_name(self):
        return self.name
    

    def set_name(self, name):
        self.name = name


    # Static Method
    def add():
        print('ADD')


if __name__ == '__main__':
    human = Animal('Ada', 'Red')
    print(human.get_name())