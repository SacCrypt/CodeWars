def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    res = str(max(numbers)) + " " + str(min(numbers))
    return res
