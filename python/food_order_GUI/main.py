# food_order use radio button
# radio button = similar to checkbox, but you can only select 1 from a group

from tkinter import *

food = ["pizza", "hamburger", "hot-dog"]

def order():
    if x.get() == 0:
        print("Client order pizza!")
    elif x.get() == 1:
        print("Client order hamburger!")
    elif x.get() == 2:
        print("Client order hot-dog!")
    else:
        print("Undefined!")


window = Tk()
window.title("Food order")

icon = PhotoImage(file="logo.png")
hamburgerImage = PhotoImage(file="hamburger.png")
pizzaImage = PhotoImage(file="pizza.png")
hotdogImage = PhotoImage(file="hot-dog.png")
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

window.iconphoto(True, icon)
window.config(background="white")

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],  # adds text to radio buttons
                               variable=x,  # groups radio button together
                               value=index,  # assign each radio button a different value
                               padx=25,
                               pady=25,
                               font=("Impact", 20, "bold"),
                               image=foodImages[index],  # add image to radio button
                               compound="left",  # icon on the left hand
                               indicatoron=0,  # eliminate circle indicator
                               width=210,  # set width of radio buttons
                               command=order    # set command of radio button to function
                               )
    radio_button.pack(anchor=W)

window.mainloop()
