# note making process by using the file handling; 

def add_note():
    note = input("Enter your note : ")
    writeNoteName = input("What would you like to give a name of your file ? (in the .txt form): ")
    with open(writeNoteName,"a") as file:
        file.write(note + "\n\n")
    print("Note completed")

def view_note():
    try:
        askFileName = input('what is your file name ? : ')
        with open(askFileName,"r") as file:
            print(file.read())
    except FileNotFoundError:
        print("not found")

while True:
    print("n1. To write the note, n2. to read the note, n3 to exit") 
    choice = input('choose:')
    if choice == '1':
        add_note()
    elif choice == '2':
        view_note()
    elif choice == '3':
        break
