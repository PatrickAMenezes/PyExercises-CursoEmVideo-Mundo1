from random import choices
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
choose = tuple(choices(nums, k=5))
print(choose[0], choose[1], choose[2], choose[3], choose[4])
print(f'The smaller number is {min(choose)}')
print(f'The greater number is {max(choose)}')
