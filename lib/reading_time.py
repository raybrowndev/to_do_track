

def read_speed(text, wpm):
    words = len(text.split())
    print(len(text))
    return words / wpm

def grammar(string):
    if string[0].isupper() == True and string[-1] == ".":
        return True
    else:
        raise Exception("sorry WRONG")    




