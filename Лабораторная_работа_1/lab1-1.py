numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count_num = len(numbers)
none_position = int(*[i for i in range(len(numbers)) if numbers[i] is None])
none_from_numbers = numbers.pop(none_position)
numbers = [i for i in numbers if not none_from_numbers]
numbers = numbers[:none_position] + [sum(numbers) / count_num] + numbers[none_position:]
print("Измененный список:", numbers)
