import pygame
from node_edit_menu import editnodemenu
from edge_edit_menu import editedgemenu
from error_msg import show_error_message
from pygame import K_SPACE

print ("\n")
pygame.init() #innitialises pygame
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #sets the height/width of the window to the variables above
pygame.display.set_caption("prototype") #sets the title of the window
pygame.RESIZABLE = False

def drawGraph(graph,shortest_path):
    for node in graph: #itterates through the nodes in the graph
        for line in node[1]: #itterates through each line in the connection section of each node
            try: #it will try and draw a line the screen from the first link node to the end link node
                drawLine("black",node,graph[IndexFromNodeID(graph,line)],default_thickness) #draws a line using the drawLine function
            except TypeError: #if there is an error the program won't draw the line and will print "type error"
                print("Type Error: when drawing a line")
    # itterates through the shortest path array and draws a line to every node in the array
    for i in range(0, len(shortest_path)-1):#the -1 at the end is becuase there is no array infront of the last element
        # draws a line from the element at the index i and whatever the element infornt of i is
        drawLine("red",graph[IndexFromNodeID(graph,shortest_path[i])],graph[IndexFromNodeID(graph,shortest_path[i+1])],higher_thickness)
        
    #this is reversed so the nodes with the lower nodeID overlap with the other nodes since they'll be drawn first
    for node in reversed(graph): #itterates through each node in the graph 
        if node[0][4] == None: #checks if the colour element is empty (is = to None)
            pygame.draw.circle(screen, "black", node[0][1],node[0][2]+4) #draws a black border to the screen
        else: #this will run if a colour is in the element
            pygame.draw.circle(screen, node[0][4], node[0][1],node[0][2]+4) #draws a coloured border to the screen
        pygame.draw.circle(screen, "white", node[0][1],node[0][2]) #draws a white circle to the screen
        if node[0][3] == "" or node[0][3] == '': 
            draw_text(str(node[0][0]), text_font, (0,0,0), node[0][1])
        else:
            draw_text(str(node[0][3]), text_font, (0,0,0), (center_text(node[0][3],node[0][1],False))) 
        if node[0][5] != None: #checks if the node type is equal to nothing
            #this draws the starting letter of the node type 20px beneth the circles radius 
            draw_text(str(node[0][5][0]), text_font, (0,0,0), (node[0][1][0],node[0][1][1]+node[0][2]+20)) 

def getWeight(node1,node2): #takes 2 nodes as perameters
    links = node1[2] #assigns the weight dictionary of node1 to the variable links for readability
    node_ID2 = node2[0][0] #assigns the node ID of node 2 to a variable for readability
    for link in links.keys(): #this itterates through every element in the dictionairy  
        if link == node_ID2: #checks if the currentlly selected link equals the nodeID we're looking for 
            weight = (links[link]) #assigned the weight of that node id to the variable weight
            return weight #this breaks out of the for loop and returns the weight variable
    return None #a link wasn't found if the program gets here, so None is retured instead of the weight 

def drawLine(colour,start_node,end_node,thinckness): #takes colour, start coordinates and end coordinates as perameters 
    start_coords = start_node[0][1] #takes the starting coordinates of the line
    end_coords = end_node[0][1] #takes the ending coordinates of the line
    weight = getWeight(start_node,end_node) #this function returns the weight of 2 linked nodes 
    
    x_middle = start_coords[0] + ((end_coords[0]-start_coords[0])/2) #finds out the middle x coordinates of the line
    y_middle = start_coords[1] + ((end_coords[1]-start_coords[1])/2) #finds out the middle y coordinates of the line
    middle_coords = (x_middle,y_middle)
    #pygame.draw.circle(screen, "red", middle_coords, 5) #draws a red circle in the middle of the line 
    pygame.draw.line(screen,colour,start_coords,end_coords,thinckness) #this is an in-built pygame function that draws lines 
    if weight != defult_weight: # only draws a the weight if the weight is not 0 
        length = len(str(weight)) 
        if length == 1:
            pygame.draw.circle(screen, "white", middle_coords, 20) #draws a white circle at the mid point so the weight doesn't 
            draw_text(str(weight),text_font,"black",middle_coords) #this draws the weight over that white circle
        elif length == 2:
            pygame.draw.circle(screen, "white", (middle_coords[0],middle_coords[1]), 25) #draws a white circle at the mid point so the weight doesn't 
            draw_text(str(weight),text_font,"black",(middle_coords[0]-10,middle_coords[1])) #this draws the weight over that white circle
        elif length == 3:
            pygame.draw.circle(screen, "white", (middle_coords[0],middle_coords[1]), 35) #draws a white circle at the mid point so the weight doesn't 
            draw_text(str(weight),text_font,"black",(middle_coords[0]-20,middle_coords[1])) #this draws the weight over that white circle
        elif length == 4:
            pygame.draw.circle(screen, "white", (middle_coords[0],middle_coords[1]), 45) #draws a white circle at the mid point so the weight doesn't 
            draw_text(str(weight),text_font,"black",(middle_coords[0]-25,middle_coords[1])) #this draws the weight over that white circle
    
