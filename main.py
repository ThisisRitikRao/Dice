import random
def get_no():
    x = random.randint(1,6)
    return x
z = "y"
while z == "y" :
    x = get_no()
    if x == 1:
        print('''
        -----------
        |         |
        |    0    |
        |         |
        -----------
        ''')
    if x == 2:
        print('''
        -----------
        |         |
        |  0   0  |
        |         |
        -----------
        ''')
    if x == 3:
        print('''
        -----------
        |    0    |
        |    0    |
        |    0    |
        -----------
        ''')
    if x == 4:
        print('''
        -----------
        |  0   0  |
        |         |
        |  0   0  |
        -----------
        ''')
    if x == 5:
        print('''
        -----------
        |  0   0  |
        |    0    |
        |  0   0  |
        -----------
        ''')
    if x == 1:
        print('''
        -----------
        |  0   0  |
        |  0   0  |
        |  0   0  |
        -----------
        ''')
    z = input("Press y to continue...")

