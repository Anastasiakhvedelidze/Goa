password = "password123"
password1 = []
question = input("enter password: ")

while question != password1:
    print("its incorrect")
    question = input("enter password: ")

if question == password:
    print("your correct")