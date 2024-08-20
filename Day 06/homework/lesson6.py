user_name = input("what is your name?: ")
user_surname = input("what is your surname?: ")
user_age = input("how old are you?: ")
user_liveplace = input("where do you live?: ")

new_user_age = int(user_age) + 20
print(new_user_age)
print("HELLO" + user_name + user_surname + ",i like your surname, you live in" + user_liveplace + ",and you are" + new_user_age + "years old")
