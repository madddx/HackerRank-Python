def print_rangoli(size):
    # your code goes here
    # we start from the middle line to the end (== second half)
    lines = list()
    for b in range(size):
        base = chr(ord("a") + b)
        temp = list()
        for i in range(size - b):
            temp.append(chr(ord(base) + i))
        chars_to_build_line = temp[:0:-1]
        chars_to_build_line.extend(temp)
        line = "-".join(chars_to_build_line)
        lines.append(line)
    result = lines[:0:-1]
    result.extend(lines)

    width = max(map(len, result))

    for l in result:
        print("{text:-^{w}}".format(text=l, w=width))
