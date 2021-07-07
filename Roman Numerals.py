class RomanNumerals():
    def to_roman(no):
        _list = [1, 4, 5, 9, 10, 49, 50, 90, 100, 400, 500, 900, 1000]
        _list.reverse()
        Numeric = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman = ''
        for index, x in enumerate(_list):
            while no >= x:
                no -= x
                roman += Numeric[index]           
        return roman
    
    def from_roman(roman):
        _list = [1, 4, 5, 9, 10, 49, 50, 90, 100, 400, 500, 900, 1000]
        Numeric = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        no = []
        for i in range(len(roman)):
            if roman[i] == 'I':
                try:
                    if roman[i+1] == 'I':
                        continue
                    else:
                        pos = _list[i+1] - _list[i] 
                except:
                    pass
            pos = Numeric.index(i)
            no.append(_list[pos])
        return sum(no)


print(RomanNumerals.from_roman('MMIX'))
print(RomanNumerals.to_roman(2009))


'''

class RomanNumerals():
    def to_roman(no):
        _list = [1, 4, 5, 9, 10, 49, 50, 90, 100, 400, 500, 900, 1000]
        _list.reverse()
        Numeric = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman = ''
        for index, x in enumerate(_list):
            while no >= x:
                no -= x
                roman += Numeric[index]           
        return roman
    
    def from_roman(roman):
        _list = [1, 4, 5, 9, 10, 49, 50, 90, 100, 400, 500, 900, 1000]
        Numeric = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        no = []
        for i in range(len(roman)):
            if roman[i] == "I":
                try:
                    if roman[i+1] != 'I':
                        pos = [Numeric.index(i) - Numeric.index(i-1)]
                except:
                    pass
            pos = Numeric.index(i)
            no.append(_list[pos])
        return sum(no)


'''
