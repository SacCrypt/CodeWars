def evens_and_odds(n):
    if n%2 == 0:
        n = bin(n)
        n = str(n).lstrip("0b")
    elif n%2 != 0:
        n = hex(n)
        n = str(n).lstrip("0x")
    return n
