

from graphics import *
import time
from math import pi, cos, sin





macaron_light_blue = color_rgb(173, 216, 230)  
macaron_red = color_rgb(255, 105, 97)               
macaron_white = color_rgb(255, 250, 240)                  
macaron_black = color_rgb(0, 0, 0)  
macaron_brown = color_rgb(182, 142, 142)  
macaron_green = color_rgb(169, 209, 142)  
macaron_orange = color_rgb(255, 179, 71)    
macaron_pink = color_rgb(255, 182, 193)        
macaron_yellow = color_rgb(255, 255, 133)      
macaron_light_green = color_rgb(144, 238, 144) 
macaron_basket_brown = color_rgb(210, 180, 140)  
macaron_yellow = color_rgb(255, 255, 133)      
macaron_light_yellow = color_rgb(255, 255, 153)  

rainbow_green = color_rgb(139, 198, 139)
rainbow_blue =color_rgb(153, 212, 247)

# create a window for graphics
win = GraphWin("Susan's Journey", 1600, 900)

# change the background of the window
win.setBackground(color_rgb(153, 212, 247))

# draw the sun which is a circle
sun = Circle(Point(1500, 100), 50)
sun.setFill(macaron_red)
sun.setOutline(macaron_yellow)
sun.draw(win)

# draw the ground which is a rectangle
ground = Rectangle(Point(0, 556), Point(1600, 900))
ground.setFill(color_rgb(139, 198, 139))
ground.setOutline(color_rgb(139, 198, 139))
ground.draw(win)

# clouds
# cloud1
cloud1 = Oval(Point(50, 200), Point(160, 250))
cloud1.setFill(macaron_white)
cloud1.setOutline(macaron_white)
cloud1.draw(win)
# cloud2
cloud2 = cloud1.clone()
cloud2.move(50, 30)
cloud2.draw(win)
# cloud3
cloud3 = cloud1.clone()
cloud3.move(1380, 0)
cloud3.draw(win)
# cloud4
cloud4 = cloud1.clone()
cloud4.move(1430, 30)
cloud4.draw(win)

# make it moving
def cloud_moving(cloud, dx, dy):
    for _ in range(51):
        cloud.move(dx, dy)
        time.sleep(0.02)

# 1,2
cloud_moving(cloud1, 12.6, 0)
cloud_moving(cloud2, 12.6, 0)
# 3,4
cloud_moving(cloud3, -12.6, 0)
cloud_moving(cloud4, -12.6, 0)

# Sheep Susan
Susan = Circle(Point(100, 430), 50)
Susan.move(0,100)
Susan.setFill(macaron_white)
Susan.setOutline(macaron_white)
Susan.draw(win)

# define hairpin
hairpin = Polygon(Point(65, 380), Point(95, 390), Point(105, 390), Point(135, 380), Point(120, 420), Point(100, 405), Point(80, 420))
hairpin.move(0,100)
hairpin.setFill(macaron_red)
hairpin.setOutline(macaron_yellow)
hairpin.draw(win)




# Sheep grandmother
def grandmother():
    
    # body
    body = Circle(Point(400, 390), 70)
    body.setFill(macaron_white)
    # body.setOutline("white")  
    body.draw(win)

    # face
    face = Circle(Point(400, 375), 40)  
    face.setFill(macaron_white)
    face.setOutline(macaron_black)
    face.draw(win)

    # eyes
    # eye1 
    eye1 = Circle(Point(385, 365), 5)  
    eye1.setFill(macaron_black)
    eye1.draw(win)
    # eye2
    eye2 = Circle(Point(415, 365), 5)  
    eye2.setFill(macaron_black)
    eye2.draw(win)

    # nose
    nose = Circle(Point(400, 370), 3)  
    nose.setFill(macaron_pink)
    nose.draw(win)

    # mouse
    mouth = Oval(Point(395, 375), Point(405, 380)) 
    mouth.setFill(macaron_pink)
    mouth.draw(win)

    # eyeballs
    # left_eyeball
    left_eyeball = Oval(Point(385, 370), Point(390, 365))  
    left_eyeball.setFill(macaron_pink)
    left_eyeball.draw(win)
    # right_eyeball
    right_eyeball = Oval(Point(410, 370), Point(415, 365))  
    right_eyeball.setFill(macaron_pink)
    right_eyeball.draw(win)
    
    # checks
    # left_check
    left_check = Oval(Point(370, 370), Point(380, 365))  
    left_check.setFill(macaron_white)
    left_check.draw(win)
    # right_checks
    right_check = Oval(Point(420, 370), Point(430, 365))  
    right_check.setFill(macaron_white)
    right_check.draw(win)
    
    # arms
    # left_arm
    left_arm = Oval(Point(340, 370), Point(370, 400))  
    left_arm.setFill(macaron_white)
    left_arm.draw(win)
    # right_arm
    right_arm = Oval(Point(430, 370), Point(460, 400))  
    right_arm.setFill(macaron_white)
    right_arm.draw(win)

    # feet
    # foot1
    foot1 = Circle(Point(365, 450), 15)
    foot1.setFill(macaron_white)
    foot1.draw(win)
    # foot2
    foot2 = Circle(Point(435, 450), 15)
    foot2.setFill(macaron_white)
    foot2.draw(win)

    return [body, face, eye1, eye2, nose, mouth, left_eyeball, right_eyeball, left_check, right_check, left_arm, right_arm, foot1, foot2]

