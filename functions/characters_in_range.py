def characters_range(chr1, chr2):
    result = ''

    for i in range(ord(chr1) + 1, ord(chr2)):
        result += chr(i) + ' '

    return result


char1 = input()
char2 = input()
print(characters_range(char1, char2))