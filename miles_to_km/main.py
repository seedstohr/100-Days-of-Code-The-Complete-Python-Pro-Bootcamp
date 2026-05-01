#import tkinter

import tkinter

#creat and setup window

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

#create functon to calc miles to km and output the result to the window

def calculate_m_to_km():
    #get input from miles_input
    mile = float(miles_input.get())
    #convert miles to km
    km = mile * 1.60934
    #update km_output with result
    km_output.config(text=f"{km}")

#create input for miles 1,0

miles_input = tkinter.Entry(width=7)
miles_input.grid(row=0, column=1)

#creat miles text 2,0

miles_text = tkinter.Label(text="   Miles")
miles_text.grid(row=0, column=2)

#create equals text 0,2

equals_text = tkinter.Label(text="is equal to")
equals_text.grid(row=1, column=0)

#create output calculation km 1, 1

km_output = tkinter.Label(text="0")
km_output.grid(row=1, column=1)

#create calculate button 1,3

calculate_button = tkinter.Button(text="Calculate", command=calculate_m_to_km)
calculate_button.grid(row=3, column=1)

#create km text 2,3

km_text = tkinter.Label(text="Km")
km_text.grid(row=1, column=2)

window.mainloop()
