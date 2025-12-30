import os 

path = os.path.expanduser('~/.config/google-chrome/Default/History')

if os.path.exists(path):
    print('chrome history is cleaned')
else:
    print('chrome history is not cleaned')