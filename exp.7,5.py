
num_list = [1, 2, 3, 4, 5, 6]
num_tuple = (1, 2, 3, 4, 5, 6)



to_char = lambda x: chr(96 + x)

string_list1 = list(map(to_char, num_list))
string_list2 = list(map(to_char, num_tuple))


print("Original List:", num_list)
print("Result 1:     ", string_list1)
print("\nOriginal Tuple:", num_tuple)
print("Result 2:      ", string_list2)
