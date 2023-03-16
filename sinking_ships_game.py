import random
from tkinter import Tk, Label, Button



# Player class:
class Player():

    def __init__(self):

        # Attributes:
        self.ships = []
        self.stage = 0

    def interact(self, x, y):

        # Creating a big ship:
        if self.stage == 0:

            self.stage = 1
            self.ships.append([x, y])

            # Filters:
            horizontal = False
            if random.randint(0, 1):
                horizontal = True

            if horizontal:
                if y == 0:
                    self.ships.append([x, y + 1])
                    self.ships.append([x, y + 2])
                elif y == 4:
                    self.ships.append([x, y - 1])
                    self.ships.append([x, y - 2])
                else:
                    self.ships.append([x, y - 1])
                    self.ships.append([x, y + 1])
            else:
                if x == 0:
                    self.ships.append([x + 1, y])
                    self.ships.append([x + 2, y])
                elif x == 4:
                    self.ships.append([x - 1, y])
                    self.ships.append([x - 2, y])
                else:
                    self.ships.append([x - 1, y])
                    self.ships.append([x + 1, y])
            
            return "nothing"

        # Creating a small ship:
        elif self.stage == 1:

            self.stage = 2

            # Ships can't be on the same spot:
            for i in range(3):
                if self.ships[i] == [x, y]:
                    # Closing the game:
                    root.destroy()

            # Create small ship:
            self.ships.append([x, y])

            return "nothing"

        # Attacking:
        else:
            for i in range(len(self.ships)):
                if self.ships[i] == [x, y]:
                    self.ships.pop(i)
                    return "red"
            return "white"


# Creating two objects:
left_player = Player()
right_player = Player()



#-----[Interface setup]-----

root = Tk()
root.title("Sinking ships game")


# Functions:
def left_click(x, y):
    result = left_player.interact(x, y)
    if left_radar[x][y]["bg"] == "red":
        pass
    elif result == "white":
        left_radar[x][y]["bg"] = "white"
    elif result == "red":
        left_radar[x][y]["bg"] = "red"

def right_click(x, y):
    result = right_player.interact(x, y)
    if right_radar[x][y]["bg"] == "red":
        pass
    elif result == "white":
        right_radar[x][y]["bg"] = "white"
    elif result == "red":
        right_radar[x][y]["bg"] = "red"

    # Says the coordinates of our last click for testing purposes:
    #label = Label(root, text = f"{x}, {y}")
    #label.grid(row = 10)


# Left radar:
left_radar = []
for x in range(5):
    left_radar.append([])
    for y in range(5):
        button = Button(root, bg = "blue", padx = 12, pady = 5, command = lambda x=x,y=y: left_click(x, y))
        button.grid(row = x, column = y)
        left_radar[x].append(button)

# Radar separator:
for i in range(5):
    button = Button(root, bg = "black", padx = 12, pady = 5)
    button.grid(row = i, column = 5)

# Right radar:
right_radar = []
for x in range(5):
    right_radar.append([])
    for y in range(6, 11):
        button = Button(root, bg = "blue", padx = 12, pady = 5, command = lambda x=x,y=y: right_click(x, y - 6))
        button.grid(row = x, column = y)
        right_radar[x].append(button)


# The game starts:
root.mainloop()
