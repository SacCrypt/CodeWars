def sum_dig_pow(a, b): 
    result = []
    _list = [x for x in range(a, b + 1)]
    for i in _list:
        incrementor = 0
        if len(str(i)) >= 2:
            splitter = list(str(i))
            splitter = [int(j) for j in splitter]
            for m in range(len(splitter)):
                incrementor += splitter[m]**(m+1)
            if incrementor == int(''.join(str(x) for x in splitter)):
                result.append(i)
        else:
            result.append(i)
    return result
