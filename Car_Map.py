import tkinter as tk # importing tkinter library so we can use graphics
import random


# NOTE: Tkinter window's top left corner is (0,0). 
# X-axis increases when goes right. Y-axis increases when goes down

# global variables for specifying window's size
WINDOW_HEIGHT = 150.0
WINDOW_WIDTH = 150.0

car_queue = [] # list/array for storing car
obstacle_queue = [] # list position array for obstacles

# function to find coordinates of given spot
def find_coords(width, height, l_pos, l_f_pos, r_f_pos, r_pos):
    # l_pos, l_f_pos, r_f_pos, and r_pos are the distances btwn car and object
    coords = [0,0]
    f_pos = (l_f_pos + r_f_pos)/2
    coords[0] = (l_pos + WINDOW_WIDTH - r_pos - width)/2 # x coord
    coords[1] = WINDOW_HEIGHT - f_pos - height # y coord

    return coords

class Car:
    def __init__(self, canvas):
        # initialize position of car and map it on canvas
        # <self> refers to the class itself. Below codes are essentially "attributes" for Car's class
        # self.sensors = arduino.read() # !!! make sure to have an output for arduino at the start of the arduino !!!
        self.width = 25.5
        self.height = 24.3
        self.sensors = [0, WINDOW_HEIGHT-self.height, WINDOW_HEIGHT-self.height, WINDOW_WIDTH-self.width]
        coords = find_coords(self.width, self.height, self.sensors[0], self.sensors[1], self.sensors[2], self.sensors[3])
        self.x = coords[0]
        self.y = coords[1]
        self.draw(canvas)

    def draw(self, canvas):
        # remove car from the list if the list is not empty
        if len(car_queue) != 0: # len() return amount of data in the parameter
            canvas.delete(car_queue[0]) # delete car from canvas. If don't do this, then previous car will stay there
            car_queue.pop()

        #size_x = 25.5
        #size_y = 24.3

        # create blue car on canvas. create_square(x1, y1, x2, y2) draws square 
        # Topleft is at (x1,y1). Bottomright at (x2,y2)
        x = canvas.create_rectangle(self.x, WINDOW_HEIGHT-self.height-self.y, self.x + self.width, WINDOW_HEIGHT-self.y, fill='blue')
        # store car at the list
        car_queue.append(x)

class Obstacle:
    def __init__ (self, x, y, size_x, size_y, canvas):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

        self.draw(canvas)
    
    def draw(self, canvas):
        # remove obstacle from the list if the list is not empty
        # if len(obstacle_queue) != 0: # len() return amount of data in the parameter
        #     obstacle_queue.pop()

        size_x = 19.3
        size_y = 16.5

        # create white obstacle on canvas. create_square(x1, y1, x2, y2) draws a square.
        # Top left is at (x1, y1). Bottom right at (x2, y2)
        x = canvas.create_rectangle(self.x, WINDOW_HEIGHT-self.height-self.y, self.x + self.width, WINDOW_HEIGHT-self.y, fill='yellow')
        # store obstacle at the list
        obstacle_queue.append(x)

# check if car is close to obstacle
def check(obstacle, car, canvas, window):
    ### don't think we need this code since arduino does it for us

    # if obstacle.x - 4 <= car.x <= obstacle.x + 4 \
    # and obstacle.y - 4 <= car.y <= obstacle.y + 4:
        #not sure if these numbers are good enough^^^
    #    canvas.delete(car[0]) # erase car from canvas
    #    car_queue.pop() # remove car from list
        ## code for moving around obstacle

    ### pseudocode for this part
    # is_obstacle = arduino.read()
    # 
    


    # exit()
    

    window.after(100, check, car, obstacle, canvas, window)

def main():

    counter = 0
    
    window = tk.Tk() # create window pop-up
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black') # Canvas widget is for drawing
    canvas.pack() # pack() organize, aka update, widgets onto canvas
    
    # create obstacle
    obstacle = Obstacle(canvas)
    # create car
    car = Car(canvas)

    window.after(100, check, car, obstacle, canvas, window) # call check() to check car and obstacle after 100 milliseconds
    window.mainloop() # tk.mainloop() -> keep looping until there's an update

main()