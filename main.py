def count_common_elements(*lists):
    result = dict()
    for lst in lists:
        for element in lst:
            if element in result:
                result[element] += 1
            else:
                result[element] = 1
    return {k: v for k, v in result.items() if v > 1}

# Пример использования
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
common_elements = count_common_elements(list1, list2, list3)
print("Количество одинаковых элементов в списках:", common_elements)
