while True:  
    name = input("what is ur name sir ")
    password = input(f"can i get ur password {name}? ")
    if password == "markie":
        break

while True:
    what = input(f"what do u want to do {name}? ")
    if what == "change_name":
        change = input("what name whould u like?")
        name = change
    if what == "quit":
        break
    if what == "buttons":
        file = input(f"which file of buttons do u want to see{name}? ")
        if file == "analzye.html":
            open("buttons/analzye.html")
            print("we did it")
