import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

def button_clicked():
    input_miles = float(mile_input.get())
    output_km = round(input_miles * 1.609)
    label_ans.config(text=f'{output_km}')

# Entry
mile_input = tkinter.Entry(width=7)
mile_input.grid(column=1, row=0)


# label mile
label_mile = tkinter.Label(text='Miles')
label_mile.grid(column=2, row=0)
label_mile.config(padx=10, pady=10)

# label equal
label_eq = tkinter.Label(text='is equal to')
label_eq.grid(column=0, row=1)
label_eq.config(padx=10, pady=10)

# label answer
label_ans = tkinter.Label(text=0)
label_ans.grid(column=1, row=1)
label_ans.config(padx=10, pady=10)

# label km
label_km = tkinter.Label(text='Km')
label_km.grid(column=2, row=1)
label_km.config(padx=10, pady=10)

# button
button_cal = tkinter.Button(text='Calculate', command=button_clicked)
button_cal.grid(column=1, row=2)
button_cal.config(padx=10, pady=10)

window.mainloop()