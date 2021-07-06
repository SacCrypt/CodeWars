def wave(people):
    _list = list(people)
    result = []
    for x in range(len(_list)):
        _list = [y.lower() for y in _list]
        _list[x] = _list[x].capitalize()
        result.append(''.join(_list))
    result = [x for x in result if not x.islower() ]
    return result
