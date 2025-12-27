
# To make the note and add it to it.

    # Using the print('') to give the one block of space to make look it good; 

def add_note():
    writeFileName = input('enter your file name in .txt form :')
    print("")
    note = input('What you want to write on your ' + writeFileName+ "? ")
    print("")
    with open (writeFileName,"a") as file:
        file.write(note + "\n")
    print("")
    print('Note completed!')
    print('')

# For Read
def read_note():
    try:
        ask_file_name = input('Write your file name To read it: ')
        print('')
        with open(ask_file_name,"r") as file:
            print(file.read())
    except FileNotFoundError:
        print("not found")

# For delete the File 
def delte_note():
    try:
        ask_file_name = input('Write the name of file which you want to be delted : ')
        print('')
        with open(ask_file_name,'d') as file:
            print(ask_file_name.remove())
    except FileNotFoundError:
        print('sorry but file not found')


# Make sure to run it again and ask to user. 
while True:
    print('')
    print('1 to write the note, 2 to read the note , 3 to delete,4 to exit')
    print('')
    choice = input('enter the number: ')
    print('')
    if choice == '1':
        add_note()
    elif choice == '2':
        read_note()
    elif choice == '3':
        delte_note()
    elif choice == '4':
        break