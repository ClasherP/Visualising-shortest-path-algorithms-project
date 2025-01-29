import pygame

pygame.init() #innitialises pygame
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #sets the height/width of the window 
pygame.display.set_caption("prototype") #sets the title of the window

def drawLine(colour,start_coords,end_coords):
    pygame.draw.line(screen,colour,start_coords[0],end_coords[0])

def inCanvas(node_x, node_y, radius):
    if node_x - radius > 10 and node_x + radius < 1180: #checks if the X coordinates are in range 
        if node_y - radius > 10 and node_y + radius < 630: #checks if the Y coordinates are in range 
            return True
    return False

def draw_text(text, font, text_col,xy):
    img = font.render(text,True,text_col) #renders the text and text colour
    xy = (xy[0]-7,xy[1]-23) #sets coordinates to the middle of the circle 
    screen.blit(img, xy) #draws the text

def detect_circle(eventpos,circles):
    for num, circle in enumerate(circles):
        if pygame.math.Vector2(circle[0]).distance_to(eventpos) <= circle[1]: 
            return num
    return None 
        
text_font = pygame.font.SysFont("comic sans",30)

class Button():
    def __init__(self,text,colour,transparency,x,y,size): #constructor
        self.text = text
        self.xy = (x,y) #coordinates
        self.size = size
        self.perameters = pygame.Surface(size) #sets the size
        self.perameters.fill(colour) #fills the colour with an RGB (tuple) value
        self.perameters.set_alpha(transparency) #sets transparency
        self.img = text_font.render(text,True,(0,0,0)) #renders text to be put onto button
        
        #centering text
        self.middle_xy = (round(size[0]/2)+x,round(size[1]/2)+y) #sets mid point coordinates by halving the size of the button and summing the x/y coordinates
        
    def draw(self):
        centered_offset_x = 0 #declares the variable
        screen.blit(self.perameters, self.xy)  #draws button to screen
        for i in range(0,len(self.text)): #this itterates through every character in the text
            centered_offset_x = centered_offset_x + 8.65 #adds to the coordinates for every letter in the text on the button
        centered_coordinates = (self.middle_xy[0]-centered_offset_x,self.middle_xy[1]-20) #edits the coordinates of the actual text 
        screen.blit(self.img,centered_coordinates) #draws text on the button
        #pygame.draw.rect(screen,"red",(pygame.Rect(self.middle_xy[0],self.middle_xy[1],3,3))) #highlights the midpoint in red for trail and error testing 
    def coordinates(self):
        return self.xy
    def getsize(self):
        return self.size
circles = []
program_state = None
active_circle = None
run = True
buttons = []
lines = []
defult_size = (285,140)
first_link = None
second_link = None
ready_for_second_link = False
#defining buttons
button1 = Button("move",(5, 200, 235),200,10,650,defult_size) #creating an object from the button class
buttons.append((button1.coordinates(),button1.getsize())) #adding the first button to the button array
button2 = Button("delete",(255,0,127),134,307,650,defult_size) #creating an object from the button class
buttons.append((button2.coordinates(),button2.getsize())) #adding the second button to the button array
button3 = Button("spawn",(16, 222, 22),134,608,650,defult_size) #creating an object from the button class
buttons.append((button3.coordinates(),button3.getsize())) #adding the third button to the button array
button4 = Button("link",(242, 242, 5),134,905,650,defult_size) #creating an object from the button class
buttons.append((button4.coordinates(),button4.getsize())) #adding the fourth button to the button array