def drawIndividualNode(node, colour):
    pygame.draw.circle(screen, colour, node[0][1],node[0][2]+4) #draws the border to the screen
    pygame.draw.circle(screen, "white", node[0][1],node[0][2]) #draws the circles to the screen
    if node[0][3] == "" or node[0][3] == '':
        draw_text(str(node[0][0]), text_font, (0,0,0), node[0][1]) #draws a circle using a custom function
    else:
        draw_text(str(node[0][3]), text_font, (0,0,0), (center_text(node[0][3],node[0][1],False))) #draws a circle using a custom function

def center_text(text,coordinates,button):
    if button == True:
        centered_offset_x = 0 #declares the variable
        for i in range(0,len(text)-1): #this itterates through every character in the text
            centered_offset_x = centered_offset_x + 8.65 #adds to the coordinates for every letter in the text on the button
        centered_coordinates = (coordinates[0]-centered_offset_x,coordinates[1]-20) #edits the coordinates of the actual text 
        return centered_coordinates
    else:
        offset_x = 0
        for i in range(0,len(str(text))): #this itterates through every character in the text
            offset_x = offset_x + 7.5 #adds to the coordinates for every letter in the text on the button
        centered_coordinates = (coordinates[0]-offset_x,coordinates[1]) #edits the coordinates of the actual text
        return centered_coordinates 

def detectEdge(mousepos,graph): #takes the mouseclick and the graph as perameters 
    for node in graph: #itterates through every node in the graph
        for link in node[1]: #itterates through every link in the graph
            start_coords = node[0][1] #start coordinates = the coordinates of the first link node 
            end_coords = graph[IndexFromNodeID(graph, link)][0][1] #end coordinates = coordinates of the second link node
            if edge_clicked_boolean(mousepos, start_coords, end_coords): #detects if the edge has been clicked
                return (node[0][0], link) #returns the 2 linking nodes in a tuple (node1,node2)
    return None #returns None if no node is found

def edge_clicked_boolean(mousepos, start_coords, end_coords): #takes the mouse click, start coords and end coords as perameters
    distance = distance_to_edge(mousepos[0], mousepos[1], start_coords[0], start_coords[1], end_coords[0], end_coords[1])
    # above is a function i will write to calculate the distance to the line 
    tolerance = 7.5  #this maens that the program registers a click if it is < 5 pixels away from the edge
    if distance < tolerance: #compares the edge and the tolerance 
        return True #registers that the edge had been clicked 
    return False #registers that the edge has not been clicked

def distance_to_edge(x, y, start_x, start_y, end_x, end_y):
    # Calculate the squared distance from the point to the line segment
    x_vector = end_x - start_x #calculates the x vector
    y_vector = end_y - start_y #calculates the y vector
    
    # Calculating the dot product between two vectors tells us how much the mouse click
    # (x, y) aligns with the direction of the edge starting from (start_x, start_y).

    # The line below calculates the x-component of the vector from (start_x, start_y) to (x, y)
    # multiplied by the x-component of the direction vector (x_vector).
    x_component_contribution = (x - start_x) * x_vector 

    # The line below calculates the y-component of the vector from (start_x, start_y) to (x, y)
    # multiplied by the y-component of the direction vector (y_vector).
    y_component_contribution = (y - start_y) * y_vector

    # Sum up the contributions to get the dot product.
    dot = x_component_contribution + y_component_contribution
    
    point = dot / (x_vector * x_vector + y_vector * y_vector) 
    #the line above calculates the decimal percentage of how far along the closest point position to the mouse click is 
    point = max(0, min(1, point)) #this ensure the point doesn't go below 0 or exceed 1, if it does, point will equal 1/0

    #these lines below use the starting coordinate + the point and then multiplies this by the vector 
    #to find the closest point in the direction of the edge
    closest_x = start_x + point * x_vector 
    closest_y = start_y + point * y_vector

    #this is how Euclidean distance calculation is represented in code
    #the ** symbol means to the power of 
    #additionally ** 0.5 is the same as a square root calculation
    distance = ((x - closest_x) ** 2 + (y - closest_y) ** 2) ** 0.5
    
    return distance #returns the distance to the edge
    
