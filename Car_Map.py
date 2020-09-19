import tkinter as tk # importing tkinter library so we can use graphics


# NOTE: Tkinter window's top left corner is (0,0). 
# X-axis increases when goes right. Y-axis increases when goes down

# global variables for specifying window's size
WINDOW_HEIGHT = 150
WINDOW_WIDTH = 150

car_queue = [] # list/array for storing car
obstacle_queue = [] # list positon array for obstacles

class Car:
    def __init__(self, canvas):
        # initialize position of car and map it on canvas
        # <self> refers to the class itself. Below codes are essentially "attributes" for Car's class
        self.x = 5
        self.y = 5
        self.draw(canvas)

    def draw(self, canvas):
        # remove car from the list if the list is not empty
        if len(car_queue) != 0: # len() return amount of data in the parameter
            canvas.delete(car_queue[0]) # delete pacman from canvas. If don't do this, then previous pacman will stay there
            car_queue.pop() 

        size.x = 25.5
        size.y = 24.3
        size = [size.x, size.y]

        # create blue car on canvas. create_square(x1, y1, x2, y2) draws square 
        # Topleft is at (x1,y1). Bottomright at (x2,y2)
        x = canvas.create_rectangle(self.x - size.x, self.y - size.y, self.x + size.x, self.y + size.y, fill='blue')
        # store car at the list
        car_queue.append(x)

class Obstacle:
    def __init__ (self, canvas):
        self.x = random.randrange(WINDOW_WIDTH)
        self.y = random.randrange(WINDOW_HEIGHT)
        self.draw(canvas) # random position for 1 obstacle (TEST!!!)
    
    def draw(self, canvas):
        # remove obstacle from the list if the list is not empty
        if len(obstacle_queue) != 0: # len() return amount of data in the parameter
            obstacle_queue.pop()

        size.x = 19.3
        size.y = 16.5
        # create white obstacle on canvas. create_square(x1, y1, x2, y2) draws a square.
        # Top left is at (x1, y1). Bottom right at (x2, y2)
        x = canvas.create_rectangle(self.x - size, self.y - size, self.x + size, self.y + size, fill='white')
        # store obstacle at the list
        obstacle_queue.append(x)

# check if car is close to obstacle
def check(obstacle, car, canvas, window):
    if obstacle.x - 4 <= car.x <= obstacle.x + 4\  
    #not sure these numbers are good enough ^^^
        and obstacle.y - 4 <= car.y <= obstacle.y + 4:
        #not sure if these numbers are good enough^^^
        canvas.delete(car[0]) # erase car from canvas
        car_queue.pop() # remove car from list
        ## code for moving around obstacle
        exit()
    

    window.after(100, check, car, obstacle, canvas, window)