while run: #this is the game loop that'll run while the session is running 
    screen.fill("gray") #fills the screen in as the colour gray 
    #draws canvas box
    print (lines)
    pygame.draw.rect(screen, "white", (pygame.Rect(10,10,1180,630)))
    
    for itterator3,line in enumerate(lines):
        if line != None:
            try:
                drawLine(line[0],circles[line[1]],circles[line[2]])
            except IndexError:
                lines[itterator3] = None
        else:
            lines.remove(line)
                
    for itterator2,circle in enumerate(circles):
        pygame.draw.circle(screen, "black", circle[0],circle[1]+4) #draws the border to the screen
        pygame.draw.circle(screen, "white", circle[0],circle[1]) #draws the circles to the screen
        draw_text(str(circle[2]), text_font, (0,0,0), circle[0]) #draws a circle using a custom function

    button1.draw() #calls method
    button2.draw()
    button3.draw()
    button4.draw()

    if first_link != None:
        temp_link_node = circles[first_link] 
        pygame.draw.circle(screen, (255, 0, 21), temp_link_node[0],temp_link_node[1]+4) #draws the border to the screen  
        pygame.draw.circle(screen, "white", temp_link_node[0],temp_link_node[1]) #draws the circles to the screen
        draw_text(str(temp_link_node[2]), text_font, (0,0,0), temp_link_node[0]) #draws text to+ a circle using a custom function
    if second_link != None:
        temp_link_node = circles[second_link] 
        pygame.draw.circle(screen, (247, 60, 2), temp_link_node[0],temp_link_node[1]+4) #draws the border to the screen  
        pygame.draw.circle(screen, "white", temp_link_node[0],temp_link_node[1]) #draws the circles to the screen
        draw_text(str(temp_link_node[2]), text_font, (0,0,0), temp_link_node[0]) #draws text to+ a circle using a custom function


    for event in pygame.event.get(): #handles the events 
        #creating circles
        if event.type == pygame.MOUSEBUTTONDOWN and program_state == "spawn": #spawns a node if the spawn button has been pressed
            radius = 50
            text = len(circles)+1

            if inCanvas(event.pos[0],event.pos[1], radius) == True:
                circles.append(((event.pos[0], event.pos[1]), radius, text)) #adding anouther element to the circle tuples 
            #this makes a tuple and puts it in the circle array, with the first 
            #tuple element being an array and the second being the radius
            

        #moving boxes
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            priority = True #before the loop is entered the priority variable is set to true
            for itterator, button in enumerate(buttons): #itterates through every existing button
                if event.pos[0] >= button[0][0] and event.pos[0] <= button[0][0]+button[1][0]: #checks if the X coordinates are in range 
                    if event.pos[1] >= button[0][1] and event.pos[1] <= button[0][1]+button[1][1]: #checks if the Y coordinates are in range 
                        button_pressed = itterator+1 #sets the button being pressed to a variable 
                        priority = False #this variable is set to false so the node cannot be moved while a button has been pressed before it 
                        ready_for_second_link = False
                        if first_link != None and second_link != None and button_pressed == 4:
                            print ("put code here dummy")
                            print (first_link,second_link)
                            lines.append(("black",first_link,second_link))
                        first_link,second_link = None,None
                        if button_pressed == 1:
                            program_state = "move"
                        elif button_pressed == 2:
                            program_state = "delete"
                        elif button_pressed == 3:
                            program_state = "spawn"
                        elif button_pressed == 4:
                            program_state = "link"
            if priority == True and (program_state == "move" or program_state == "link"): #the event handler can only check for moving nodes while a button isn't being pressed 
                for num, circle in enumerate(circles):
                    if pygame.math.Vector2(circle[0]).distance_to(event.pos) <= circle[1]: 
                        #above says "if the distance to the circle is less than the radius"
                        active_circle = num 
        if event.type == pygame.MOUSEMOTION and program_state == "move":
            if active_circle != None:
                text = (circles[active_circle])[2] #active circle holds the number of the selected circle  
                circles[active_circle] = ((event.pos[0], event.pos[1]), circles[active_circle][1], text)   
                #the line above says when a circle is active the coordinates will be
                #set to the current mouse coordinates with the same radius  
        #dropping nodes
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and (program_state == "move" or program_state == "link"): 
        #only works if the program state is in move and the left moues button has been released 
            if active_circle != None and inCanvas(event.pos[0],event.pos[1],radius) == False: 
                #checks that there is an an active circle and the mouse position is outside of the canvas 
                circles[active_circle] = ((SCREEN_WIDTH/2,SCREEN_HEIGHT/2),circles[active_circle][1],circles[active_circle][2])
                #this just sets the coordinates of the circle to x:600 and y:400 and keeps the other 2 elements 
            active_circle = None
        #deleting boxes
        if event.type == pygame.MOUSEBUTTONDOWN and program_state == "delete":
            for num, circle in enumerate(circles):
                if pygame.math.Vector2(circle[0]).distance_to(event.pos) <= circle[1] and active_circle == None:
                    for i,line in enumerate(lines):
                        if line[1] == num or line[2] == num:
                            lines.remove(line)
                    circles.remove(circle)

        if event.type == pygame.QUIT: 
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and program_state == "link" and event.button == 1:
            first_link = detect_circle(event.pos,circles)
            ready_for_second_link = True
            print ("first one", first_link)
        elif event.type == pygame.MOUSEBUTTONDOWN and program_state == "link" and event.button == 3 and ready_for_second_link == True:
            second_link = detect_circle(event.pos,circles)
            print ("second one", second_link)
        
        
    #this block above looks at every event in the session so if i click the x button on my screen, it'll
    #register that as an event and exit the while loop 
            
    pygame.display.flip() #updates the screen

pygame.quit #quits the session once the while loop has stopped 






