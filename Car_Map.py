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
        # remove pacman from the list if the list is not empty
        if len(car_queue) != 0: # len() return amount of data in the parameter
            canvas.delete(car_queue[0]) # delete pacman from canvas. If don't do this, then previous pacman will stay there
            car_queue.pop() 

        size = 
        # create blue car on canvas. create_square(x1, y1, x2, y2) draws square 
        # Topleft is at (x1,y1). Bottomright at (x2,y2)
        x = canvas.create_rectangle(self.x - size, self.y - size, self.x + size, self.y + size, fill='blue')
        # store car at the list
        car_queue.append(x)

class Ghost:
    def __init__ (self, canvas):
        self.x = random.randrange(WINDOW_WIDTH)
        self.y = random.randrange(WINDOW_HEIGHT)
        self.draw(canvas) # random position for every new game
    
    def draw(self, canvas):
        # remove ghost from the list if the list is not empty
        if len(ghost_queue) != 0: # len() return amount of data in the parameter
            canvas.delete(ghost_queue[0]) # delete ghost from canvas. If don't do this, then previous ghost will stay there
            ghost_queue.pop() 

        size = 30
        # create white ghost on canvas. create_square(x1, y1, x2, y2) draws a square.
        # Top left is at (x1, y1). Bottom right at (x2, y2)
        x = canvas.create_rectangle(self.x - size, self.y - size, self.x + size, self.y + size, fill='white')
        # store ghost at the list
        ghost_queue.append(x)

# check if pacman is on top of dot or not
def check2(ghost, pacman, canvas, window):
    if ghost.x - 30 <= pacman.x <= ghost.x + 30\
        and ghost.y - 30 <= pacman.y <= ghost.y + 30:
        canvas.delete(pac_queue[0]) # erase pacmnan from canvas
        pac_queue.pop() # remove pacman from list
        print('GAME OVER!!')
        exit()
    

    window.after(100, check2, pacman, ghost, canvas, window)


def main():
    window = tk.Tk() # create window pop-up
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black') # create Canvas widget for drawing
    canvas.pack() # pack() organize, aka update, widgets onto canvas

    pacman = Pacman(canvas) # pass in canvas so pacman can be drawn
    window.bind("<KeyPress-Left>", lambda event: pacman.moveLeft(event, canvas)) # need to pass event, otherwise won't work
    window.bind("<KeyPress-Right>", lambda event: pacman.moveRight(event, canvas))
    window.bind("<KeyPress-Up>", lambda event: pacman.moveUp(event, canvas))
    window.bind("<KeyPress-Down>", lambda event: pacman.moveDown(event, canvas))

    dot = Dot(canvas)
    ghost = Ghost(canvas)

    window.after(100, check1, pacman, dot, canvas, window) # call check() to check dot&pacman after 100 milliseconds
    window.after(100, check2, pacman, ghost, canvas, window) #call check() to check ghost&pacman afrer 100 milliseconds
    window.mainloop() # tk.mainloop() -> keep looping until there's an update

main()



