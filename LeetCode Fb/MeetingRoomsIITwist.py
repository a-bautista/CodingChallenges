from collections import defaultdict


def find_common_number(nums):
    for i in range(len(nums)):
        start = nums[i][0]
        end = nums[i][1]
        new_list = set(list(range(start, end + 1)))
        nums[i] = new_list
    common_frequency = defaultdict(int)
    for value_set in nums:
        for value in value_set:
            common_frequency[value] += 1
    most_common_value = None
    highest_frequency = float('-inf')
    for value, frequency in common_frequency.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            most_common_value = value
    return most_common_value


print(find_common_number([[1, 4], [3, 5], [4, 6]]))
print(find_common_number([[0, 2], [3, 5]]))
print(find_common_number([[1, 5], [3, 5]]))