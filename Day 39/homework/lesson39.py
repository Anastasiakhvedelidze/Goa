numbers = []
for i in range(10):
    number = int(input("bring number: "))
    numbers.append(number)

more_then_100 = []
less_then_100 = []

for number in numbers:
    if number > 100:
        more_then_100.append(number)
    else:
        less_then_100.append(number)

print("more then 100 numbers: ", more_then_100 )
print("numbers less than 100: ", less_then_100 )