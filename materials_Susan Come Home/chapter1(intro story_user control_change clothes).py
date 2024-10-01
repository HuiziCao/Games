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


# DrawObject class
class DrawObject:
    def __init__(self, win):
        self.win = win
    

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

class Move:
    def __init__(self, win, body, hairpin):
        self.win = win
        self.body = body
        self.hairpin = hairpin

    def move_step_by_step(self, point, steps=10):
        current_center = self.body.getCenter()
        dx, dy = point.getX() - current_center.getX(), point.getY() - current_center.getY()
        steps = int(max(abs(dx), abs(dy)) / steps) + 1

        for _ in range(steps):
            self.body.move(dx / steps, dy / steps)
            # hairpin
            self.hairpin.move(dx / steps, dy / steps)  
            time.sleep(0.01)

    def move_to(self, point):
        current_center = self.body.getCenter()
        dx = point.getX() - current_center.getX()
        dy = point.getY() - current_center.getY()
        self.body.move(dx, dy)
        # hairpin
        self.hairpin.move(dx, dy) 



class Sheep(Move):
    def __init__(self, win):
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
        self.hairpin.setOutline(macaron_yellow)
        self.player_name = ""

        super().__init__(win, self.body, self.hairpin)

    def draw(self):
        self.body.draw(self.win)
        self.hairpin.draw(self.win)

    def introduce(self):
        intro_text_part1 = Text(self.body.getCenter(), "Hi! I'm Susan the Sheep.")
        intro_text_part1.setSize(20)
        intro_text_part1.setStyle('bold')
        intro_text_part1.draw(self.win)
        self.win.getMouse()  
        intro_text_part1.undraw()  

        intro_text_part2 = Text(self.body.getCenter(), "Click different spots on the screen to move me. How many times do you want to?")
        intro_text_part2.setSize(20)
        intro_text_part2.setStyle('bold')
        intro_text_part2.draw(self.win)
        self.win.getMouse()  
        intro_text_part2.undraw()

    def move_n_times(self, n):
        if n > 0:
            click_point = self.win.getMouse()
            self.move_step_by_step(click_point)

            magic_text = Text(Point(self.win.getWidth() / 2, 20), "That was me walking. Now watch my magic!")
            magic_text.setSize(20)
            magic_text.setStyle('bold')
            magic_text.draw(self.win)
            self.win.getMouse()  # Wait for a click
            magic_text.undraw()

            for _ in range(n - 1):
                click_point = self.win.getMouse()
                self.move_to(click_point)

            self.return_to_original_position()

    def return_to_original_position(self):
        self.move_to(self.original_position)
        return_text = Text(self.original_position, "No matter where I go, I'll always wear my red hairpin, "
                                                   "because it's a gift from my grandmother! It means a lot to me!")
        return_text.setSize(20)
        return_text.setStyle('bold')
        return_text.draw(self.win)
        self.win.getMouse()
        return_text.undraw()
    
    def ask_player_name(self):
        # name
        name_question = Text(self.body.getCenter(), "Would you like to tell me what should i call you?")
        name_question.setSize(20)
        name_question.setStyle('bold')
        name_question.draw(self.win)
        self.player_name = input("Please enter your name: ")
        self.win.getMouse() 
        name_question.undraw()
        
        # greeting
        self.win.getMouse()
        greeting = Text(Point(self.win.getWidth() / 2, 50), f"Hello {self.player_name}, nice to meet you!")
        greeting.setSize(20)
        greeting.setStyle('bold')
        greeting.draw(self.win)
        self.win.getMouse()  
        greeting.undraw()

    def ask_about_story(self):
        story_question = Text(self.body.getCenter(), "Would you like to know more about me?")
        story_question.setSize(20)
        story_question.setStyle('bold')
        story_question.draw(self.win)
        self.win.getMouse()  
        story_question.undraw()

        # yes & no
        yes_option = Oval(Point(200, 400), Point(400, 450))
        yes_option.setFill(macaron_white)
        yes_option.draw(self.win)
        yes_text = Text(Point(300, 425), "Yes")
        yes_text.setSize(20)
        yes_text.setStyle('bold')
        yes_text.draw(self.win)

        no_option = Oval(Point(1200, 400), Point(1400, 450))
        no_option.setFill(macaron_white)
        no_option.draw(self.win)
        no_text = Text(Point(1300, 425), "No")
        no_text.setSize(20)
        no_text.setStyle('bold')
        no_text.draw(self.win)

        # wait for click
        clicked = False
        while not clicked:
            click_point = self.win.getMouse()
            if yes_option.p1.x <= click_point.x <= yes_option.p2.x and \
               yes_option.p1.y <= click_point.y <= yes_option.p2.y:
                clicked = True
                response_text = "I'm glad you want to know more about me. Let me tell you my story."
            elif no_option.p1.x <= click_point.x <= no_option.p2.x and \
                 no_option.p1.y <= click_point.y <= no_option.p2.y:
                clicked = True
                response_text = "Oops, I bet you clicked the wrong one! But I'd still like to share my story with you."

        yes_option.undraw()
        yes_text.undraw()
        no_option.undraw()
        no_text.undraw()

        response = Text(Point(self.win.getWidth() / 2, self.win.getHeight() / 2), response_text)
        response.setSize(20)
        response.setStyle('bold')
        response.draw(self.win)
        self.win.getMouse()  
        response.undraw()
    

    def offer_choices(self):
        selected_options = []
        # graphics
        main_options = []  

        while len(selected_options) < 3:
            option1 = self.create_option("my hometown", Point(200, 200), "my hometown" in selected_options)
            option2 = self.create_option("my current city", Point(800, 200), "my current city" in selected_options)
            option3 = self.create_option("my plan", Point(1400, 200), "my plan" in selected_options)
            main_options.extend([option1, option2, option3])

            clicked_option = self.get_clicked_option([option1, option2, option3])
            if clicked_option:
                self.handle_option_click(clicked_option, selected_options, main_options)

        # 主+子 完成后，移除主选项
        for option, text in main_options:
            option.undraw()
            text.undraw()







    def create_option(self, text, position):
        # crate option
        option = Oval(Point(position.x - 100, position.y - 50), Point(position.x + 100, position.y + 50))
        option.setFill(macaron_white)
        option.draw(self.win)
        option_text = Text(position, text)
        option_text.draw(self.win)
        return option, option_text
    





    def get_clicked_option(self, options):
        while True:
            click_point = self.win.getMouse()
            for option, option_text in options:
                if self.is_point_in_oval(click_point, option):
                    return option, option_text
            # click logic




    def is_point_in_oval(self, point, oval):
        # whether point in oval
        return oval.p1.x <= point.x <= oval.p2.x and oval.p1.y <= point.y <= oval.p2.y
    

    
   
    

    def handle_option_click(self, clicked_option, selected_options, main_options):
        option, option_text = clicked_option
        if option_text.getText() not in selected_options:
            if option_text.getText() == "my hometown":
                finished = self.tell_hometown_story()
            elif option_text.getText() == "my current city":
                finished = self.tell_现居地_story()
            elif option_text.getText() == "my plan":
                finished = self.tell_plan_story()

            if finished:
                selected_options.append(option_text.getText())
                # finish primary option
                option.setFill("grey")




    def tell_hometown_story(self):
        
        selected_sub_options = []
        sub_options = []  
        
        # 我热爱我的故乡rainbow ville，我在那里生活了18年，直到去其他城市上大学。
        self.display_text("I love my hometown, Rainbow Ville, where I lived for 18 years until I went to college in another city.")
        # 故乡给我留下了许多美好的记忆，无论在哪我都不会忘记。
        self.display_text("My hometown has left me with many fascinating memories that I will never forget, no matter where I am.")
        # 接下来，请更详细的了解我的故乡吧。
        self.display_text("Next, please learn more about my hometown in detail.")

        while len(selected_sub_options) < 2:
            
            option1 = self.create_option("rainbow ville", Point(400, 400), "rainbow ville" in selected_sub_options)
            option2 = self.create_option("loved ones", Point(1200, 400), "loved ones" in selected_sub_options)
            sub_options.extend([option1, option2])

            clicked_sub_option = self.get_clicked_option([option1, option2])
            if clicked_sub_option:
                self.handle_secondary_option_click(clicked_sub_option, selected_sub_options)
        
        
        for option, text in sub_options:
            option.undraw()
            text.undraw()
        
        
        return True  


    def tell_现居地_story(self):
        
        selected_sub_options = []
        sub_options = []  

        self.display_text("我热爱")
        self.display_text("故乡")
        self.display_text("接下来")

        while len(selected_sub_options) < 2:
            
            option1 = self.create_option("现居地1", Point(400, 400), "现居地1" in selected_sub_options)
            option2 = self.create_option("现居地2", Point(1200, 400), "现居地2" in selected_sub_options)
            sub_options.extend([option1, option2])

            clicked_sub_option = self.get_clicked_option([option1, option2])
            if clicked_sub_option:
                self.handle_secondary_option_click(clicked_sub_option, selected_sub_options)
        
        
        for option, text in sub_options:
            option.undraw()
            text.undraw()

        return True  
    

    def tell_plan_story(self):
        
        selected_sub_options = []
        sub_options = []  

        self.display_text("plan我热爱")
        self.display_text("故乡")
        self.display_text("接下来")

        while len(selected_sub_options) < 2:
            
            option1 = self.create_option("plan1", Point(400, 400), "plan1" in selected_sub_options)
            option2 = self.create_option("plan2", Point(1200, 400), "plan2" in selected_sub_options)
            sub_options.extend([option1, option2])

            clicked_sub_option = self.get_clicked_option([option1, option2])
            if clicked_sub_option:
                self.handle_secondary_option_click(clicked_sub_option, selected_sub_options)
        
        
        for option, text in sub_options:
            option.undraw()
            text.undraw()

        return True  
    

    

    def create_option(self, text, position, is_selected):
        
        option_color = "grey" if is_selected else macaron_white
        option = Oval(Point(position.x - 100, position.y - 50), Point(position.x + 100, position.y + 50))
        option.setFill(option_color)
        option.draw(self.win)

        option_text = Text(position, text)
        option_text.setSize(20)  
        option_text.setStyle('bold')  
        option_text.draw(self.win)


        return option, option_text
    



    def handle_secondary_option_click(self, clicked_option, selected_sub_options):
        option, option_text = clicked_option
        if option_text.getText() not in selected_sub_options:
            selected_sub_options.append(option_text.getText())
            if option_text.getText() == "rainbow ville":
                self.display_rainbow_ville_story()
            elif option_text.getText() == "loved ones":
                self.display_loved_ones_story()
            elif option_text.getText() == "现居地1":
                self.display_现居地1_story()
            elif option_text.getText() == "现居地2":
                self.display_现居地2_story()
            elif option_text.getText() == "plan1":
                self.display_plan1_story()
            elif option_text.getText() == "plan2":
                self.display_plan2_story()
            
            option.setFill("grey")
    
    

    def display_现居地1_story(self):
        self.display_text("现居地1")
        self.display_text("尽管")
        self.display_text("美丽")
        self.display_text("迷人")
        self.display_text("温暖")
        self.display_text("rainbow")


    def display_现居地2_story(self):
        
        self.display_text("现居地2")
        self.display_text("感情联结。")
        self.display_text("生活")
        self.display_text("种植，一起收获。")
        self.display_text("庆祝不同的节日和活动。")
        self.display_text("我永远爱raninbow viille的亲人和朋友，我时常思念它们。")


    def display_plan1_story(self):
        self.display_text("plan1")
        self.display_text("尽管")
        self.display_text("美丽")
        self.display_text("迷人")
        self.display_text("温暖")
        self.display_text("rainbow")


    def display_plan2_story(self):
        
        self.display_text("plan2")
        self.display_text("感情联结。")
        self.display_text("生活")
        self.display_text("种植，一起收获。")
        self.display_text("庆祝不同的节日和活动。")
        self.display_text("我永远爱raninbow viille的亲人和朋友，我时常思念它们。")


    def display_rainbow_ville_story(self):
        # rainbow ville是个特别美丽的ville。
        self.display_text("Rainbow Ville is a particularly fantastic ville.")
        # 尽管它不是繁华的大城市,但它有比urban city更美丽的风景。
        self.display_text("Although it's not a bustling big city, it has scenery even more beautiful than that of an urban city.")
        # 这里有美丽的瀑布，湖泊，溪流。
        self.display_text("Here, there are beautiful waterfalls, lakes, and streams.")
        # 这里也有迷人的山坡，草原，森林。
        self.display_text("Here, there are also charming hillsides, grasslands, and forests.")
        # 这里气候温暖，种植了不同的食物和花朵。
        self.display_text("The climate here is warm, supporting the growth of various foods and flowers.")
        # rainbow ville在我心里是最好的地方。
        self.display_text("Rainbow Ville is the best place in my heart.")


    def display_loved_ones_story(self):
        # rainbow ville有很多我爱的动物。
        self.display_text("rainbow ville有很多我爱的动物。")
        self.display_text("有我的亲人和朋友，他们都与我有深厚的感情联结。")
        self.display_text("我们一起生活，一起玩耍。")
        self.display_text("我们一起种植，一起收获。")
        self.display_text("我们互帮互助，共同庆祝不同的节日和活动。")
        self.display_text("我永远爱raninbow viille的亲人和朋友，我时常思念它们。")
    

    def display_text(self, message):
        text = Text(Point(self.win.getWidth() / 2, 50), message)
        text.setSize(20)
        text.setStyle('bold')
        text.draw(self.win)
        self.win.getMouse() 
        text.undraw()

    def invite_for_journey(self):
        # 和我一起回我的故乡吧。我需要你的帮助，我也想带你参观我的家乡
        self.display_text(f"{self.player_name}, come with me. I need your help, and I also want to take you to visit my hometown.")
        self.display_text("Before leaving, please help me dress up.")
        self.display_text("Come on, come to my cloakroom.(enter confirm after choosing)")

        self.dress_up_game()

    def dress_up_game(self):
        
        clothes_options = [
            {"color": macaron_red, "position": Point(400, 400)},
            {"color": macaron_orange, "position": Point(600, 400)},
            {"color": macaron_green, "position": Point(800, 400)},
            {"color": macaron_yellow, "position": Point(1000, 400)},
            {"color": macaron_pink, "position": Point(1200, 400)}]

        for option in clothes_options:
            self.create_clothes_option(option["color"], option["position"])

        
        self.choose_clothes(clothes_options)

    def create_clothes_option(self, color, position):
        circle = Circle(position, 50)
        circle.setFill(color)
        circle.draw(self.win)
    
    
    
    def choose_clothes(self, clothes_options):
        circles = []  
        
        for option in clothes_options:
            circle = Circle(option["position"], 50)
            circle.setFill(option["color"])
            circle.draw(self.win)
            circles.append(circle)  
        
        
        while True:
            try:
                click_point = self.win.getMouse()
                for option in clothes_options:
                    circle = Circle(option["position"], 50)
                    if self.is_point_in_circle(click_point, circle):
                        self.change_clothes_color(option["color"])
    

                
            except input(":").lower() == "confirm":
                for circle in circles:  
                        circle.undraw()
                        break  




    def change_clothes_color(self, color):
        
        self.body.setFill(color)

    def is_point_in_circle(self, point, circle):
        return (point.getX() - circle.getCenter().getX()) ** 2 + (point.getY() - circle.getCenter().getY()) ** 2 <= circle.getRadius() ** 2


 

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
    n_moves = int(input("Click different spots on the screen to move Susan. How many times do you want to move her? (bigger than 2):"))
except ValueError:
    print("Please enter a valid number.")
    
# Allow the player to move Susan n times
susan.move_n_times(n_moves)

susan.ask_player_name()
susan.ask_about_story()
susan.offer_choices()
susan.invite_for_journey()


win.getMouse()
win.close()


# dress up / 
# 
# pick things in a certain time  ()  be specific
# not too many different things
