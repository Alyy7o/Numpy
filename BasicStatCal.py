import numpy as np


def operations(data, option):
    if option == 1:
        return print(f'Mean of Given Data is: {np.mean(data)}')
    elif option == 2:
        return print(f'Median of Given Data is: {np.median(data)}')
    elif option == 3:
        return print(f'Standard Deviation  of Given Data is: {np.std(data)}')
    else:
        return print('Please Enter Valid Number')


print('''\n   Basic Statistics Calculator \n''')

size_of_arr = int(input('''   Enter Size of Data: \n'''))

data = []

for i in range(size_of_arr):
    value = int(input(f'{i}th Value: '))
    data.append(value)
    
print('''
    Enter 1 for Mean
    Enter 2 for Median
    Enter 3 for Standard Deviation
        ''')

option = int(input())

operations(data, option)
