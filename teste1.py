"""1) Write a function that takes in a non-empty array (array_value) of distinct integers and an integer
representing a target sum (target_sum). If any two numbers in the input array sum up to the target
sum, the function should return them in an array, in any order. If no two numbers sum up to the
target sum, the function should return an empty array.

Inputs:
array_value = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10
Outputs:
It’s a list of numbers or empty list
"""

array_value = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10


def return_the_two_num_array(array_value, target_sum):
    list = []
    length = len(array_value) - 1
    length_int = len(array_value)    
    for index in range(length):
        for num in range(index + 1, length_int):            
            if array_value[index] + array_value[num] == target_sum:
                list.append(array_value[index],)
                list.append(array_value[num])
                if len(list) == 0:
                    print('OUTPUT: The list is empty')
                else:
                    print("OUTPUT: It's a list of numbers")
    return list

print(return_the_two_num_array(array_value, target_sum))