year = int(input("Enter a Year: "))

if year % 400 == 0:
    print(year, "Is a Leap Year")

elif year % 100 == 0:
    print(year, "Is not a Leap Year")

elif year % 4 == 0:
    print(year, "Is a Leap Year")

else:
    print(year, "Is not a Leap Year")
