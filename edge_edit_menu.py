import customtkinter
import tkinter
from tkinter import colorchooser, messagebox
from PIL import ImageTk, Image

def editedgemenu(weight): 
    #this holds a dictionry with the different attributes in to return
    edge_info = {
        'weight': weight, #holds the edge weight
        } #holds the radius of the circle
    
    def print_entry1():
        dont_accept = False #sets a boolean variable to False
        info = (entry1.get()) #this grabs whtever text is in the text box
        
        try: #attempts to run this code
            int(info) #this turns "info" into an integer 
        #this code will run if an error occurs from the line above, meaning "info" is a string not a number
        except ValueError: 
            error_label.configure(text="Error: enter a number") #configures the error message
            dont_accept = True #sets a boolean variable to True
            
        #checks if that text is short enough and if the value is still accepted 
        if len(str(info)) > 4 and dont_accept == False: 
            error_label.configure(text="Error: number too long") #configures the error message
        elif str(info)[0] == "-":
            error_label.configure(text="Error: No negative numbers") #configures the error message
        else:
            if dont_accept == False: #checks if the value is still accepted
                error_label.configure(text="accepted: "+info) #edits the label text to say accepted 
                label2.configure(text="Edit edge (weight: "+info+")") #changes the title of the edge 
                edge_info['weight'] = int(info) #changes the edge weight stored in the dictionary    
                 
    def reset_weight():
        label2.configure(text="Edit edge")
        error_label.configure(text="Weight reset to 0")
        edge_info['weight'] = 0
        entry1.delete(0, len(str(entry1.get())))
        
    title = "Edit edge" # sets the title using the node_name
    customtkinter.set_appearance_mode("light") # sets the appearance of the window to light mode
    customtkinter.set_default_color_theme("blue") # sets the colour scheme to blue 

    menu = customtkinter.CTk() # this defines the tkinter window and stores it in the menu variable
    menu.geometry("400x200") # sets the coordinates of the screen
    menu.title(title) # sets the title of the window to the title variable above
    menu.iconbitmap("images\\edit.ico")

    background_image = ImageTk.PhotoImage(Image.open("images\\backgraound.jpeg")) # this grabs an image stored in my files
    label1 = customtkinter.CTkLabel(master=menu, image=background_image, text="") # this fills a label with an image 
    label1.pack() # this draws the image to the screen

    # below creates a frame and assigns it to the frame variable 
    frame = customtkinter.CTkFrame(master=label1, width=320, height=170, corner_radius=15, fg_color="#C0C0C0")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # places that frame on the screen

    # this creates a label (which acts as a title) called edit edge
    label2 = customtkinter.CTkLabel(master=frame, text=("Edit edge"), font=("Century gothic",20))
    label2.place(x=20,y=35)

    #the error label will let the user know a pice of text has been approved or denied
    error_label = customtkinter.CTkLabel(master=frame, text="") #creates an empty error message
    error_label.place(x=20, y=115) #draws the error label at the coordinates 
    #code below is a text box to enter the edge weight, with the placeholder text "enter edge weight"
    entry1 = customtkinter.CTkEntry(master=frame, width=160, placeholder_text="enter edge weight:")
    entry1.place(x=20, y=90) #this places the text box at required coordinates 
    #this is the button that will take whatver has been inputted in the text box
    submit = customtkinter.CTkButton(master=frame, width=100, text="submit", command=print_entry1) #calls the print_entry function 
    submit.place(x=190, y=90) #places the button at desired coordinates 
    reset_button = customtkinter.CTkButton(master=frame, width=100, text="reset", command=reset_weight)
    reset_button.place(x=190, y=125) #places this button on the left side of the frame 
    
    menu.mainloop() # this is the main program loop that keeps the window open
    return edge_info

#this code will run if the program isn't being imported
if __name__ == "__main__":
    print (editedgemenu(34)) #prints the return value