# Define apple tree model
def apple_tree_model(x, y):

    # Trunk
    trunk = Rectangle(Point(x, y), Point(x + 30, y + 90))
    trunk.setFill(macaron_brown)
    trunk.setOutline(macaron_brown)
    trunk.draw(win)
    
    # Leaves
    leaves = Circle(Point(x + 10 , y - 10), 50)
    leaves.setFill(color_rgb(76, 165, 100))
    leaves.setOutline(color_rgb(76, 165, 100))
    leaves.draw(win)

    # Draw apples
    apple1 = Circle(Point(x - 20, y), 10)
    apple1.setFill(macaron_red)
    apple1.setOutline(macaron_red)
    apple1.draw(win)
    
    apple2 = apple1.clone()
    apple2.move(30, -10)
    apple2.draw(win)

    apple3 = apple1.clone()
    apple3.move(60, -20)
    apple3.draw(win)

    return [trunk, leaves, apple1, apple2, apple3]









  

# define warm_home
def warm_home():

    # roof
    roof = Polygon(Point(250, 550), Point(550, 550), Point(400, 400))
    roof.setFill(macaron_pink)
    roof.setOutline(macaron_pink)
    roof.draw(win)

    # house body
    house = Rectangle(Point(250, 550), Point(550, 750))
    house.setFill(macaron_light_blue)
    house.setOutline(macaron_light_blue)
    house.draw(win)

    # door
    door = Rectangle(Point(350, 600), Point(450, 750))
    door.setFill(macaron_pink)
    door.setOutline(macaron_pink)
    door.draw(win)
    
    # hairpin
    hairpin = Polygon(Point(65, 380), Point(95, 390), Point(105, 390), Point(135, 380),Point(120, 420), Point(100, 405), Point(80, 420))
    hairpin.setFill(macaron_red)
    hairpin.setOutline(macaron_yellow)
    hairpin2 = hairpin.clone()
    hairpin2.move(300, 270)
    hairpin2.draw(win)

    # locker at the center
    locker = Circle(Point(400, 667.5), 5.5)
    locker.setFill(macaron_yellow)
    locker.setOutline(macaron_yellow)
    locker.draw(win)

    # windows with 8 glasses
    # left window with 4 glasses
    glass1 = Rectangle(Point(280, 600), Point(310, 630))
    glass1.setFill(macaron_yellow)
    glass1.setOutline(macaron_yellow)
    glass1.draw(win)
    glass2 = Rectangle(Point(280, 630), Point(310, 660))
    glass2.setFill(macaron_pink)
    glass2.setOutline(macaron_pink)
    glass2.draw(win)
    glass3 = Rectangle(Point(310, 600), Point(340, 630))
    glass3.setFill(macaron_light_green)
    glass3.setOutline(macaron_light_green)
    glass3.draw(win)
    glass4 = Rectangle(Point(310, 630), Point(340, 660))
    glass4.setFill(macaron_orange)
    glass4.setOutline(macaron_orange)
    glass4.draw(win)

    # right window with 4 glasses clone from left ones
    glass5 = glass1.clone()
    glass5.move(180, 0)
    glass5.draw(win)
    glass6 = glass2.clone()
    glass6.move(180, 0)
    glass6.draw(win)
    glass7 = glass3.clone()
    glass7.move(180, 0)
    glass7.draw(win)
    glass8 = glass4.clone()
    glass8.move(180, 0)
    glass8.draw(win)






