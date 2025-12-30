#READ


with open("data.txt", "r") as f:
    print(f.read())


#WRITE
with open("log.txt", "w") as f:
    f.write("Hello")
