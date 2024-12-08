def search_ind(list_items, item):
    if item not in list_items:  # Предварительно проверям присутсвие искомого элемента в списке
        return None  # В случае отсутсвия выводим None
    for i in range(len(list_items)):  # Проведем поиск элемента через индексы списка
        if list_items[i] == item:  # Проверяем соответствие значения по индексу с искомым элементом
            return i  # Выводим индекс первого вхождения элемента
    # TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_ind(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
