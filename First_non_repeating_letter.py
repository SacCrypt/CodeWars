def first_non_repeating_letter(string):
    _list = list(string)
    _list1 = list(string.lower())
    for x in _list1:
        if _list1.count(x) == 1:
            index = _list1.index(x)
            break
    try:
        return _list[index]
    except:
        return ''
