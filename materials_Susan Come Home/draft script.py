# picture.py (Susan's Journey)
# author : Huizi Cao(Amery) , pictures(except home_town_flower) are from https://weibo.com/u/7537514484 which can be used without commercial use
# I hereby declare that i use a lot of model code from Zelle Graphics module documentation https://mcsp.wartburg.edu/zelle/python/graphics/graphics/graphref.html
# I took 10 hours to finish the assignment, it is fun though
# SORRY BUT SUPER IMPORTANT! I "#" all the parts that need to open pictures but these can work well definitely if you download the gif i provided in the same path as me, after downloading it you can remove the "#" and then try it please. They are very cute pictures!


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
    for _ in range(50):
        cloud.move(dx, dy)
        time.sleep(0.05)

# 1,2
cloud_moving(cloud1, 5, 0)
cloud_moving(cloud2, 5, 0)
# 3,4
cloud_moving(cloud3, -5, 0)
cloud_moving(cloud4, -5, 0)

# Sheep Susan
Susan = Circle(Point(100, 430), 50)
Susan.setFill("white")
Susan.setOutline("white")
Susan.draw(win)

# define hairpin
hairpin = Polygon(Point(65, 380),Point(95, 390), Point(105, 390), Point(135, 380),Point(120, 420),Point(100, 405),Point(80, 420))
hairpin.setFill("red")
hairpin.setOutline("yellow")
hairpin.draw(win)

# Sheep grandmother
def grandmother():
    
    # body
    body = Circle(Point(400, 390), 70)
    body.setFill("white")
    # body.setOutline("white")
    body.draw(win)

    # face
    face = Circle(Point(400, 375), 40)  
    face.setFill("white")
    face.setOutline("black")
    face.draw(win)

    # eyes
    # eye1 
    eye1 = Circle(Point(385, 365), 5)  
    eye1.setFill("black")
    eye1.draw(win)
    # eye2
    eye2 = Circle(Point(415, 365), 5)  
    eye2.setFill("black")
    eye2.draw(win)

    # nose
    nose = Circle(Point(400, 370), 3)  
    nose.setFill("pink")
    nose.draw(win)

    # mouse
    mouth = Oval(Point(395, 375), Point(405, 380)) 
    mouth.setFill("pink")
    mouth.draw(win)

    # eyeballs
    # left_eyeball
    left_eyeball = Oval(Point(385, 370), Point(390, 365))  
    left_eyeball.setFill("pink")
    left_eyeball.draw(win)
    # right_eyeball
    right_eyeball = Oval(Point(410, 370), Point(415, 365))  
    right_eyeball.setFill("pink")
    right_eyeball.draw(win)
    
    # checks
    # left_check
    left_check = Oval(Point(370, 370), Point(380, 365))  
    left_check.setFill("white")
    left_check.draw(win)
    # right_checks
    right_check = Oval(Point(420, 370), Point(430, 365))  
    right_check.setFill("white")
    right_check.draw(win)
    
    # arms
    # left_arm
    left_arm = Oval(Point(340, 370), Point(370, 400))  
    left_arm.setFill("white")
    left_arm.draw(win)
    # right_arm
    right_arm = Oval(Point(430, 370), Point(460, 400))  
    right_arm.setFill("white")
    right_arm.draw(win)

    # feet
    # foot1
    foot1 = Circle(Point(365, 450), 15)
    foot1.setFill("white")
    foot1.draw(win)
    # foot2
    foot2 = Circle(Point(435, 450), 15)
    foot2.setFill("white")
    foot2.draw(win)

    return[body, face, eye1, eye2, nose, mouth, left_eyeball, right_eyeball, left_check, right_check, left_arm, right_arm, foot1, foot2]