def inCanvas(node_x, node_y, radius):
    if node_x - radius > 10 and node_x + radius < 1180: #checks if the X coordinates are in range 
        if node_y - radius > 10 and node_y + radius < 630: #checks if the Y coordinates are in range 
            return True
    return False

def detectButton(pos,buttons): #the perameter "pos"takes the mouse coordinates in a tuple  
    for i,button in enumerate(buttons): 
    #this itterates through every button in the button array and "i" keeps track of the current buttins index
        if pos[0] >= button[0][0] and pos[0] <= button[0][0]+button[1][0]: #checks if the X coordinates are in range 
            if pos[1] >= button[0][1] and pos[1] <= button[0][1]+button[1][1]: #checks if the Y coordinates are in range 
                return i #returns the index (which is the button that's being pressed)
    return None #if a button is not being pressed, None is returned

def draw_text(text, font, text_col,xy):
    img = font.render(text,True,text_col) #renders the text and text colour
    xy = (xy[0]-7,xy[1]-23) #sets coordinates to the middle of the circle 
    screen.blit(img, xy) #draws the text

def detect_circle(eventpos,circles): 
    #the perameter eventopos is the position of the mouse and circles is the array which stores the circles (like the graph array)
    for circle in circles: #itterates through the array of circles
        if pygame.math.Vector2(circle[0][1]).distance_to(eventpos) <= circle[0][2]: #checks if the mouse press is inside the radius of the circle 
            return circle #if the above statment is true then that is returned 
    return None #if nothing is detected than none is returned 

def remove_connection(graph,connection): #takes the graph and the connection to remove as a perameter
    for node in graph: #itterates through every node in the graph
        for link in node[1]: #itterates through every element in the connection array of the selected node 
            if link == active_circle[0][0]: #checks if there is a link with the same node ID as the node being remove   
                node[1].remove(connection[0][0]) #removes the connection with the node ID of the connection to be deleted
    return graph #returns the graph with the removed nodes 

def remove_weighted_connections(graph__,nodeID_to_remove):
    for node in graph__: #itterating through every node in the graph
        elements_to_check = [] #sets temp to an empty array
        dictionary = node[2] #assigns the weight dictionary to the dictonary variable (easier to read)
        for keys in dictionary.keys(): #this cycles through every key (nodeID in our case) in the dict
            elements_to_check.append(keys) #this appends the empty array with elements to remove 
        for elements in elements_to_check: #itterates through every item in the elements_to_check array
            if elements == nodeID_to_remove: #checks to see if the the element needs to be removed 
                dictionary.pop(nodeID_to_remove) #pops the element from the dictionary
    return graph #returns the full graph 

def check_if_linked(node1,node2): #takes 2 nodes to check as perameters
    node1_connections = node1[1] #assigns the connections array to a variable for readability
    node2_connections = node2[1] #assigns the connections array to a variable for readability
    nodeID1 =  node1[0][0] #assigns the nodeID to a variable for readability
    nodeID2 = node2[0][0] #assigns the nodeID to a variable for readability
    
    #checking node1s connections array
    for link in node1_connections: #this itterates through the connection array of node1
        if link == nodeID2: #checks whether node2s nodeID is in node1s connections
            return True #returns True if found
        
    #checking node2s connections array
    for link in node2_connections: #this itterates through the connection array of node2
        if link == nodeID1: #checks whether node1s nodeID is in node2s connections
            return True #returns True if found
        
    return False #returns false if not found
    
