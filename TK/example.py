import tkinter as tk

root = tk.Tk()
root.title('Tkinter Demo App')
print(root.title())

# width x height ±x(window’s horizontal position) ±y(window’s vertical position)
root.geometry('600x600+100+200')
root.resizable(False, False)
#Transparency
root.attributes('-alpha', 0.9)


#Label widget
message = tk.Label(root, text="Hello World!")
message.pack()


root.mainloop()

