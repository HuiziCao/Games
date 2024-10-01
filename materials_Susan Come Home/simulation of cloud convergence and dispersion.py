

# imports all functions directly from the graphics module and time
from graphics import *
import time

# create a window for graphics
win = GraphWin("Susan's Journey", 800, 800)

# change the background of the window
win.setBackground("lightblue")

# draw the sun which is a circle
sun = Circle(Point(700, 100), 50)
sun.setFill("red")
sun.setOutline("yellow")
sun.draw(win)

# draw the ground which is a rectangle
ground = Rectangle(Point(0, 500), Point(800, 800))
ground.setFill("green")
ground.setOutline("green")
ground.draw(win)

# clouds
# cloud1
cloud1 = cloud = Oval(Point(50, 200), Point(160, 250))
cloud1.setFill("white")
cloud1.setOutline("white")
cloud1.draw(win)
# cloud2
cloud2 = cloud1.clone()
cloud2.move(50, 30)
cloud2.draw(win)
# cloud3
cloud3 = cloud1.clone()
cloud3.move(580, 0)
cloud3.draw(win)
# cloud4
cloud4 = cloud1.clone()
cloud4.move(630, 30)
cloud4.draw(win)

# make it moving
def cloud_moving(cloud, dx, dy):
    for _ in range(12):
        cloud.move(dx, dy)
        time.sleep(0.05)


for i in range(10):
# 1,2
    cloud_moving(cloud1, 20, 0)
    cloud_moving(cloud2, 20, 0)
# 3,4
    cloud_moving(cloud3, -20, 0)
    cloud_moving(cloud4, -20, 0)


# 1,2
    cloud_moving(cloud1, -20, 0)
    cloud_moving(cloud2, -20, 0)
# 3,4
    cloud_moving(cloud3, 20, 0)
    cloud_moving(cloud4, 20, 0)
