number = int(input(":"))

count = 0

while number >0:
    count +=1
    number //= 10

print("Digits:", count)