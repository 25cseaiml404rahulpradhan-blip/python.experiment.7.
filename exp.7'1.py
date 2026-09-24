
def triple(x):
    return x * 3

numbers = [10, 20, 30, 40]


tripled_numbers = list(map(triple, numbers))


print("Original list:", numbers)
print("Tripled list: ", tripled_numbers)
