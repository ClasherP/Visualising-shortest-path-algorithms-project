from tkinter import messagebox #imports the correct library

def show_error_message(error_message): #defines a function to show an error message
    messagebox.showerror("Error", (error_message)) #shows an error message with the perameter text
    
def confirmation(message): #gets the message from the perameter
    result = messagebox.askyesno("Confirmation", message) #brings up a yes/no box with the message
    return result #returns either true or false


if __name__ == "__main__":
    show_error_message("hello")
    confirmation("ok")