def remove_individual_connections(graph, nodes): #takes the graph and the 2 nodes to unlink as inputs
    nodeID1,nodeID2 = nodes #seperates the tuple into 2 variables 
    
    graph[IndexFromNodeID(graph,nodeID1)][1].remove(nodeID2) #takes node2s nodeID out of node1s connection array
    graph[IndexFromNodeID(graph,nodeID2)][1].remove(nodeID1) #takes node1s nodeID out of node2s connection array
    
    del graph[IndexFromNodeID(graph,nodeID1)][2][nodeID2] #removes node2s weight from node1s dictionary
    del graph[IndexFromNodeID(graph,nodeID2)][2][nodeID1] #removes node1s weight from node2s dictionary
    return graph #returns the graph with the removed links

def IndexFromNodeID(graph, nodeID): #the graph and nodeID of the requested node is being passed through as perameters 
    for i,node in enumerate(graph): 
    #this itterates through the graph array keeping track of the index (the i variable) with the enumerate function
        if node[0][0] == nodeID: 
        #this checks if the node ID of the selected node is the same as the nodeID of the requested node
            return i #this returns the index of the requested node in the graph array
    return None #this returns None if the node can't be found 

def update_node(node,dictionary):
    title = dictionary["name"] #assigns the title in the dict to the "title" variable
    colour = dictionary["color"] #assigns the colour in the dict to the "colour" variable
    radius = dictionary["radius"] #assigns the radius in the dict to the "radius" variable
    node_type = dictionary["type"] #assigns the node_type in the dict to the "node_type" variable
    
    if title != None: #checks if changes were made to the title
        #every element of the nodes tuple is being assigned with the same values, excluding the title
        node[0] = (node[0][0],node[0][1],node[0][2],title,node[0][4],node[0][5])
        
    if radius != None: #checks if changes were made to the radius
        #every element of the nodes tuple is being assigned with the same values, excluding the radius
        node[0] = (node[0][0],node[0][1],radius,node[0][3],node[0][4],node[0][5])
    
    if colour != None: #checks if changes were made to the colour
        #every element of the nodes tuple is being assigned with the same values, excluding the colour
        node[0] = (node[0][0],node[0][1],node[0][2],node[0][3],colour,node[0][5])
   
    if node_type == None: #checks if changes were made to the node_type 
        #every element of the nodes tuple is being assigned with the same values, excluding the node_type
        node[0] = (node[0][0],node[0][1],node[0][2],node[0][3],node[0][4],None)
    elif node_type == "starting": #checks if the node is a starting node
        #every element of the nodes tuple is being assigned with the same values, excluding the node_type 
        #which is set to "starting"
        node[0] = (node[0][0],node[0][1],node[0][2],node[0][3],node[0][4],"starting")
    elif node_type == "destination": #checks if the node is a destination node
        #every element of the nodes tuple is being assigned with the same values, excluding the node_type 
        #which is set to "destination"
        node[0] = (node[0][0],node[0][1],node[0][2],node[0][3],node[0][4],"destination")
        
    return node #returns the edited node to the program

def update_edge(graph,node1,node2,dictionary): #takes the graph and the 2 nodes to remove links from as parameters
    weigth_to_update = dictionary["weight"]  #assigns the weight to a new variable
    
    if weigth_to_update != None and weigth_to_update >= 0: #checks that there is a weight in the dictionary
        node1_index = IndexFromNodeID(graph,node1[0][0]) #sets this variable to the index of node1 using the "indexFromNodeID" function
        node2_index = IndexFromNodeID(graph,node2[0][0]) #sets this variable to the index of node2 using the "indexFromNodeID" function
        
        #updates node1s connections dictionary. The connection to node2s nodeID is being set to the "weight_to_update" variable
        graph[node1_index][2].update({node2[0][0]:weigth_to_update}) 
        #updates node2s connections dictionary. The connection to node1s nodeID is being set to the "weight_to_update" variable
        graph[node2_index][2].update({node1[0][0]:weigth_to_update})

    return graph #returns the full graph 

def gen_nodeID(graph_):
    if graph_ == []:
        nodeID_ = 0
    else:
        maxID_ = 0
        for node in graph_:
            if node[0][0] > maxID_:
                maxID_ = node[0][0]
        nodeID_ = maxID_
    return nodeID_

