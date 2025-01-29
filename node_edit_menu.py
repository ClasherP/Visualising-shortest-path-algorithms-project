import customtkinter
import tkinter
from tkinter import colorchooser, messagebox
from PIL import ImageTk, Image

def editnodemenu(node_name,ntype,colour,radius): 
    #this holds a dictionry with the different attributes in to return
    node_info = {
        'type': ntype, #type means starting node/ending node
        'name': node_name, #holds the node name
        'color': colour, #holds the colour picked in hexidecimal values
        "radius": radius} #holds the radius of the circle
    def set_destination_node(): #this function sets the type value in the dicionary to "destination"
        error_label3.configure(text="Node Set as destination node") #updates the error message
        node_info['type'] = 'destination' #sets the "type" value 
    def set_start_node(): #this function sets the type value in the dicionary to "destination"s
        error_label3.configure(text="Node Set as starting node") #updates the error message
        node_info['type'] = 'starting' #sets the "type" value
    def reset_node(): #this function sets the type value in the dicionary to None
        error_label3.configure(text="Node type reset") #updates the error message
        node_info['type'] = None #sets the "type" value as None
    
    def print_entry1():
        info = (entry1.get()) #this grabs whtever text is in the text box
        if len(info) >10: #checks if that text is to be accepted or not
            error_label.configure(text="Error: too long") #edits the label text to say not accepted
        else:
            error_label.configure(text="accepted: "+info) #edits the label text to say accepted 
            label2.configure(text="Edit node ("+info+")") #changes the title of the node via the 
            node_info['name'] = info #changes the node name stored in the dictionary 
    def choose_colour():
        color = colorchooser.askcolor(title="choose the nodes colour:")[1] #brings up a colour picking menu
        #the line below edits the second error label to be set to the colour hexidecimal
        error_label2.configure(text="colour has been set to ("+color+")") 
        node_info['color'] = color #this changes the value that is stored in the dictionary 
    def update_slider_value(value): #takes the value of the slider  
        if round(value) == 50: #if the slider is the default value then the text below will be configured
            slider_label.configure(text="Radius: " + str(round(value)) + " (default value)")    
        else: #if the slider is not the default value then the text below will be configured
            slider_label.configure(text="Radius: " + str(round(value)))
        node_info["radius"] = (round(value)) #reasigns the radius to the nofe_info dictionary


    title = "Edit node" # sets the title using the node_name
    customtkinter.set_appearance_mode("light") # sets the appearance of the window to light mode
    customtkinter.set_default_color_theme("blue") # sets the colour scheme to blue 
    
    menu = customtkinter.CTk() # this defines the tkinter window and stores it in the menu variable
    menu.geometry("440x500") # sets the coordinates of the screen
    menu.title(title) # sets the title of the window to the title variable above
    menu.iconbitmap("images\\edit.ico")

    background_image = ImageTk.PhotoImage(Image.open("images\\backgraound.jpeg")) # this grabs an image stored in my files
    label1 = customtkinter.CTkLabel(master=menu, image=background_image, text="") # this fills a label with an image 
    label1.pack() # this draws the image to the screen

    # below creates a frame and assigns it to the frame variable 
    frame = customtkinter.CTkFrame(master=label1, width=320, height=370, corner_radius=15, fg_color="#C0C0C0")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # places that frame on the screen

    # this creates a label (which acts as a title) called edit node with the nodename 
    label2 = customtkinter.CTkLabel(master=frame, text=("Edit node ("+node_name+")"), font=("Century gothic",20))
    label2.place(x=20,y=35)

    #the error label will let the user know a pice of text has been approved or denied
    error_label = customtkinter.CTkLabel(master=frame, text="") #creates an empty error message
    error_label.place(x=20, y=115) #draws the error label at the coordinates 
    #code below is a text box to enter the node name, with the placeholder text "enter node name"
    entry1 = customtkinter.CTkEntry(master=frame, width=160, placeholder_text="enter node name:")
    entry1.place(x=20, y=90) #this places the text box at required coordinates 
    #this is the button that will take whatver has been inputted in the text box
    submit = customtkinter.CTkButton(master=frame, width=100, text="submit", command=print_entry1) #calls the print_entry function 
    submit.place(x=190, y=90) #places the button at desired coordinates 

    #creates the error label
    error_label3 = customtkinter.CTkLabel(master=frame, text="") #creates an empty error message
    error_label3.place(x=20, y=195) #places the error label just below the starting and destination buttons
    #creates the staring button with width=130px and height=40px and calls the starting node function
    starting_button = customtkinter.CTkButton(master=frame, width=130, height=40, text="set starting node", command=set_start_node)
    starting_button.place(x=20, y=150) #places the button at the end of the screen
    #Creates the destination node button with width=130px and height=40px and calls the destination node function
    destination_button = customtkinter.CTkButton(master=frame, width=130, height=40, text="set destination node", command=set_destination_node)
    destination_button.place(x=160, y=150) #places this button on the right side of the frame 
    #creates the reset button with the small dimentions of width=50px and height=10px, and calls the reset node function
    reset_button = customtkinter.CTkButton(master=frame, width=50, height=10, text="reset", command=reset_node)
    reset_button.place(x=240, y=199) #places this button on the left side of the frame 
    
    #creates the colour button with the text "pick a colour" and which calls the "choose colour" function
    colour_button = customtkinter.CTkButton(master=frame, width=270, height=40, text="pick a colour", command=choose_colour)
    colour_button.place(x=20, y=230) #places this near the bottom of the screen
    error_label2 = customtkinter.CTkLabel(master=frame, text="") #creates the error label 
    error_label2.place(x=20, y=270) #places the error message right under the colour button

    #this creates a horizontal slider that goes from 20 to 100 and calls the function (update slider) 
    slider1 = customtkinter.CTkSlider(frame, from_=20, to=100, width=270, orientation="horizontal",command=update_slider_value)
    slider1.set(radius) #sets the slider to start at 50
    slider1.place(x = 20, y =330) #places it right under the colour picker button
    #sets the slider label as 50 to start with
    if radius == 50:
        slider_label = customtkinter.CTkLabel(master=frame, text="Radius: " + str(round(slider1.get())) +" (default value)")
    else:
        slider_label = customtkinter.CTkLabel(master=frame, text="Radius: " + str(round(slider1.get())) +" (previous value)")
    slider_label.place(x=20, y=300) #places it right above the slider

    
    menu.mainloop() # this is the main program loop that keeps the window open
    return node_info

#this code will run if the program isn't being imported
if __name__ == "__main__":
    node_name = "node 1" #sets the node name
    print (editnodemenu(node_name,None,None,50)) #prints the return value
