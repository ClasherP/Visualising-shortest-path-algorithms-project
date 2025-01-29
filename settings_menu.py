import customtkinter
import tkinter
from tkinter import colorchooser, filedialog
from PIL import ImageTk, Image
from error_msg import confirmation,show_error_message
import ast



def settingsmenu(algorithm, graph, canvas_background, title,image,stats): 
    #this holds a dictionry with the different attributes in to return
    settings_info = {
        "title" : title, #sets the title of the main window
        "algorithm" : algorithm, #the type of algorithm being used to find the shortest path
        'graph': graph, #holds the graph
        "background": canvas_background, #holds the background image 
        "randomiser": 0,
        "image": image,
        "stats": stats} #number of nodes to put on screen
    
    def read_and_construct(filename): #takes the file address as a perameter 
        graph = [] #declares an empty graph array 
        with open(filename, 'r') as file: #opens the file 
            for node in file: #itterates through each node in the file
                #converts the node from a string into an array
                node_line = ast.literal_eval(node.strip())
                graph.append(node_line) #appends the array to the graph array
        return graph #returns the completed graph
    
    def clear_canvas():
        if confirmation("Are you sure you want to delete the canvas?") == True:
            settings_info["graph"] = []
            menu.destroy()
    
    def set_dijkstra(): 
        error_label3.configure(text="Algorithm set: A*") 
        settings_info['algorithm'] = "a"
    def set_A_star(): 
        error_label3.configure(text="Algorithm set: Dijkstra") 
        settings_info['algorithm'] = "d" 
    
    def title_change():
        info = (entry1.get()) #this grabs whtever text is in the text box
        if len(info) >30: #checks if that text is to be accepted or not
            error_label.configure(text="Error: too long") #edits the label text to say not accepted
        elif len(info) < 3:
            error_label.configure(text="Error: too short")
        else:
            error_label.configure(text="accepted: "+info) #edits the label text to say accepted 
            settings_info['title'] = info #changes the node name stored in the dictionary 
    
    def save_g():
        #the filedialog class and asksaveasfilename allows the user to create a txt file 
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if filename != "": #this statment will only run there is data in the variable 
            graph_data = settings_info["graph"] #takes the current graph from the settings_info dictionary 
            with open(filename, "w") as file: #this with statment opens the file and closes it once the for loop is done running
                #the for loop itterates through each node in the graph and writes it to a seperate line in the .txt file
                for node in graph_data: 
                    file.write(str(node) + "\n") #the \n string creates a new line   
            error_label5.configure(text="Saved") #the error label shows that the file has been saved
        else: #this will run if there was no data in the filename variable 
            error_label5.configure(text="Error: No file selected") #updates the error message with an error
            
    def load_g():
        # Opens a file and lets the user pick a txt file
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt"),))
        if filename != "":  # This will be True if a file was selected
            try: #the code below will try to run if it can and if a value error is caught then the "except" statment runs
                settings_info["graph"] = read_and_construct(filename)  # Sets the contents of the file to the graph
                error_label5.configure(text="Loaded")  # Edits the label to say that the file has been accepted
            except: #if there was an error loading the graph, the code will run below
                show_error_message("Graph is unable to open\nPlease select a different file to open") #shows an error message
                error_label5.configure(text="Error") #configures the text under the button to say "error"
            menu.destroy() #closes the menu
        else:  # This will run if no file was selected
            error_label5.configure(text="Error: No file selected")  # Edits the label to say that no file was selected
            
    def choose_colour():
        color = colorchooser.askcolor(title="choose the nodes colour:")[1] #brings up a colour picking menu
        #the line below edits the second error label to be set to the colour hexidecimal
        error_label2.configure(text="Canvas colour has been set to ("+color+")") 
        settings_info["background"] = color #this changes the value that is stored in the dictionary 
        settings_info["image"] = ""
    
    
    def update_slider_value(value): #takes the value of the slider  
        slider_label.configure(text="Nodes: " + str(round(slider1.get())))    

    def switcher():
        if switch.get():
            settings_info["stats"] = True
        else:
            settings_info["stats"] = False

    def submit_randomiser():
        if confirmation("Are you sure you want to randomise?\n\nThis deletes the current canvas!") == True:
            if round(slider1.get()) != 0:
                settings_info["randomiser"] = round(slider1.get()) #rounds the value and replaces the randomiser
                menu.destroy()
            else:
                show_error_message("Error: select more nodes")
    
    def browse_pic():
        #opens a file and lets the user pick a png/jpeg image                                                  
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("png","*.png*"), #allows a .png file to be selected
                                                                                                    ("jpeg","*.jpg*"), #allows a .jpeg file to be selected
                                                                                                    ("gif","*.gif*"), #allows a .gif file to be selected
                                                                                                    ("img","*.img*"))) #allows a .img file to be selected
        if filename: #this will be True if a file was selected
            error_label2.configure(text="File selected: "+filename) #edits the label to say that the file has been accepted
            settings_info["image"] = filename #sets the background to the file type
        else: #this will run if no file was selected
            error_label2.configure(text="Error: no file selected") #edits the label to sat that no file was selected
            
        
    title = "Settings menu" # sets the title using the node_name
    customtkinter.set_appearance_mode("light") # sets the appearance of the window to light mode
    customtkinter.set_default_color_theme("blue") # sets the colour scheme to blue 

    menu = customtkinter.CTk() # this defines the tkinter window and stores it in the menu variable
    menu.geometry("440x600") # sets the coordinates of the screen
    menu.title(title) # sets the title of the window to the title variable above
    menu.iconbitmap("images\\gear.ico")
    

    background_image = ImageTk.PhotoImage(Image.open("images\\backgraound.jpeg")) # this grabs an image stored in my files
    label1 = customtkinter.CTkLabel(master=menu, image=background_image, text="") # this fills a label with an image 
    label1.pack() # this draws the image to the screen

    # below creates a frame and assigns it to the frame variable 
    frame = customtkinter.CTkFrame(master=label1, width=320, height=480, corner_radius=15, fg_color="#C0C0C0")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # places that frame on the screen

    # this creates a label (which acts as a title) called edit node with the nodename 
    label2 = customtkinter.CTkLabel(master=frame, text=("Settings menu"), font=("Century gothic",20))
    label2.place(x=20,y=35)

    #creates the error label
    error_label3 = customtkinter.CTkLabel(master=frame, text="") #creates an empty error message
    error_label3.place(x=20, y=135) #places the error label just below the starting and destination buttons
    #creates the staring button with width=130px and height=40px and calls the starting node function
    star_button = customtkinter.CTkButton(master=frame, width=130, height=40, text="Set Dijkstra algorithm", command=set_A_star)
    star_button.place(x=20, y=90) #places the button at the end of the screen
    #Creates the destination node button with width=130px and height=40px and calls the destination node function
    dijkstra_button = customtkinter.CTkButton(master=frame, width=130, height=40, text="Set A* algorithm", command=set_dijkstra)
    dijkstra_button.place(x=160, y=90) #places this button on the right side of the frame 

    #creates the staring button with width=130px and height=40px and calls the starting node function
    save_button = customtkinter.CTkButton(master=frame, width=137, height=40, text="Save graph", command=save_g)
    save_button.place(x=20, y=240) #places the button at the end of the screen
    #Creates the destination node button with width=130px and height=40px and calls the destination node function
    load_button = customtkinter.CTkButton(master=frame, width=130, height=40, text="Load graph", command=load_g)
    load_button.place(x=160, y=240) #places this button on the right side of the frame 
    error_label5 = customtkinter.CTkLabel(master=frame, text="") #creates an empty error message
    error_label5.place(x=160, y=285) #places the error label just below the starting and destination buttons
    
    #creates the colour button with the text "pick a colour" and which calls the "choose colour" function
    colour_button = customtkinter.CTkButton(master=frame, width=137, height=40, text="Canvas colour", command=choose_colour)
    colour_button.place(x=20, y=165) #places this near the bottom of the screen
    browse_button = customtkinter.CTkButton(master=frame, width=130, height=40, text="Browse images", command=browse_pic)
    browse_button.place(x=160, y=165) #places this near the bottom of the screen
    error_label2 = customtkinter.CTkLabel(master=frame, text="") #creates the error label 
    error_label2.place(x=20, y=205) #places the error message right under the colour button

    error_label = customtkinter.CTkLabel(master=frame, text="") 
    error_label.place(x=20, y=395) 
    entry1 = customtkinter.CTkEntry(master=frame, width=160, placeholder_text="Enter window title:")
    entry1.place(x=20, y=368)
    submit = customtkinter.CTkButton(master=frame, width=100, text="submit", command=title_change) 
    submit.place(x=190, y=368) 

    #this creates a horizontal slider that goes from 20 to 100 and calls the function (update slider) 
    #i have updated the upper bound of the slider from 30 to 1000
    slider1 = customtkinter.CTkSlider(frame, from_=0, to=30, width=160, orientation="horizontal",command=update_slider_value)
    slider1.set(0) #sets the slider to start at 50
    slider1.place(x = 20, y =328) #places it right under the colour picker button
    slider_label = customtkinter.CTkLabel(master=frame, text="Nodes: " + str(round(slider1.get())))
    slider_label.place(x=20, y=298) #places it right above the slider
    submit_randomiser_button = customtkinter.CTkButton(master=frame, width=100, text="randomise", command=submit_randomiser) #calls the print_entry function 
    submit_randomiser_button.place(x=190, y=321) #places the button at desired coordinates 
    
    #creates the colour button with the text "pick a colour" and which calls the "choose colour" function
    colour_button = customtkinter.CTkButton(master=frame, width=270, height=40, text="reset canvas", command=clear_canvas, fg_color="#c70d00", hover_color="black")
    colour_button.place(x=20, y=420) #places this near the bottom of the screen
    
    colour_button = customtkinter.CTkButton(master=frame, width=270, height=40, text="reset canvas", command=clear_canvas, fg_color="#c70d00", hover_color="black")
    colour_button.place(x=20, y=420) #places this near the bottom of the screen
    
    switch = customtkinter.CTkSwitch(text="advanced stats",command=switcher,master=label1)
    if settings_info["stats"]:
        switch.select()
    switch.place(x=20)
    menu.mainloop() # this is the main program loop that keeps the window open
    return settings_info

#this code will run if the program isn't being imported
if __name__ == "__main__":
    node_name = "node 1" #sets the node name
    print("\n\/")
    print (settingsmenu(node_name,
                        [[(1, (401, 234), 50, '', None, None), [3, 4], {3: 0.1, 4: 0.1}], [(2, (804, 150), 50, 'end', None, 'destination'), [3], {3: 0.1}], [(3, (630, 463), 50, '', None, None), [2, 1], {2: 0.1, 1: 0.1}], [(4, 
(263, 507), 50, 'start', None, 'starting'), [1], {1: 0.1}]],
                        None,
                        "title",
                        "image",False)) #prints the return value
    print("\n^")