# Define apple tree model
def apple_tree_model(x, y):

    # Trunk
    trunk = Rectangle(Point(x, y), Point(x + 30, y + 90))
    trunk.setFill("brown")
    trunk.setOutline("brown")
    trunk.draw(win)
    
    # Leaves
    leaves = Circle(Point(x + 10 , y - 10), 50)
    leaves.setFill("green")
    leaves.draw(win)

    # Draw apples
    apple1 = Circle(Point(x - 20, y), 10)
    apple1.setFill("red")
    apple1.setOutline("red")
    apple1.draw(win)

    
    apple2 = apple1.clone()
    apple2.move(30, -10)
    apple2.draw(win)

    apple3 = apple1.clone()
    apple3.move(60, -20)
    apple3.draw(win)

    # it is very import to return all of them! otherwise it would return to none when tring to have more apple trees later
    return [trunk, leaves, apple1, apple2, apple3]


# define warm_home
def warm_home():

    # roof
    roof = Polygon(Point(250, 550), Point(550, 550), Point(400, 400))
    roof.setFill("pink")
    roof.setOutline("pink")
    roof.draw(win)


    # house body
    house = Rectangle(Point(250, 550), Point(550, 750))
    house.setFill("lightblue")
    house.setOutline("lightblue")
    house.draw(win)

    # door
    door = Rectangle(Point(350, 600), Point(450, 750))
    door.setFill("pink")
    door.setOutline("pink")
    door.draw(win)
    
    # hairpin
    hairpin = Polygon(Point(65, 380), Point(95, 390), Point(105, 390), Point(135, 380),Point(120, 420), Point(100, 405), Point(80, 420))
    hairpin.setFill("red")
    hairpin.setOutline("yellow")
    hairpin2 = hairpin.clone()
    # from（100，405）to（300,675),600-300=300,675-405=270
    hairpin2.move(300, 270)
    hairpin2.draw(win)

    # locker at the center
    locker = Circle(Point(400, 667.5), 5.5)
    locker.setFill("yellow")
    locker.setOutline("yellow")
    locker.draw(win)

    # windows with 8 glasses
    # left window with 4 glasses
    # glass1
    glass1 = Rectangle(Point(280, 600), Point(310, 630))
    glass1.setFill("yellow")
    glass1.setOutline("yellow")
    glass1.draw(win)
    # glass2
    glass2 = Rectangle(Point(280, 630), Point(310, 660))
    glass2.setFill("pink")
    glass2.setOutline("pink")
    glass2.draw(win)
    # glass3
    glass3 = Rectangle(Point(310, 600), Point(340, 630))
    glass3.setFill("lightgreen")
    glass3.setOutline("lightgreen")
    glass3.draw(win)
    # glass4
    glass4 = Rectangle(Point(310, 630), Point(340, 660))
    glass4.setFill("orange")
    glass4.setOutline("orange")
    glass4.draw(win)

    # right window with 4 glasses clone from left ones
    # glass5
    glass5 = glass1.clone()
    glass5.move(180, 0)
    glass5.draw(win)
    # glass6
    glass6 = glass2.clone()
    glass6.move(180, 0)
    glass6.draw(win)
    # glass7
    glass7 = glass3.clone()
    glass7.move(180, 0)
    glass7.draw(win)
    # glass8
    glass8 = glass4.clone()
    glass8.move(180, 0)
    glass8.draw(win)


# make sure to let the user click to continue
# this code get from zelle page 114 Example: clickPoint = win.getMouse()
# "getMouse() Pauses for the user to click a mouse in the window and returns where the mouse was clicked as a Point object"
def pause_for_click():
    clickPoint = win.getMouse()
    return clickPoint


# define how to open the image
# zelle graphics model documention-displaying images : https://mcsp.wartburg.edu/zelle/python/graphics/graphics/node13.html
# Displaying Images- images in a GraphWin. Most platforms will support at least PPM and GIF images. Display is done with an Image object. Images support the generic methods move(dx,dy), draw(graphwin), undraw(), and clone().
# Image(anchorPoint, filename) Constructs an image from contents of the given file, centered at the given anchor point. Can also be called with width and height parameters instead of filename. In this case, a blank (transparent) image is created of the given width and height (in pixels).
# img_path = "path(example:/Users/apple/Desktop/CS111F23/hometown_flower.gif)"
# img = Image(Point(400, 400), img_path)
# img.draw(win)
# pause_for_click()
# img.undraw()



