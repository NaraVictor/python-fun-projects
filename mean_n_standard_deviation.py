# assignment 4: a programe that prompts user for ten numbers then
# displays the mean n standard deviation of those numbers

from math import sqrt

def calculate_mean(list_of_nums):
    sum = 0
    for i in list_of_nums:
        sum += i
    return round(sum/len(list_of_nums),2)


def standard_deviation(numbers):
    mean = calculate_mean(numbers)
    new_list = []
    for i in numbers:
        new_num = (i - mean)
        new_list.append(new_num * new_num)

    new_mean = calculate_mean(new_list)
    return round(sqrt(new_mean), 5)


if __name__ == '__main__':
    print('Enter ten numbers')
    ten_nums = []
    count = 1
    while len(ten_nums) < 10:
        num = int(input(f'{count} - input number: '))
        ten_nums.append(num)
        count += 1

    print(f'\nThe mean is: {calculate_mean(ten_nums)}')
    print(f'The standard deviation is: {standard_deviation(ten_nums)}')
