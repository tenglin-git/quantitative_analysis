import math


def sum_average(str):
    string_array = str.split()
    numeric_list = [float(x) for x in string_array]
    length = len(numeric_list)
    sum=0
    for item in numeric_list:
        sum+=item
    average = sum/length
    print(f'sum is {sum}, average = {average}',)
    return average

def sample_standard_deviation(str):
    average = sum_average(str)
    string_array = str.split()
    float_list = [float(x) for x in string_array]
    n = len(float_list) - 1
    sum_square=0
    for item in float_list:
        sum_square += (item - average)**2
    print(f'sum_square = {sum_square}')
    variance = sum_square/n
    print(f'variance = {variance}')
    standard_deviation = math.sqrt(variance)
    print(f'standard_deviation = {standard_deviation}')
    return standard_deviation

def confidence_interval(str):
    average = sum_average(str)
    standard_deviation = sample_standard_deviation(str)
    string_array = str.split()
    float_list = [float(x) for x in string_array]
    length = len(float_list)
    t = 2.2622
    err = t*standard_deviation/math.sqrt(length)
    print(f'err = {err}')

s = '6.5 6.6 6.7 6.8 7.1 7.3 7.4 7.7 7.7 7.7'

confidence_interval(s)
