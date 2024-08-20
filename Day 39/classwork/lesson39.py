print("აირჩიეთ ნივთი")

price = int(input("რა ფასის ნივთი გნებავთ?: "))
discount = int(input("რა ფასდაკლებით გნებავთ ნივთი?: "))

num = (price * discount)  / 100 
print(price - num)