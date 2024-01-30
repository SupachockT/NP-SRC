from tkinter import*
from tkinter import ttk

def Configure(obj):
    print(obj.configure());
    
root = Tk(); #Create root window
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid(); #put winget to root window

#print(button['text']);
button['text']="Goodbye";
#print(button['text']);
#print(button.configure('text')); #chane history
Configure(button);

