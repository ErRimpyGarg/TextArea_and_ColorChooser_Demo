#STEP:1 Import required modules

from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser

#STEP:2 Set Screen Window
window=Tk()
window.geometry("600x600")

#STEP:3 Adding text area to add get text from the user.
text = Text(window)
text.pack()

#STEP 5: Defining get_value function that is called in Add_text button.
def get_value():
    text_content = text.get(1.0, END)
    messagebox.showinfo("Msg",message=text_content)

#STEP:4 Creating Add_text button and msg_box pop_up to show entered text by user in the msg box.
add_text_button = Button(window, text="Get Value", command=get_value)
add_text_button.pack(pady="10")

#STEP:7 defining Change_bg function that is called in second button(Change_bg_button) to get required
# color by the user.
def change_bg():
    user_color=colorchooser.askcolor()
    text.config(bg=user_color[1])
#NOTE: In line 27(bg=user_color[1]), [1] is given for the second attribute of the returned value of the
# askcolor() function in line 26 which is the hexvalue of the chosen color and will chnge the bg color to
# that value and the first attribute of that will be R,G,B (user_color[0]) pattern of the color.

#STEP:6 Creating second button for changing background of the text area as per user choice.
change_bg_button=Button(window,text="Change background",command=change_bg)
change_bg_button.pack(pady="10")

window.mainloop()