def find_missing_letter(chars):
    for x in range(len(chars)):
        if ord(chars[x + 1]) != ord(chars[x]) + 1: 
            return chr(ord(chars[x]) + 1)
