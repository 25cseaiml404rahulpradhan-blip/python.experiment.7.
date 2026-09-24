numbers = [1, -2, 0, 4, -5, 0, 3]
total_count = len(numbers)

classified = list(map(lambda x: 'pos' if x > 0 else ('neg' if x < 0 else 'zero'), numbers))


pos_count = classified.count('pos')
neg_count = classified.count('neg')
zero_count = classified.count('zero')


pos_ratio = pos_count / total_count
neg_ratio = neg_count / total_count
zero_ratio = zero_count / total_count


print(f"Original Array: {numbers}")
print(f"Positive Ratio: {pos_ratio:.4f}")
print(f"Negative Ratio: {neg_ratio:.4f}")
print(f"Zeros Ratio:    {zero_ratio:.4f}")
