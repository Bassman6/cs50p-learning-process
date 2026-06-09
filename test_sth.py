name = input("your name")

file = open("name.text","a")
file.write(f"{name}\n")
file.close()