def dijkstra(graph):
    infinity = 999999999999 # Infinity is just a really big number
    node_estimated_cost_dict = {} # Dictionary to store estimated costs 
    nodes_explored = [] # array to store explored nodes
    previous_node = {} # dictionary to store previous node of each node

    for node in graph: #cycles through each node in the graph 
        if node[0][5] == "destination": #checks if a node is the destination node 
            destination = node[0][0] #assigns a destination node
        if node[0][5] == "starting":#checks if a node is the starting node 
            node_estimated_cost_dict.update({node[0][0]:0}) #updates the nodes estimated cost as 0
        else:
            #if a node is not the starting node then the estimated cost is set to infinity
            node_estimated_cost_dict.update({node[0][0]:infinity})
        #fills the previous nodes with a nodeID key and a None value
        previous_node.update({node[0][0]:None}) 
            
    while True:
        lowest_cost = infinity #sets the origonal low cost to infinity, meaning any number will be higher than it
        lowest_node = None #sets the lowest costing node to None
        #itterates through the nodes, while asigning the nodeID and the cost to the designated varibe
        #at the end of this for loop, the lowest_node/cost should be equal to the lowest costs
        for node_id, cost in node_estimated_cost_dict.items(): 
            if node_id not in nodes_explored and cost < lowest_cost: #checks to see if the selected node has the lowest cost
                lowest_cost = cost #assigns the lowest cost
                lowest_node = node_id #assigns the lowest costing nodes nodeID  
    
        #this will only be True is no node cost is lower than infinity
        #since this will never be False, it means there are no nodes left
        if lowest_node == None: 
            break  #every node has been explored
        #adding the exploring node to the explored array
        nodes_explored.append(lowest_node)
        # Checks if the exploration node is the destination node
        if lowest_node == destination:
            break
        
        #looks at connection of the exploring nodes connection array
        for connection in graph[IndexFromNodeID(graph, lowest_node)][1]: 
            if connection not in nodes_explored: #this will be True if the connection hasn't been explored
                #calculates the weights of the connection node and linking nodes
                weight = getWeight(graph[IndexFromNodeID(graph, lowest_node)], graph[IndexFromNodeID(graph, connection)])
                calculated_cost = node_estimated_cost_dict[lowest_node] + weight #calculated cost is calculated (estimated cost + weight)
                if calculated_cost < node_estimated_cost_dict[connection]: #this checks if the calculated cost is less than the estimated cost
                    node_estimated_cost_dict[connection] = calculated_cost #sets the estimated cost of the node to the calculated cost
                    previous_node[connection] = lowest_node #sets the previous node of the connection to the lowest costing node

    #makes shortest path from the previous node dictionary
    shortest_path = [] #sets the shorting path to an empty array
    current_node = destination #sets the destination node to the current node
    #the currnet node will only = one when it looks at the starting nodes previous node
    while current_node != None: #while the current node doesn't = nonde
        shortest_path.append(current_node) #adds the shortest node to the shortest path array
        current_node = previous_node[current_node] #sets the current_node to the current nodes prior node 
    return shortest_path

def is_graph_valid(graph):
    destination_tally = 0 #declares a destination node tally
    starting_tally = 0 #declares a starting node tally
    for node in graph: #cycles through each node in the graph
        if node[0][5] == "starting": #checks if the node is a starting node
            starting_tally = starting_tally + 1 #this keeps a tally of the graphs starting nodes
        elif node[0][5] == "destination": #checks if the node is a destination node
            destination_tally = destination_tally + 1 #this keeps a tally of the graphs destination nodes
    
    if starting_tally == 1 and destination_tally == 1: #checks to see if there's only one of each type of node
        return True #returns True if there's only one of each type of node
    else:
        return False #returns False if there is less/more than one of each node
    
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
        
    def draw(self,border):
        if border == False:
            screen.blit(self.perameters, self.xy)  #draws button to screen
            screen.blit(self.img,center_text(self.text,self.middle_xy,True)) #draws text on the button
        if border == True:
            border_box = pygame.Surface((self.size[0]+10,self.size[1]+10)) #sets the size
            border_box.fill("black") #fills the colour with an RGB (tuple) value
            screen.blit(border_box, (self.xy[0]-5,self.xy[1]-5))  #draws button to screen
            self.perameters.set_alpha(256) #sets transparency
            screen.blit(self.perameters, self.xy)  #draws button to screen
            screen.blit(self.img,center_text(self.text,self.middle_xy,True)) #draws text on the button
    def coordinates(self):
        return self.xy
    def getsize(self):
        return self.size
    

    
    
