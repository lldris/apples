#increases something with 1 
def add_one(something):
    something += 1

#the main code
def main():
    apples = 0
    while True: 
        choice = input("add one? ")
        if choice == "": #just press enter 
            add_one(apples) #calls on the function add_one
            print(f"You have {apples} apples")
        else:
            break

main()
