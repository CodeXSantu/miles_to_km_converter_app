from tkinter import*


window = Tk()
window.title("Miles to km converter")
window.minsize(width=300,height=150)
window.config(padx=30,pady=30)



miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)


is_equal_to_label = Label(text="is equal to ")
is_equal_to_label.grid(column=0,row=1)


converted_km_label = Label(text="0")
converted_km_label.grid(column=1,row=1)


km_label = Label(text="Km")
km_label.grid(column=2,row=1)

def calculate_km():
    miles = float(miles_input.get())
    converted_value = miles *1.609
    converted_km_label.config(text=f"{converted_value}")

calculate_button = Button(text="calculate",command=calculate_km)
calculate_button.grid(column=1,row=2)











window.mainloop()
