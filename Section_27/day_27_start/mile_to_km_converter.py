from tkinter import END, Button, Entry, Label, Text, Tk

window = Tk()
window.title("Mile to km convertor")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


text_input = Entry(width=10)
text_input.insert(END, "0")
miles_text = Label(text="Miles")
text_input.grid(column=2, row=1)
miles_text.grid(column=3, row=1)


is_equal_text = Label(text="is equal to")
km_convertor_text = Label(text=0)
km_text = Label(text="Km")
is_equal_text.grid(column=1, row=2)
km_convertor_text.grid(column=2, row=2)
km_text.grid(column=3, row=2)


def click():
    try:
        miles_num = float(text_input.get())
        km_convertor_text.config(text=miles_num * 1.609)
    except:
        error = Label(text="Please enter the valid number")
        error.grid(column=2, row=1)


calculate_btn = Button(text="Calculate", command=click)
calculate_btn.grid(column=2, row=3)


window.mainloop()
