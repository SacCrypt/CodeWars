def duplicate_count(text):
    counter = 0
    text = text.lower()
    for x in text:
        if text.count(x) > 1:  
            counter += 1
            text = text.replace(x, "")
    return counter
