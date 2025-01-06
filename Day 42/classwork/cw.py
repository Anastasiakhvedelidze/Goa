numbers = [-1, 5, -6, 7, -55, 2, -67, 9]
positive_numbers = []
negative_numbers = []
for i in range(len(numbers)):
    if numbers[i] == 0:
        continue
    elif numbers[i] < 0:
        negative_numbers.append(numbers[i])
    else:
        positive_numbers.append(numbers[i])
print("this is positive numbers: ", positive_numbers)
print("this in negative numbers: ", negative_numbers)