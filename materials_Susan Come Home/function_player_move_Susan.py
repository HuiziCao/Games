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


# Drawable base class
class DrawObject:
    def __init__(self, win):
        self.win = win
    
    def draw(self):
        
        raise NotImplementedError("Draw method should be implemented by subclasses.")
        

# Sun class
class Sun(DrawObject):
    def __init__(self, win):
        super().__init__(win)
        self.shape = Circle(Point(1500, 100), 50)
        self.shape.setFill(macaron_red)
        self.shape.setOutline(macaron_yellow)

    def draw(self):
        self.shape.draw(self.win)

# Ground class
class Ground(DrawObject):
    def __init__(self, win):
        super().__init__(win)
        self.shape = Rectangle(Point(0, 556), Point(1600, 900))
        self.shape.setFill(color_rgb(139, 198, 139))
        self.shape.setOutline(color_rgb(139, 198, 139))

    def draw(self):
        self.shape.draw(self.win)

# Sheep class
class Sheep(DrawObject):
    def __init__(self, win):
        super().__init__(win)
        self.original_position = Point(800, 530)  
        self.body = Circle(self.original_position, 50)
        self.body.setFill(macaron_white)
        self.body.setOutline(macaron_white)

        self.hairpin = Polygon(Point(65, 380), Point(95, 390), Point(105, 390),
                               Point(135, 380), Point(120, 420), Point(100, 405),
                               Point(80, 420))
        self.hairpin.move(700, 100)
        self.hairpin.setFill(macaron_red)
        self.hairpin.setOutline(macaron_yellow)

    def draw(self):
        self.body.draw(self.win)
        self.hairpin.draw(self.win)

    def introduce(self):
        
        # 一
        intro_text_part1 = Text(self.body.getCenter(), "Hi! I'm Susan the Sheep.")
        intro_text_part1.setSize(20)
        intro_text_part1.setStyle('bold')
        intro_text_part1.draw(self.win)
        self.win.getMouse()  
        intro_text_part1.undraw()  

        # 二
        intro_text_part2 = Text(self.body.getCenter(), "Click different spots on the screen to move me. How many times to you want to?")
        intro_text_part2.setSize(20)
        intro_text_part2.setStyle('bold')
        intro_text_part2.draw(self.win)
        self.win.getMouse()  
        intro_text_part2.undraw()


    def move_to(self, point):
        # Get current center of the sheep
        current_center = self.body.getCenter()
        dx = point.getX() - current_center.getX()
        dy = point.getY() - current_center.getY()
        self.body.move(dx, dy)
        self.hairpin.move(dx, dy)

    def move_n_times(self, n):
        for _ in range(n):
            click_point = self.win.getMouse()
            self.move_to(click_point)
        self.return_to_original_position()

    def return_to_original_position(self):
        self.move_to(self.original_position)
        return_text = Text(self.original_position, "No matter where I go, I'll always wear my red bow, "
                                                   "because it's a gift from my grandmother! It means a lot to me!")
        return_text.setSize(20)
        return_text.setStyle('bold')
        return_text.draw(self.win)
        self.win.getMouse()
        # time.sleep(5)  
        return_text.undraw()

def main():
    

    # open the graphics window
    win = GraphWin("Susan's Journey", 1600, 900)
    win.setBackground(color_rgb(153, 212, 247))

    sun = Sun(win)
    sun.draw()
    ground = Ground(win)
    ground.draw()

    susan = Sheep(win)
    susan.draw()
    susan.introduce()
    
    # Get the number of moves from the user before opening the graphics window
    try:
        n_moves = int(input("Click different spots on the screen to move Susan. How many times do you want to move her? "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    # Allow the player to move Susan n times
    susan.move_n_times(n_moves)

if __name__ == "__main__":
    main()
