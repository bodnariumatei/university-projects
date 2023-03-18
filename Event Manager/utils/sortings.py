def default_cmp(param1, param2):
    return param1 > param2


def selection_sort(lista, key=lambda lista: lista, reversed=False, cmp=default_cmp):
    """
    Sortează o listă prin metoda selecției.
    :param lista: o listă nesortată
    :type lista: list
    :param key:
    :type key:
    :param reversed: flag care determină dacă lista e sortată crescător/descrescător
    :type reversed: bool
    :return: ordered_list - lista ordonată
    :rtype: list
    """
    ordered_list = lista
    for i in range(0, len(ordered_list) - 1):
        index = i
        for j in range(i + 1, len(ordered_list)):
            if cmp(key(ordered_list[index]), key(ordered_list[j])):
                index = j
        if i < index:
            aux = ordered_list[i]
            ordered_list[i] = ordered_list[index]
            ordered_list[index] = aux
    if reversed:
        ordered_list.reverse()
    return ordered_list


def selection_sort_recursive(lista, i, key=lambda lista: lista, reversed=False, cmp=default_cmp):
    """
    Sortează o listă prin metoda selecției.
    :param lista: o listă nesortată
    :type lista: list
    :param key:
    :type key:
    :param reversed: flag care determină dacă lista e sortată crescător/descrescător
    :type reversed: bool
    :return: ordered_list - lista ordonată
    :rtype: list
    """
    if i < 0:
        if reversed:
            lista.reverse()
        return lista
    index = i
    for j in range(i):
        if cmp(key(lista[j]), key(lista[index])):
            index = j
    if i > index:
        aux = lista[i]
        lista[i] = lista[index]
        lista[index] = aux
    return selection_sort_recursive(lista, i - 1, key=key, reversed=reversed, cmp=cmp)


def shake_sort(lista, key=lambda lista: lista, reversed=False, cmp=default_cmp):
    """
    Sortează o listă prin metoda shake-ului/cockteil-ului.
    :param lista: o listă nesortată
    :type lista: list
    :param key:
    :type key:
    :param reversed: flag care determină dacă lista e sortată crescător/descrescător
    :type reversed: bool
    :return: ordered_list - lista ordonată
    :rtype: list
    """
    swapped = True
    start = 0
    end = len(lista) - 1
    ordered_list = lista
    while swapped:
        swapped = False
        for i in range(start, end):
            if cmp(key(ordered_list[i]), key(ordered_list[i + 1])):
                ordered_list[i], ordered_list[i + 1] = ordered_list[i + 1], ordered_list[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if key(ordered_list[i]) > key(ordered_list[i + 1]):
                ordered_list[i], ordered_list[i + 1] = ordered_list[i + 1], ordered_list[i]
                swapped = True
        start = start + 1
    if reversed:
        ordered_list.reverse()
    return ordered_list
