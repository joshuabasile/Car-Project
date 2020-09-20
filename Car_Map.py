import tkinter as tk  # importing tkinter library so we can use graphics
import random
import serial

# NOTE: Tkinter window's top left corner is (0,0).
# X-axis increases when goes right. Y-axis increases when goes down

# global variables for specifying window's size
WINDOW_HEIGHT = 150.0
WINDOW_WIDTH = 150.0

car_queue = []  # list/array for storing car
obstacle_queue = []  # list position array for obstacles


# function to find coordinates of given spot
def find_coords(width, height, l_pos, l_f_pos, r_f_pos, r_pos):
    # l_pos, l_f_pos, r_f_pos, and r_pos are the distances btwn car and object
    coords = [0, 0]
    f_pos = (l_f_pos + r_f_pos) / 2
    coords[0] = (l_pos + WINDOW_WIDTH - r_pos - width) / 2  # x coord
    coords[1] = WINDOW_HEIGHT - f_pos - height  # y coord

    return coords


class Car:
    def __init__(self, reset_car, SerialPort, canvas):
        # initialize position of car and map it on canvas
        # <self> refers to the class itself. Below codes are essentially "attributes" for Car's class
        #SerialPort = serial.Serial("COM5", "9600", timeout=1)
        self.width = 25.5
        self.height = 24.3
        sensor_string = SerialPort.readline()  # !!! make sure to have an output at the start of the arduino's run !!!
        sensor_string_decoded = str(sensor_string.decode('utf-8'))
        sensors = sensor_string_decoded.rstrip().split(',')
        if (sensors[0] != ''):
            for i in range(0, len(sensors)):  # convert to ints
                sensors[i] = float(sensors[i])*100
            sensors[-1] = sensors[-1]/100
            print(sensors)
            # TEST: self.sensors = [0, WINDOW_HEIGHT-self.height, WINDOW_HEIGHT-self.height, WINDOW_WIDTH-self.width]
            coords = find_coords(self.width, self.height, sensors[0], sensors[1], sensors[2], sensors[3])
            self.x = coords[0]
            self.y = coords[1]
            self.draw(canvas)
        elif (reset_car == True):
            self.x = 0
            self.y = 0

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def draw(self, canvas):
        # remove car from the list if the list is not empty
        if len(car_queue) != 0:  # len() return amount of data in the parameter
            canvas.delete(car_queue[0])  # delete car from canvas. If don't do this, then previous car will stay there
            car_queue.pop()

        # size_x = 25.5
        # size_y = 24.3

        # create blue car on canvas. create_square(x1, y1, x2, y2) draws square
        # Topleft is at (x1,y1). Bottomright at (x2,y2)
        x = canvas.create_rectangle(self.x, WINDOW_HEIGHT - self.height - self.y, self.x + self.width,
                                    WINDOW_HEIGHT - self.y, fill='blue')
        # store car at the list
        car_queue.append(x)


class Obstacle:
    def __init__(self, x, y, canvas):
        # x and y correspond to the left bottom corner of the object
        self.x = x
        self.y = y

        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

        self.numofsides = 0  # starts out with 0 known sides

        self.draw(canvas)

    def get_numofsides(self):
        return self.numofsides

    def set_side(self, side_length, canvas):
        if (self.left == 0):
            self.left = side_length
            self.numofsides = 1
        elif (self.top == 0):
            self.top = side_length
            self.numofsides = 2
        elif (self.right == 0):
            self.right = side_length
            self.numofsides = 3
        elif (self.bottom == 0):
            self.bottom = side_length
            self.numofsides = 4
            # try to draw rectangle now that we have set the side lengths
            self.draw(canvas)

    def draw(self, canvas):
        # remove obstacle from the list if the list is not empty
        # if len(obstacle_queue) != 0: # len() return amount of data in the parameter
        #    canvas.delete(obstacle_queue[0])
        #    obstacle_queue.pop()
        # create white obstacle on canvas. create_square(x1, y1, x2, y2) draws a square.
        # Top left is at (x1, y1). Bottom right at (x2, y2)

        # don't draw until all four sides are found
        self.width = (self.left + self.right) / 2
        self.height = (self.top + self.bottom) / 2
        x = canvas.create_rectangle(self.x, WINDOW_HEIGHT - self.height - self.y, self.x + self.width,
                                    WINDOW_HEIGHT - self.y, fill='yellow')
        # store obstacle at the list
        obstacle_queue.append(x)