# 1st scene: susan encounter setback
def encounter_setback():
    
    # from Zelle Graphics module documentation-Text Methods：Text(anchorPoint, textString) https://mcsp.wartburg.edu/zelle/python/graphics/graphics/node11.html
    setback_text = Text(Point(400, 155), "Susan encountered setbacks while she was away and lost her red butterfly hair clip.")

    # from Zelle Graphics module documentation-Text Methods：setFace(family) Changes the font face to the given family. Possible values are "helvetica", "courier", "times roman", and "arial". Example: message.setFace("arial")
    setback_text.setFace("times roman")

    # from Zelle -Text Methods：setSize(point) Changes the font size to the given point size. Sizes from 5 to 36 points are legal. Example: message.setSize(18)
    setback_text.setSize(18)

    # from Zelle -Text Methods：setTextColor(color) Sets the color of the text to color. Note: setFill has the same effect.Example: message.setTextColor("pink")
    setback_text.setTextColor("black")
    
    # from Zelle -Text Methods：:setStyle(style) Changes font to the given style. Possible values are: "normal", "bold", "italic", and "bold italic". Example: message.setStyle("bold")
    setback_text.setStyle("bold italic")

    # draw the text
    setback_text.draw(win)

    # pause for user to click
    pause_for_click()

    # remove hairpin
    hairpin.undraw()
    setback_text.undraw()
    
    pause_for_click()

    # Susan
    # open the image of susan
    # zelle graphics model documention-displaying images : https://mcsp.wartburg.edu/zelle/python/graphics/graphics/node13.html
    # img0_path = "/Users/apple/Desktop/CS111F23/susan.gif"
    # img0 = Image(Point(400, 400), img0_path)
    
    # show pictures
    # img0.draw(win)

    # pause_for_click()

    # img0.undraw()

encounter_setback()



# 2ed scene: susan misses hometown
def miss_hometown():

    miss_hometown_text = Text(Point(400, 155), "Susan misses the osmanthus flowers from her hometown.")
    miss_hometown_text.setFace("times roman")
    miss_hometown_text.setSize(18)
    miss_hometown_text.setTextColor("black")
    miss_hometown_text.draw(win)

    pause_for_click()
    
    # open picture of hometown flower
    # img1_path = "/Users/apple/Desktop/CS111F23/hometown_flower.gif"
    # img1 = Image(Point(400, 400), img1_path)
    
    # show picture
    # img1.draw(win)

    # pause_for_click()

    # img1.undraw()

    # hometown flower figure
    hometown_flower = Circle(Point(600, 250), 30)
    hometown_flower.setFill("lightyellow")
    hometown_flower.draw(win)

    miss_hometown_text.undraw()

miss_hometown()



# 3rd scene: susan decides to vist her grandma
def decide_to_visit_grandma():
    

    decide_text = Text(Point(400, 155), "Susan decides to visit her hometown to see her grandmother Fluffy.")
    decide_text.setFace("times roman")
    decide_text.setSize(18)
    decide_text.setTextColor("black")
    decide_text.draw(win)

    pause_for_click()
    
    # open picture of grandma
    # img2_path = "/Users/apple/Desktop/CS111F23/grandma.gif"
    # img2 = Image(Point(400, 400), img2_path)

    # show picture
    # img2.draw(win)
    
    # pause_for_click()

    # img2.undraw()
    
    # draw grandmother()
    lovely_grandmother = grandmother()
    time.sleep(5)
    pause_for_click()

    # move Susan out of the window
    Susan.undraw()

    # move grandmother out of the window
    for i in lovely_grandmother:
        i.undraw()
    decide_text.undraw()

