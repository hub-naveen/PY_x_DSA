word = input("Enter a word:")
print(word)

enter = input("Enter your Command [1] start [2] stop [3] restart:")

if enter == "1":
    print("Starting...")
elif enter == "2":
    print("Stopping...")
elif enter == "3":
    print("Restarting...")
else:
    print("Invalid command")

