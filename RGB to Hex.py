def rgb(r, g, b):
    _list = []
    _list.append(r)
    _list.append(g)
    _list.append(b)
    for x in range(len(_list)):
        if len(str(_list[x])) == 1:
            _list[x] = hex(_list[x]).replace("x", "")
        elif len(str(_list[x])) > 1 and _list[x] >= 0 and _list[x] <= 255:
            _list[x] = hex(_list[x]).replace("x", "").replace("0", "").upper()
        elif _list[x] <= 0 :
            _list[x] = hex(0).replace("x", "")
        elif _list[x] >= 255:
            _list[x] = hex(255).replace("x", "").replace("0", "").upper()
    return ''.join(_list)
