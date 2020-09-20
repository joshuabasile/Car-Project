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
        sensor_string = SerialPort.read() # !!! make sure to have an output for arduino at the start of the arduino !!!
        self.sensors = sensor_string.split(',')
        self.width = 25.5
        self.height = 24.3
        # TEST: self.sensors = [0, WINDOW_HEIGHT-self.height, WINDOW_HEIGHT-self.height, WINDOW_WIDTH-self.width]
        coords = find_coords(self.width, self.height, self.sensors[0], self.sensors[1], self.sensors[2], self.sensors[3])
        self.x = coords[0]
        self.y = coords[1]
        self.draw(canvas)

    def getx(self):
        return self.x
    def gety(self):
        return self.y

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
    def __init__ (self, x, y, canvas):
        # x and y correspond to the left bottom corner of the object
        self.x = x
        self.y = y

        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

        self.draw(canvas)

    def set_side(self, side_length, canvas):
        if (self.left == 0):
            self.left = side_length
        elif (self.top == 0):
            self.top = side_length
        elif (self.right == 0):
            self.right = side_length
        elif (self.bottom == 0):
            self.bottom = side_length
            # try to draw rectangle now that we have set the side lengths
            self.draw(canvas)
    
    def draw(self, canvas):
        # remove obstacle from the list if the list is not empty
        if len(obstacle_queue) != 0: # len() return amount of data in the parameter
            canvas.delete(obstacle_queue[0])
            obstacle_queue.pop()
        # create white obstacle on canvas. create_square(x1, y1, x2, y2) draws a square.
        # Top left is at (x1, y1). Bottom right at (x2, y2)

        # don't draw until all four sides are found
        self.width = (self.left + self.right)/2
        self.height = (self.top + self.bottom)/2
        x = canvas.create_rectangle(self.x, WINDOW_HEIGHT-self.height-self.y, self.x + self.width, WINDOW_HEIGHT-self.y, fill='yellow')
        # store obstacle at the list
        obstacle_queue.append(x)

def check(car, obstacle_length, canvas, window):
    ### don't think we need this code since arduino does it for us

    # if obstacle.x - 4 <= car.x <= obstacle.x + 4 \
    # and obstacle.y - 4 <= car.y <= obstacle.y + 4:
        #not sure if these numbers are good enough^^^
    #    canvas.delete(car[0]) # erase car from canvas
    #    car_queue.pop() # remove car from list
        ## code for moving around obstacle

    # update/create new car - make the car move!
    new_car = Car(canvas)
    car_queue.append(new_car)

    # check sensors for obstacle
    sensor_string = SerialPort.read()
    sensors = sensor_string.split(',')
    num_of_turns = sensors(4)

    # find the distance between the car and the object


    window.after(100, check, car, obstacle_tracker, canvas, window)

def main():

    counter = 0
    
    window = tk.Tk() # create window pop-up
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black') # Canvas widget is for drawing
    canvas.pack() # pack() organize, aka update, widgets onto canvas

    # create car
    car = Car(canvas)

    # car starts with nothing but wall in the right sensor
    obstacle_length = 0

    window.after(100, check, car, obstacle_length, canvas, window) # call check() to check car and obstacle after 100 milliseconds
    window.mainloop() # tk.mainloop() -> keep looping until there's an update

main()