def check(car, obstacle_length, obstacle_start, SerialPort, canvas, window):
    ### don't think we need this code since arduino does it for us

    # if obstacle.x - 4 <= car.x <= obstacle.x + 4 \
    # and obstacle.y - 4 <= car.y <= obstacle.y + 4:
    # not sure if these numbers are good enough^^^
    #    canvas.delete(car[0]) # erase car from canvas
    #    car_queue.pop() # remove car from list
    ## code for moving around obstacle

    # check sensors for obstacle
    #SerialPort = serial.Serial("COM5", "9600", timeout=1)
    sensor_string = SerialPort.readline()  # !!! make sure to have an output at the start of the arduino's run !!!
    sensor_string_decoded = str(sensor_string.decode('utf-8'))
    sensors = sensor_string_decoded.rstrip().split(',')
    if (sensors[0] != ''):
        new_car = Car(False, SerialPort, canvas)
        car_queue.append(new_car)

        for i in range(0, len(sensors)):  # convert to doubles
            sensors[i] = float(sensors[i])*100
        num_of_turns = sensors[4]

        # find position of obstacle
        obstacle_x = new_car.getx() + new_car.get_width() + sensors[3]
        obstacle_y = new_car.gety() + new_car.get_height() - 12.3  # takes into account the placement of the sensors

        # find out whether the object is a wall or not
        is_wall = (sensors[0] + new_car.get_width() + sensors[3] > 130)  # boolean
        if (not is_wall):  # start or continuation of an obstacle
            if (obstacle_start[0] == 0 and obstacle_start[1] == 0):  # start of obstacle
                obstacle_start[0] = obstacle_x
                obstacle_start[1] = obstacle_y
            else:  # continuation of an obstacle
                obstacle_length = abs(obstacle_start[0] - obstacle_x + obstacle_start[1] - obstacle_y)
        else:
            if (obstacle_start[0] == 0 and obstacle_start[1] == 0 and obstacle_length > 0):  # right after an obstacle side is finished
                if (num_of_turns == 0):  # first turn for this object
                    obstacle = Obstacle(obstacle_start[0], obstacle_start[1], canvas)
                    obstacle.set_side(obstacle_length, canvas)
                    obstacle_queue.append(obstacle)
                elif (num_of_turns > 0 and num_of_turns < 4):
                    # check to see if there is one object; if there is, then just add the side to it
                    obstacle_tracker = [0,
                                        0]  # first item is the number of sides the highest is (furthest down the list), second is which object this corresponds to
                    if (len(obstacle_queue) == 1):
                        obstacle_queue[0].set_side(obstacle_length)
                    else:
                        # check to see if the number of sides on the first equals the number of sides on the last
                        if (obstacle_queue[0].get_numofsides() == obstacle_queue[len(obstacle_queue) - 1].get_numofsides()):
                            # then, just add the side to the first object
                            obstacle_queue[0].set_side(obstacle_length)
                        else:
                            # first item is the number of sides the highest is (furthest down the list), second is which object this corresponds to
                            obstacle_tracker = [0, 0]
                            for i in range(0, len(obstacle_queue)):
                                # not sure how to figure out which obstacle to add to :/
                                obs = obstacle_queue[i]
                                if (obs.get_numofsides() >= num_of_turns):  # greater than or equal to, then keep track
                                    obstacle_tracker[0] = obs.get_numofsides()
                                    obstacle_tracker[1] = i
                            # update the obstacle that needs to be updated
                            obstacle_queue[obstacle_tracker[0] + 1].set_side(obstacle_length)
                            # obstacle.set_side(obstacle_length,canvas)
                obstacle_length = 0
                obstacle_start = [0, 0]
        car = new_car

    window.update()
    window.after(100, check, car, obstacle_length, obstacle_start, SerialPort, canvas, window)


def main():
    window = tk.Tk()  # create window pop-up
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black')  # Canvas widget is for drawing
    canvas.pack()  # pack() organize, aka update, widgets onto canvas

    SerialPort = serial.Serial("COM5", "9600", timeout=1)

    # create car
    car = Car(True, SerialPort, canvas)

    # car starts with nothing but wall in the right sensor
    obstacle_length = 0
    obstacle_start = [0, 0]

    window.after(100, check, car, obstacle_length, obstacle_start, SerialPort, canvas, window)  # call check() to check car and obstacle after 100 milliseconds
    window.mainloop()  # tk.mainloop() -> keep looping until there's an update


main()