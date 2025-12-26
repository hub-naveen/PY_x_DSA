

# Print all Even numbers from 1 to N
num = int(input("Enter a number:"))

for i in range(1, num+1):
    if i % 2 == 0:
        print(i)


# Print table of a number (5 → 5 10 15 …)
num = int(input("Enter a number: "))

for i in range(1, 15+2 ):  #Satrt from 1 End at 16 times
    print(num * i)


#Sum of digits of a number
num = int(input("Enter a number: "))
total = 0


while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of All digit", total)



#Reverse a number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev= rev * 10  + digit
    num //= 10

print("Reversed Number is :", rev)
