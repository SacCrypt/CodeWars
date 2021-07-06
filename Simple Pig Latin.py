def pig_it(text):
    _list = text.split()
    _list = [x[1:] + x[0] + "ay" if x[0].isalpha() or x[0].isdigit() else x for x in _list ]
    return ' '.join(_list)