decide_to_visit_grandma()



# 4th scene: susan connects with nature
def connect_with_nature():
    
    connect_text = Text(Point(400, 155), "Susan connects with her hometown's loved ones and nature.")
    connect_text.setFace("times roman")
    connect_text.setSize(18)
    connect_text.setTextColor("black")
    connect_text.draw(win)

    pause_for_click()
    
    # open hometown_house picture
    # img3_path = "/Users/apple/Desktop/CS111F23/hometown_house.gif"
    # img3 = Image(Point(400, 680), img3_path)

    # show picture
    # img3.draw(win)
    
    # pause_for_click()

    # img3.undraw()

    # hometown_house figure
    hometown_house = Rectangle(Point(350, 550), Point(450, 650))
    hometown_house.setFill("brown")
    hometown_house.draw(win)

    connect_text.undraw()

connect_with_nature()



# 5th scene: susan picks apples
# 5th scene: susan picks apples 
# mention that this part took me 2 hours! made so many mistakes and vscode report each mistake, and i do ccorrections by the hint by vscode

def pick_apples():
    # Clear previous text

    # Using a list to draw all of apple trees
    apple_trees = []
    # i want 7 apple trees
    for i in range(7):
        x = 80 + i * 100
        y = 420
        # my_apple_trees = apple_tree_model(x, y) = [trunk, leaves, apple1, apple2, apple3]
        my_apple_tree = apple_tree_model(x, y)
        # use .append() to include every apple true
        apple_trees.append(my_apple_tree)
    
    # basket
    basket = Rectangle(Point(375, 600), Point(425, 650))
    basket.setFill("brown")
    basket.draw(win)

    # pick_apples_text
    pick_apples_text = Text(Point(400, 155), "Please use the mouse to click on the apples to help the sheep pick them. How many do you want to pick?")
    pick_apples_text.setFace("times roman")
    pick_apples_text.setSize(18)
    pick_apples_text.setTextColor("black")
    pick_apples_text.setStyle("bold italic")
    pick_apples_text.draw(win)
    
    thank_you_text = Text(Point(400, 155), "Thank you for helping Susan and Fluffy.")
    thank_you_text.setFace("times roman")
    thank_you_text.setSize(18)
    thank_you_text.setTextColor("black")
    thank_you_text.setStyle("bold italic")
    
    
    # the range of apples user can pick is from 1 to 21 (3*7)
    n=int(input("how many apples do you want to pick(please enter an integer, range from 1 to 21):"))

    # initialize picked_apples
    picked_apples = 0

    # let the user picks as many as apples as they want
    while picked_apples < n:

        # still wait for click to pick more apples every time it not reach to n, that is why i use while loop
        # picked_apples == n is the condition to break
        clickPoint = pause_for_click()

        # we should include all of the apple tree because each of them have apples
        for my_apple_tree in apple_trees:

            # my_apple_trees = apple_tree_model(x, y) = [trunk, leaves, apple1, apple2, apple3]
            # I want apple1, apple2, apple3, so slice from 2 to 5 （n-1）
            apples = my_apple_tree[2:5]

            # consider every apple in apples  
            for i in apples:

                # i presents each apple
                # In Zelle page 117 ： get Center () Returns a clone of the center point of the circle
                # In Zelle page 116 : get X () Returns the x coordinate of a point. getY() Returns they coordinate of a point. 
                # i want to know whether the click is on apple, so we get click point(x,y), x should be in range of the apple's x range, y should be in range of the the apple's y range
                # apple is a circle has radius 10,so x range would from centerX-10 to centerX+10, so y range would from center Y-10 TO center Y+10 
                if i.getCenter().getX() - 10 <= clickPoint.getX() <= i.getCenter().getX() + 10 and i.getCenter().getY() -10 <= clickPoint.getY() <= i.getCenter().getY() + 10: 
                   
                   # In Zelle page 115 ：move (dx,dy) Moves the object dx units in the x direction and dy units in the y direction 
                   # move picked apple to the basket, basket = Rectangle(Point(375, 600), Point(425, 650)),let us use the point (400,625) which is the centerof the basket
                   # use .move(dx,dy)，so dx = 400 - apple center x , dy = 625 - apple center y
                   i.move(400-i.getCenter().getX(), 625-i.getCenter().getY())  

                   # record the numbers of apples be picked
                   picked_apples = picked_apples + 1

                   # the conditon to break the while loop is when the apples are enough (picked_apples == n)
                   if picked_apples == n:
                      # undraw the text
                      pick_apples_text.undraw()

                      # show thank you
                      thank_you_text.draw(win)

                      # let user click before break to give time if user want to see this scene for longer time even the apples are picked already
                      pause_for_click()

                      thank_you_text.undraw()

                      break

