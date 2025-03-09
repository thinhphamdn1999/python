from tkinter import END, Button, Entry, Label, Text, Tk

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="This is a label", font=("Arial", 24))
my_label.place(x=0, y=0)

my_label["text"] = "New Text"
my_label.config(text="New Text 1")
my_label.grid(column=0, row=0)


# Button

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

new_button = Button(text="New button")
new_button.grid(column=3, row=0)

# Entry
input = Entry(width=5)
input.insert(END, "Example")
input.grid(column=4, row=3)

# Text
text = Text(width=30, height=5)
text.insert(END, chars="Text input")
print(text.get("1.0", END))

# Spin box

# Scale

# Check button

# Radio button

window.mainloop()
