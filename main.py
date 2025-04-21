import sys

list_ints = []
list_neg_ints = []

# Read all 6 integers from stdin at once
list_ints = list(map(int, sys.stdin.read().split()))

# Copy only the negative integers
for num in list_ints:
    if num < 0:
        list_neg_ints.append(num)

# Output number of negatives
print(len(list_neg_ints))

# Output negative integers
for neg in list_neg_ints:
    print(neg)
