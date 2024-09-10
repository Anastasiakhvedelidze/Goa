numbers = [4, 67, 7, 34, 8, 23, 5, 98, 1, 92,]
counter = 0

for i in range (len(numbers)):
    if len(str(numbers[i])) == 2:
        counter += 1

print(counter) 