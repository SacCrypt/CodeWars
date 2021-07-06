def to_underscore(string):
    if type(string) == int:
        return str(string)
    return ''.join(['_' + i.lower() if i.isupper() else i for i in string]).lstrip('_')
