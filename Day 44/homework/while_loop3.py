correct_number = 7
incorrect_number = 1 ,2, 3, 4, 5, 6, 8, 9, 10 
number = input("guess the number between 1 and 10: ")
 
while number != incorrect_number:
    print("your answer is incorrect")
    number = input("guess the number between 1 and 10: ")

if number == correct_number:
    print("your are right")