pick_apples()



# 6th scene: susan collects honey
def collect_honey():
    
    
    honey_text = Text(Point(400, 155), "Susan and her grandmother Fluffy collect honey together.")
    honey_text.setFace("times roman")
    honey_text.setSize(18)
    honey_text.setTextColor("black")
    honey_text.setStyle("bold italic")
    honey_text.draw(win)

    pause_for_click()
    
    # open pictures of bee and honey_jar
    # img4_path = "/Users/apple/Desktop/CS111F23/bee.gif"
    # img4 = Image(Point(310, 400), img4_path)

    # img4.draw(win)
    
    # pause_for_click()

    # img4.undraw()

    # img5_path = "/Users/apple/Desktop/CS111F23/honey_jar.gif"
    # img5 = Image(Point(850, -200), img5_path)
  
    # img5.draw(win)
    
    # pause_for_click()

    # img5.undraw()

    # figures of bee and honey_jar
    bee1 = Circle(Point(300, 350), 15)
    bee1.setFill("yellow")
    bee1.setOutline("yellow")
    bee1.draw(win)
    bee2 = Circle(Point(500, 350), 15)
    bee2.setFill("yellow")
    bee2.setOutline("yellow")
    bee2.draw(win)
    honey_jar = Rectangle(Point(380, 450), Point(420, 500))
    honey_jar.setFill("brown")
    honey_jar.draw(win)

    honey_text.undraw()

collect_honey()



# 7th scene: susan says godbye to grandma
def say_goodbye():
    

    goodbye_text = Text(Point(400, 155), "Susan says goodbye to her grandmother Fluffy.")
    goodbye_text.setFace("times roman")
    goodbye_text.setSize(18)
    goodbye_text.setTextColor("black")
    goodbye_text.setStyle("bold italic")
    goodbye_text.draw(win)

    pause_for_click()

    goodbye_text.undraw()

say_goodbye()



# 8th scene: susan feels warmth of home
def feel_warm_home():
    
    feel_warm_home_text = Text(Point(400, 155), "Susan feels the warmth and happiness of home.")
    feel_warm_home_text.setFace("times roman")
    feel_warm_home_text.setSize(18)
    feel_warm_home_text.setTextColor("black")
    feel_warm_home_text.setStyle("bold italic")
    feel_warm_home_text.draw(win)
    pause_for_click()

    # figure of home
    warm_home()
    
    pause_for_click()

    # open warm_home picture
    # img6_path = "/Users/apple/Desktop/CS111F23/warm_home.gif"
    # img6 = Image(Point(580, 500), img6_path)

    # img6.draw(win)
    
    # pause_for_click()

    # img6.undraw()

    feel_warm_home_text.undraw()
    
    
    thank_you_bye_text = Text(Point(400, 155), "Thank you so much! Byebye!")
    thank_you_bye_text.setFace("times roman")
    thank_you_bye_text.setSize(18)
    thank_you_bye_text.setTextColor("black")
    thank_you_bye_text.setStyle("bold italic")
    thank_you_bye_text.draw(win)

feel_warm_home()



# close the window
win.getMouse()
win.close()