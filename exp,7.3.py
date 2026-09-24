
bases = [10, 20, 30, 40, 50]


result = list(map(lambda pair: pair[1] ** pair[0], enumerate(bases)))


print("Original bases: ", bases)
print("Power of index: ", result)
