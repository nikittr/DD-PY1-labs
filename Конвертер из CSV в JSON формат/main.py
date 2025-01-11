import csv, json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:  # функция, сериализующая данные из csv файла в json файл
    with open(INPUT_FILENAME) as in_file:
        reader = csv.DictReader(in_file, delimiter=',', quotechar='"')  # TODO считать содержимое csv файла
        json_list = [row for row in reader]
    with open(OUTPUT_FILENAME, 'w') as out_file:
        json.dump(json_list, out_file, indent=4)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
