import tkinter as tk
from tkinter import ttk
from time import strftime, localtime

# Use aliases for the modules
root = tk.Tk()
Frame = tk.Frame
Label = tk.Label  # Using tk.Label instead of ttk.Label
Entry = ttk.Entry
Button = ttk.Button

#------------------------------------------------------------------------------ 
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
    
center_window(root, 1500, 750)

label = Label(
    root,
    text='ร้านอาหารคณะวิศวกรรมศาสตร์ ศรีราชา',
    font=("roboto", 36))
label.pack(ipadx=10, ipady=10)

#------------------------------------------------------------------------------ Time
def update_time():
    current_time = strftime("%A %B %d %H:%M:%S %Y", localtime())
    label2.config(text=current_time)
    label2.after(1000, update_time)
    
frame = tk.Frame(root)
frame.pack(side=tk.TOP, pady=10)

# Add widgets to the frame (you can customize this part)
label1 = tk.Label(frame, text="", padx=150, pady=20,  relief="groove", bg="powder blue")
label1.grid(row=0, column=0)

label2 = tk.Label(frame, text="", padx=20, pady=20, relief="groove", border='0')
label2.grid(row=0, column=1)

label3 = tk.Label(frame, text="", padx=150, pady=20, relief="groove", bg="powder blue")
label3.grid(row=0, column=2)

update_time()

#------------------------------------------------------------------------------ Calculator UI
def button_click(number):
    if number == 'C':
        clear_entry()
    elif number == '=':
        compute_result()
    else:
        current = entry_var.get()
        entry_var.set(current + str(number))

def clear_entry():
    entry_var.set("")

def compute_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")
        
calculator_frame = tk.Frame(root)
calculator_frame.pack(side=tk.RIGHT, ipadx=8)

entry_var = tk.StringVar()

entry = Entry(calculator_frame, textvariable=entry_var, font=("roboto", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    btn = Button(calculator_frame, text=button_text, command=lambda btn_text=button_text: button_click(btn_text))
    btn.grid(row=row_val, column=col_val, ipadx=4, ipady=16)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

#------------------------------------------------------------------------------ Center UI
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.6, anchor="center")

labels = {}
menuName = ["Pizza", "Burger", "Sushi", "Pasta", "Salad", "Sandwich"]
food_indices = [5, 9, 13, 17, 21, 3]
prices = [100, 120, 50, 80, 75, 45]

# Create a dictionary to associate each food with its price
food_prices = dict(zip(menuName, prices))

# Create a dictionary to store quantity entry fields for each food
quantity_entries = {}

# Create a 4x6 grid of labels within the frame
for i in range(6):
    for j in range(4):
        label_number = i * 4 + j + 1
        label_text = f"Label {label_number}"
        bg_color = "powder blue" if label_number % 2 == 0 else "white"  # Set background color based on label number
        label = tk.Label(frame, text=label_text, relief="sunken", bg=bg_color, padx=50, pady=10)
        label.grid(row=i, column=j, padx=20, pady=10)
        labels[(i, j)] = label

# Indices of labels to be changed to Entry widgets
indices_to_change = [6, 10, 14, 18, 22, 4]

# Replace specific labels with Entry widgets
for index in indices_to_change:
    row = (index - 1) // 4
    col = (index - 1) % 4
    food = menuName[indices_to_change.index(index)]
    quantity_var = tk.StringVar(value="0")  # Set default value to "0"

    # Validation function to allow only integers
    def validate_input(new_value):
        return new_value.isdigit() or new_value == ""

    validate_cmd = (frame.register(validate_input), '%P')

    entry = tk.Entry(frame, textvariable=quantity_var, relief="sunken", bg="powder blue", justify="center", font=("Arial", 12), width=15,
                     validate="key", validatecommand=validate_cmd)
    entry.grid(row=row, column=col, padx=20, pady=10, ipady=10)  # Use ipady to adjust the height
    labels[(row, col)].destroy()  # Destroy the label
    labels[(row, col)] = entry
    quantity_entries[food] = entry

# Change text label
specific_label = labels[(0, 0)]
specific_label.config(text='reference')

# Replace specific labels with food items
for index, food in zip(food_indices, menuName):
    row = (index - 1) // 4
    col = (index - 1) % 4
    specific_label = labels[(row, col)]
    specific_label.config(text=food)

# Function to calculate the total and display on label 8
def calculate_total():
    total_cost = sum(int(quantity_entries[food].get()) * food_prices[food] for food in menuName)
    specific_label = labels[(1, 3)]
    specific_label.config(text=f"B {total_cost}")

# Create "Calculate Total" button
calculate_button = ttk.Button(frame, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=7, column=0, columnspan=4, pady=10)

root.mainloop()