# make sure to let the user click to continue
def pause_for_click():
    clickPoint = win.getMouse()
    return clickPoint








# 1st scene: susan encounter setback
def encounter_setback():
    
    # Text for the setback scene
    setback_text = Text(Point(400, 155), "Susan encountered setbacks while she was away and lost her red butterfly hair clip.")
    setback_text.setFace("times roman")
    setback_text.setSize(18)
    setback_text.setTextColor(macaron_black)  
    setback_text.setStyle("bold italic")
    setback_text.draw(win)

    # pause for user to click
    pause_for_click()

    # remove hairpin
    hairpin.undraw()
    setback_text.undraw()
    
    pause_for_click()


encounter_setback()








def draw_flower(center, petal_radius=5):
    white = color_rgb(255, 255, 255)
    flower_center = Circle(center, petal_radius / 2)
    flower_center.setFill(white)
    flower_center.draw(win)

    colors = [macaron_orange, macaron_yellow, macaron_orange, macaron_yellow, macaron_orange, macaron_yellow]
    for i in range(6):
        angle = pi / 3 * i
        petal_x = center.getX() + petal_radius * cos(angle)
        petal_y = center.getY() + petal_radius * sin(angle)
        petal = Circle(Point(petal_x, petal_y), petal_radius)
        petal.setFill(colors[i])
        petal.setOutline(colors[i])
        petal.draw(win)
    return flower_center

def place_on_circle(circle_center, circle_radius, angle):
    x = circle_center.getX() + circle_radius * cos(angle)
    y = circle_center.getY() + circle_radius * sin(angle)
    return Point(x, y)

def draw_pentagon_points(center, radius):
    points = []
    for i in range(5):
        angle = pi / 2 + i * 2 * pi / 5
        points.append(place_on_circle(center, radius, angle))
    return points

def flower_tree_model(x, y, flower_size, trunk_height=80, trunk_width=20):
    trunk = Rectangle(Point(x, y), Point(x + trunk_width, y - trunk_height))
    trunk.setFill(macaron_brown)
    trunk.setOutline(macaron_brown)
    trunk.draw(win)
    
    leaves_center = Point(x + trunk_width / 2, y - trunk_height)
    leaves_radius = trunk_height * 0.75
    leaves = Circle(leaves_center, leaves_radius)
    leaves.setFill(macaron_green)
    leaves.setOutline(macaron_green)
    leaves.draw(win)

    pentagon_radius = leaves_radius - flower_size
    pentagon_points = draw_pentagon_points(leaves_center, pentagon_radius)

    flowers = []
    for point in pentagon_points:
        flower_center = draw_flower(point, flower_size)
        flowers.append(flower_center)

    flower_center = draw_flower(leaves_center, flower_size)
    flowers.append(flower_center)

    return [trunk, leaves] + flowers


def miss_hometown():
    miss_hometown_text = Text(Point(400, 155), "Susan misses the osmanthus flowers from her hometown.")
    miss_hometown_text.setFace("times roman")
    miss_hometown_text.setSize(18)
    miss_hometown_text.setTextColor(macaron_black)
    miss_hometown_text.draw(win)

    win.getMouse()  # Pause for a click

    # Ensure flower tree elements are only drawn once
    flower_tree_model(500, 555, 5, 80, 20)

    pause_for_click()
    
    miss_hometown_text.undraw()  # This clears the text

    win.getMouse()  # Wait for another click before closing the window

# Call the scene function
miss_hometown()









# 3rd scene: susan decides to visit her grandma
def decide_to_visit_grandma():
    
    decide_text = Text(Point(400, 155), "Susan decides to visit her hometown to see her grandmother Fluffy.")
    decide_text.setFace("times roman")
    decide_text.setSize(18)
    decide_text.setTextColor(macaron_black)  
    decide_text.draw(win)

    pause_for_click()
    
    
    
    # Draw grandmother
    lovely_grandmother = grandmother()  
    time.sleep(5)
    pause_for_click()

    # Move Susan out of the window
    Susan.undraw()

    # Move grandmother out of the window
    for i in lovely_grandmother:
        i.undraw()
    decide_text.undraw()

decide_to_visit_grandma()






