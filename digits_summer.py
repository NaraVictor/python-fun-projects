# program to sum digits of an integer

def sum_digits():
    number = int(input('input a number between 0 & 1000'))

    if number < 1:
        return print('number cannot be less than 1')
    elif number > 999:
        return print('number cannot be more than 999')

    sum = 0
    for i in str(number):
        sum += int(i)

    return print(f'sum of digits is: {sum}')

    
if __name__ == "__main__":
    sum_digits()
