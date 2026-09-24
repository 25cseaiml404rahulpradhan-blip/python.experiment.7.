
char_list = ['A', 'B', 'C', 'C', 'D', 'E', 'F', 'A']



unique_chars = list(dict.fromkeys(char_list))


lowercase_result = list(map(lambda char: char.lower(), unique_chars))


print("Original List:", char_list)
print("Unique Lowercase:", lowercase_result)