#graph layout = [[(nodeID , coordinates tuple , radius , text , colour , node type),[connections],{weights}],[node#2],[node#3]...]

run = True
graph = [[(1, (200, 100), 50, '', '#00ff00', 'starting'), [2, 3, 4], {2: 10, 3: 15, 4: 29}], [(2, (700, 231), 50, '', '#c0c0c0', None), [1, 5, 6], {1: 10, 5: 25, 6: 18}], [(3, (908, 175), 50, '', '#c0c0c0', None), [1, 7], {1: 15, 7: 22}], [(4, (1028, 84), 50, '', '#c0c0c0', None), [1, 8], {1: 29, 8: 17}], [(5, (107, 230), 50, '', '#c0c0c0', None), [2, 9], {2: 25, 9: 30}], [(6, (277, 309), 50, '', '#c0c0c0', None), [2, 7, 10], {2: 18, 7: 28, 10: 23}], [(7, (768, 350), 50, '', '#c0c0c0', None), [3, 6, 11], {3: 22, 6: 28, 11: 32}], [(8, (1064, 268), 50, '', '#c0c0c0', None), [4, 11, 12], {4: 17, 11: 18, 12: 1}], [(9, (108, 430), 50, '', '#c0c0c0', None), [5, 10, 13], {5: 30, 10: 35, 13: 40}], [(10, (626, 430), 50, '', '#c0c0c0', None), [6, 9, 13], {6: 23, 9: 35, 13: 26}], [(11, (736, 532), 50, '', '#c0c0c0', None), [7, 8], {7: 32, 8: 18}], [(12, (1092, 538), 50, '', '#c0c0c0', None), [8], {8: 1}], [(13, (280, 511), 50, '', '#ff0000', 'destination'), [9, 10], {9: 40, 10: 26}]]
buttons = []
defult_size = (285,140)
programState = ""
button_pressed = None
defult_weight = 0.1
holding_shift = False
left_shift = 1073742049
right_shift = 1073742053
first_link,second_link = None,None
previous_button = None
active_circle = None
temp2 = None
temp3 = None
temp4 = None
temp5 = None
text_font = pygame.font.SysFont("comic sans",30)
editing_node = None
nodeID = gen_nodeID(graph)
default_thickness = 1
higher_thickness = 3
dijkstra_array = []

#making buttons

button1 = Button("move",(5, 200, 235),200,10,650,defult_size) #creating an object from the button class
buttons.append((button1.coordinates(),button1.getsize())) #adding the first button to the button array
button2 = Button("delete",(255,0,127),134,307,650,defult_size) #creating an object from the button class
buttons.append((button2.coordinates(),button2.getsize())) #adding the second button to the button array
button3 = Button("create",(16, 222, 22),134,608,650,defult_size) #creating an object from the button class
buttons.append((button3.coordinates(),button3.getsize())) #adding the third button to the button array
button4 = Button("link",(242, 242, 5),134,905,650,defult_size) #creating an object from the button class
buttons.append((button4.coordinates(),button4.getsize())) #adding the fourth button to the button array
button5 = Button("edit",(255,128,0),200,20,20,(100,50)) #creating an object from the button class
buttons.append((button5.coordinates(),button5.getsize())) #adding the fifth button to the button array
button6 = Button("run",(133, 224, 255),200,20,80,(100,50)) #creating an object from the button class
buttons.append((button6.coordinates(),button6.getsize())) #adding the sixth button to the button array
button7 = Button("settings",(177,177,177),100,130,20,(130,50)) #creating an object from the button class
buttons.append((button7.coordinates(),button7.getsize())) #adding the seventh button to the button array

