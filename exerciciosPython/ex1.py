# Comprime string: exemple: aaabbbbcc -> a3b4c2
# Extra: If result is longer than input, return the input

def compress_string(text):
    if not text:
        return text
    
    result = ""

    current_letter = text[0]
    count = 0

    for c in text:
        if c == current_letter:
            count += 1
        else:
            result += current_letter + str(count)

            count = 1
            current_letter = c

    result += current_letter + str(count)

    return result if len(result) < len(text) else text


text = input("Insert text to comprime: ")
print(compress_string(text))