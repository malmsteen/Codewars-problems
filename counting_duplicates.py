def duplicate_count(text):
    dct = {}
    text.lower()
    for l in text.lower():
        dct[l] = dct.get(l, 0) + 1

    num = 0
    for d in dct.values():
        if d > 1:
            num += 1

    return num


duplicate_count("abcdeaB")