# 4th scene: susan connects with nature
def connect_with_nature():
    
    connect_text = Text(Point(400, 155), "Susan connects with her hometown's loved ones and nature.")
    connect_text.setFace("times roman")
    connect_text.setSize(18)
    connect_text.setTextColor(macaron_black)  
    connect_text.draw(win)

    pause_for_click()
    


    # Hometown house figure
    hometown_house = Rectangle(Point(350, 550), Point(450, 650))
    hometown_house.setFill(macaron_brown)  
    hometown_house.draw(win)

    connect_text.undraw()

connect_with_nature()








# 5th scene: susan picks apples
def pick_apples():
    
    apple_trees = []
    
    for i in range(7):
        x = 80 + i * 100
        y = 420
        
        my_apple_tree = apple_tree_model(x, y)  
        
        apple_trees.append(my_apple_tree)
    
    # basket
    basket = Rectangle(Point(375, 600), Point(425, 650))
    basket.setFill(macaron_basket_brown)  
    basket.draw(win)

    # pick_apples_text
    pick_apples_text = Text(Point(400, 155), "Please use the mouse to click on the apples to help the sheep pick them. How many do you want to pick?")
    pick_apples_text.setFace("times roman")
    pick_apples_text.setSize(18)
    pick_apples_text.setTextColor(macaron_black)  
    pick_apples_text.setStyle("bold italic")
    pick_apples_text.draw(win)
    
    thank_you_text = Text(Point(400, 155), "Thank you for helping Susan and Fluffy.")
    thank_you_text.setFace("times roman")
    thank_you_text.setSize(18)
    thank_you_text.setTextColor(macaron_black)  
    thank_you_text.setStyle("bold italic")

    # the range of apples user can pick is from 1 to 21 (3*7)
    n=int(input("how many apples do you want to pick(please enter an integer, range from 1 to 21):"))

    # initialize picked_apples
    picked_apples = 0

    # let the user picks as many as apples as they want
    while picked_apples < n:

        
        clickPoint = pause_for_click()

        
        for my_apple_tree in apple_trees:

            
            apples = my_apple_tree[2:5]

            
            for i in apples:

                
                if i.getCenter().getX() - 10 <= clickPoint.getX() <= i.getCenter().getX() + 10 and i.getCenter().getY() -10 <= clickPoint.getY() <= i.getCenter().getY() + 10: 
                   
                   
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






macaron_honey_yellow = color_rgb(255, 223, 186)  
macaron_honey_brown = color_rgb(198, 140, 83)   

# 6th scene: susan collects honey
def collect_honey():
    
    honey_text = Text(Point(400, 155), "Susan and her grandmother Fluffy collect honey together.")
    honey_text.setFace("times roman")
    honey_text.setSize(18)
    honey_text.setTextColor(macaron_black)  # 使用马卡龙黑色
    honey_text.setStyle("bold italic")
    honey_text.draw(win)

    pause_for_click()
    
    
    # Figures of bee and honey_jar
    bee1 = Circle(Point(300, 350), 15)
    bee1.setFill(macaron_honey_yellow)  
    bee1.setOutline(macaron_honey_yellow)  
    bee1.draw(win)
    bee2 = Circle(Point(500, 350), 15)
    bee2.setFill(macaron_honey_yellow)  
    bee2.setOutline(macaron_honey_yellow)  
    bee2.draw(win)
    honey_jar = Rectangle(Point(380, 450), Point(420, 500))
    honey_jar.setFill(macaron_honey_brown)  
    honey_jar.draw(win)

    honey_text.undraw()

collect_honey()



# 7th scene: susan says goodbye to grandma
def say_goodbye():
    
    goodbye_text = Text(Point(400, 155), "Susan says goodbye to her grandmother Fluffy.")
    goodbye_text.setFace("times roman")
    goodbye_text.setSize(18)
    goodbye_text.setTextColor(macaron_black)  
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
    feel_warm_home_text.setTextColor(macaron_black)  
    feel_warm_home_text.setStyle("bold italic")
    feel_warm_home_text.draw(win)
    pause_for_click()

    # figure of home, "warm_home()" has been called, assumed to be already adjusted to macaron colors
    warm_home()
    
    pause_for_click()

    
    feel_warm_home_text.undraw()
    
    thank_you_bye_text = Text(Point(400, 155), "Thank you so much! Byebye!")
    thank_you_bye_text.setFace("times roman")
    thank_you_bye_text.setSize(18)
    thank_you_bye_text.setTextColor(macaron_black)  
    thank_you_bye_text.setStyle("bold italic")
    thank_you_bye_text.draw(win)

feel_warm_home()