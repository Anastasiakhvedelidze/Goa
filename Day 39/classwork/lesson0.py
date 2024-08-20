"""
მომხმარებელი შემოიტანს რიცხვს, შემდეგ კი თუ რიცხვი კენტია დაამატებთ კენტებისთვის განკუთნილ სიაში "მომხმარებელი"
თუ არადა ლუწებისთვის განკუთვნილ სიაში   "არადა": Unknow word.
"""
odd = []
even = []
input_number = int(input("wish number for 0 to 100: "))
if input_number % 2 == 0:
    odd.append(input_number)
else:
    even.append(input_number)
print(odd)
print(even)

