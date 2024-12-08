def find_common_participants(first_group, second_group, split_sym=','):  # Напишите функцию find_common_participants
    first_set = set(first_group.split(split_sym))  # списки создаем, разделяя по символу строку
    second_set = set(second_group.split(split_sym))  # затем получаем множества из списков для последующего пересечения
    intesec_list = list(first_set.intersection(second_set))  # список пересения двух множеств
    intesec_list.sort()  # сортируем в алфавитном порядке итоговый список
    return intesec_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))  #