while run: #this is the game loop that'll run while the session is running 
    screen.fill("gray") #fills the screen in as the colour gray 
    pygame.draw.rect(screen, "white", (pygame.Rect(10,10,1180,630))) #draws canvas box
    drawGraph(graph,dijkstra_array)
    if first_link != None: #if a first link exsists
        drawIndividualNode(first_link,(127, 0, 255)) #an individual node will be drawn with a purple colour (RGB)
    if second_link != None: #if a second link exsists
        drawIndividualNode(second_link,(0,0, 255)) #an individual node will be drawn with a blue colour (RGB)
    if active_circle != None and active_circle != second_link and active_circle != first_link and programState != "delete":
        drawIndividualNode(graph[IndexFromNodeID(graph, active_circle[0][0])],(122, 4, 9)) 
    button1.draw(False) #calls method
    button2.draw(False)
    button3.draw(False)
    button4.draw(False)
    button5.draw(False)
    button6.draw(False)
    button7.draw(False)
    
    #this will be true if the "run" button was the last to be pressed
    if programState == "run": 
        #this runs the dijkstra function and assigns the shortest path array to the "dijkstra_array" variable
        if is_graph_valid(graph) == True:
            dijkstra_array = dijkstra(graph)
        else:
            show_error_message("Inadequate amount of starting / destination nodes") 
            programState = None
    #the program will run the else statment if the run button wasn't pressed last
    else:
        #sets the dijkstra_array to an empty array
        dijkstra_array = []
                    
    for event in pygame.event.get(): #handles the events 
        #holding shift
        if event.type == pygame.KEYDOWN and (event.key == right_shift or event.key == left_shift):
            holding_shift = True
        elif event.type == pygame.KEYUP and (event.key == right_shift or event.key == left_shift):
            holding_shift = False
        #active circle code
        if event.type == pygame.MOUSEBUTTONDOWN: #detects if a mousebutton is being held down 
            editing_node = None
            temp3 = detect_circle(event.pos,graph) #detects the current circle using the detect_circle function
            if temp3 != None: #checks if there is a circle being clicked on or not
                active_circle = temp3 #the node stored in the temporary variable is assigned to active_circle
        if event.type == pygame.MOUSEBUTTONUP: #detects if a mouse button has been let go
            temp3 = active_circle #assigns the active circle to temp3
            try:
                if temp3 != None and inCanvas(event.pos[0],event.pos[1],temp3[0][2]) == False:
                    temp2 = graph[IndexFromNodeID(graph,temp3[0][0])]
                    graph[IndexFromNodeID(graph, temp3[0][0])] = [(temp2[0][0],(SCREEN_WIDTH/2,SCREEN_HEIGHT/2),temp2[0][2],temp2[0][3],temp2[0][4],temp2[0][5]),temp2[1],temp2[2]]
            except:
                print("Avoided out of bounds error")
            active_circle = None

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #detects if the left mouse button is pressed
            temp = detectButton(event.pos,buttons) #detecting a button press using the fun
            if temp != None: #this will be True if a button has been pressed 
                if first_link != None and second_link != None: #if there is no first/second link
                    if temp == 3 and previous_button == 3: #and if the link button was pushed before
                        if check_if_linked(first_link, second_link) == False: #checks if the 2 nodes are linked 
                            
                            #first linking node
                            weight1 = graph[IndexFromNodeID(graph,first_link[0][0])][2] #assigns the dictionary as the weight1 variable
                            weight1.update({second_link[0][0]:defult_weight}) #this apends the dictionary with the linking node id and the weight
                            graph[IndexFromNodeID(graph,first_link[0][0])][1].append(second_link[0][0]) #this is appends the connections array
                            
                            #second linking node
                            graph[IndexFromNodeID(graph,second_link[0][0])][1].append(first_link[0][0])#this is appends the connections array
                            weight2 = graph[IndexFromNodeID(graph,second_link[0][0])][2] #assigns the dictionary as the weight2 variable
                            weight2.update({first_link[0][0]:defult_weight})#this apends the dictionary with the linking node id and the weight
                        else:
                            print("node",first_link[0][0],"is already linked to",second_link[0][0]) #this is an error message saying you can't link
                first_link,second_link = None,None #resets the first and second link nodes 
                button_pressed = temp #sets the variable button pressed to temp, 
                #these lines detect the button press and sets the program state.
                if button_pressed == 0: 
                    programState = "move"
                elif button_pressed == 1:
                    programState = "delete"
                elif button_pressed == 2:       
                    programState = "create"
                elif button_pressed == 3:
                    programState = "link"
                elif button_pressed == 4:
                    programState = "edit"
                elif button_pressed == 5:
                    programState = "run"
                elif button_pressed == 6:
                    programState = "settings"
                previous_button = button_pressed
                
            elif temp == None: #if no button has been pressed 
                
                if programState == "create": #if the create button has been pressed 
                    radius = 50 #sets the radius of the node to 50 pixels
                    if inCanvas(event.pos[0],event.pos[1], radius) == True: #checks if the node is inside the canvas
                        nodeID = nodeID + 1 #increments the node ID by one 
                        if graph == []:
                            nodeID = 1
                        graph.append([(nodeID,event.pos,radius,"",None,None),[],{}]) 
                        #the above code appends the graph array setting the defult coordinates to the current mouse position
                
                if programState == "link": #this detects if the link button has been pressed 
                    if holding_shift != True: #holding_shift is a variable that is True when a shift button is being held down
                        first_link = detect_circle(event.pos,graph) #this assigns the active node to the first_link variable  
                    else:
                        second_link = detect_circle(event.pos,graph) #this assigns the active node to the second_link variable  
                
                if programState == "delete" or programState == "run": #if the "delete" button has been pressed
                    if active_circle != None and programState != "run": #and if there is an active circle set (to avoid any errors)
                        graph.remove(active_circle) #the active circle (which is the node being clicked) is removed from the graph array
                        graph = remove_weighted_connections(graph,active_circle[0][0])
                        graph = remove_connection(graph, active_circle) #this removes all the connections to the deleted node
                       #this line above resets the whole graph with some removes edge connections using a custom fuDnction
                    else: #if no node is detected
                        temp4 = detectEdge(event.pos,graph) #assigns temp4 to the edge detected
                        if temp4 != None: #if an edge is detected
                            graph = remove_individual_connections(graph,temp4) #the graph is reasigned with the removed links
                            
                if programState == "edit": #checks if the edit button was last pressed
                    if detect_circle(event.pos,graph) != None: #if a circle is being clicked
                        editing_node = detect_circle(event.pos,graph) #assigns the node to as variable
                        if editing_node[0][3] == "": #checks if the node has a namde
                            node_title = (str(editing_node[0][0]))  #sets the title to the nodeID
                        else: #program will go here the node has a name
                            node_title = editing_node[0][3] #sets the title to the node name
                        #the line below calls the editnodemenu function (which opens the menu) and passes these perameters through 
                        node_changes = editnodemenu(node_title,editing_node[0][5],editing_node[0][4],editing_node[0][2])
                        #updates the node attributes using my update_node() function 
                        graph[IndexFromNodeID(graph,editing_node[0][0])] = update_node(editing_node,node_changes)
                    elif detectEdge(event.pos,graph) != None: #checks that an edge is being clicked
                        
                        edge_node_ids = detectEdge(event.pos,graph) #the "detect edge" function returns the edge ids
                        
                        edge_link_1 = (graph[IndexFromNodeID(graph,edge_node_ids[0])]) #asigns one of the linking nodes to the variable
                        edge_link2 = (graph[IndexFromNodeID(graph,edge_node_ids[1])]) #asigns the other linking nodes to the variable
                        
                        #calls the edge menu function and uses the "getweight(node1,node2)" function to find the clicked edges weight
                        edge_info = editedgemenu(getWeight(edge_link_1,edge_link2)) 
                        #updates the graph with the "update_edge" function 
                        graph = update_edge(graph,edge_link_1,edge_link2,edge_info)

                        

        if programState == "move" and event.type == pygame.MOUSEMOTION: #this checks if the program is in the "move" state and if the mouse is currently moving 
            if active_circle != None: #checks if there is an active circle (a circle currently being clicked)
                temp2 = graph[IndexFromNodeID(graph,active_circle[0][0])] #the active circle node is being selected with a custom function and assigned to the variable temp2
                graph[IndexFromNodeID(graph, active_circle[0][0])] = [(temp2[0][0],(event.pos[0], event.pos[1]),temp2[0][2],temp2[0][3],temp2[0][4],temp2[0][5]),temp2[1],temp2[2]] 
                #the active nodes coordinates is being set to whatever the mouse position id, and all the other elements like nodeID an connections are being set to the same values 
            
        
        if event.type == pygame.QUIT: 
            run = False
            print ("graph array:\n",graph)
    pygame.display.flip() #updates the screen

pygame.quit #quits the session once the while loop has stopped 