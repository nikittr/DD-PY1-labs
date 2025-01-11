import json
# TODO решите задачу
def task() -> float:  # функция, вычисляющая сумму произведений 2 значений в словаре
    with open('input.json') as in_file:
        json_list = json.load(in_file)
        sum_of_val = sum([j_dict['score'] * j_dict['weight'] for j_dict in json_list])
        return round(sum_of_val, 3)

print(task())
