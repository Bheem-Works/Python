import pyttsx3

engine = pyttsx3.init()

try:
    # Open your text file and read all of its content
    with open('/home/vim-magar/Desktop/miso/Python/Projects/Note/vim.txt', 'r') as f:
        text_to_speak = f.read()

    print("I will now read the following text from the file:")
    print(f'"{text_to_speak.strip()}"')

    # Queue the text to be spoken
    engine.say(text_to_speak)

    # Process the speech queue and wait for it to finish
    engine.runAndWait()

except FileNotFoundError:
    print("Error: The file '/home/vim-magar/Desktop/miso/Python/Projects/Note/vim.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")