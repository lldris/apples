
#increases a lists value with 1 
def add_one(u_lista, key):
    u_lista[key] += 1

#the main code
def main():
    apples = {"a":0} 
    key = "a" 
    while True:
        choice = input("add one? ")
        if choice == "": #just press enter 
            add_one(apples, key) #calls on the function add_one
            print(f"You have {apples[key]} apples")
        else:
            break

main()

