def countLetters(s):
    result = {}
    for c in s:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1

    return result

text = "abracadabra"
count = countLetters(text)

for key in sorted(count):
    print(key + ":", count[key], end="; ")