# final project: rainbow combination
# author : Huizi Cao
# combination logic are from universal combination games
# Thanks Professor Sneha for providing crucial ideas such as a timer, a click counter, random balls' drop lines."


import tkinter as tk
import random
import time


rainbow_colors = [
    "#FF6961",  # Red lv1
    "#FFB347",  # Orange lv2
    "#EBD798",  # Yellow lv3
    "#8BC68B",  # Green lv4
    "#93D3D3",  # Cyan lv5 
    "#3081fe",  # Blue lv6 
    "#DDA0DD"   # Purple lv7
]

rainbow_red = "#FF6961"
rainbow_orange = "#FFB347"
rainbow_yellow = "#ffe338"         
rainbow_green = "#8BC68B"
rainbow_cyan = "#6fd9cf"
rainbow_blue = "#4c78ae"
rainbow_purple = "#9f8cc3"

color_level = {rainbow_red: 1, rainbow_orange: 2, rainbow_yellow: 3, rainbow_green: 4, rainbow_cyan: 5, rainbow_blue: 6, rainbow_purple: 7}


class Stick:
    def __init__(self, x, balls=None):
        self.x = x
        self.balls = balls if balls is not None else []
        self.line = None

    def add_ball(self, ball):
        self.balls.append(ball)

    def remove_top_ball(self):
        return self.balls.pop() if self.balls else None

    def get_top_ball(self):
        return self.balls[-1] if self.balls else None

    def get_second_ball(self):
        return self.balls[-2] if len(self.balls) > 1 else None

    def is_full(self):
        return len(self.balls) >= 7




def create_ball(canvas, x, y, color):
    
    radius = 40
    ball = canvas.create_oval(x - 40, y - 40, x + 40, y + 40, fill=color, outline=color)
    color_level = {rainbow_red: '1', rainbow_orange: '2', rainbow_yellow: '3', rainbow_green: '4', rainbow_cyan: '5', rainbow_blue: '6', rainbow_purple: '7'}
    level = color_level[color]
    label_x = x + 30
    label_y = y + 30
    label = canvas.create_text(label_x, label_y, text=level, fill='black')
    return (ball, label)


# update sticks of current balls on it
def update_sticks():
    for stick in sticks:
        canvas.delete(stick.line)
        stick.line = canvas.create_line(stick.x, 200, stick.x, 800, fill='tan', width=10)

        y = 750
        for ball, label in stick.balls:
            if (ball, label) not in lifted_balls:
                canvas.coords(ball, stick.x - 40, y - 40, stick.x + 40, y + 40)
                canvas.coords(label, stick.x + 30, y + 30) 
                y -= 80



# lift balls from original selected stick
def lift_balls(stick_index):
    if game_over:  
        return
    stick = sticks[stick_index]
    if stick.balls:
        top_ball = stick.get_top_ball()
        second_ball = stick.get_second_ball()
        
        if second_ball and canvas.itemcget(top_ball[0], 'fill') == canvas.itemcget(second_ball[0], 'fill'):
            lifted_balls.extend([top_ball, second_ball])
            stick.balls = stick.balls[:-2]

            # Move the two-ball-group up y-100 & 60
            move_second_ball = 200 - (canvas.coords(second_ball[0])[1] + canvas.coords(second_ball[0])[3]) / 2
            move_top_ball = 160 - (canvas.coords(top_ball[0])[1] + canvas.coords(top_ball[0])[3]) / 2
            canvas.move(second_ball[0], 0, move_second_ball)
            canvas.move(second_ball[1], 0, move_second_ball)  
            canvas.move(top_ball[0], 0, move_top_ball)
            canvas.move(top_ball[1], 0, move_top_ball)  
        else:
            lifted_balls.append(top_ball)
            stick.remove_top_ball()

            # Move the single ball up y-100
            move_y = 160 - (canvas.coords(top_ball[0])[1] + canvas.coords(top_ball[0])[3]) / 2
            canvas.move(top_ball[0], 0, move_y)
            canvas.move(top_ball[1], 0, move_y)  

        update_sticks()





# drop balls lifted onto new selected stick
def drop_balls(stick_index):
    global game_over
    stick = sticks[stick_index]

    
    if stick.is_full():
        end_game()
        return

    # check for merge
    can_merge = False
    if len(stick.balls) + len(lifted_balls) >= 7:
        new_ball_color = canvas.itemcget(lifted_balls[0][0], 'fill')
        top_ball_color = canvas.itemcget(stick.get_top_ball()[0], 'fill') if stick.balls else None
        second_ball_color = canvas.itemcget(stick.get_second_ball()[0], 'fill') if len(stick.balls) > 1 else None

        # check whether can  merge
        can_merge = new_ball_color == top_ball_color or new_ball_color == second_ball_color

    
    if len(stick.balls) + len(lifted_balls) > 7 and not can_merge:
        end_game()
        return

    
    for ball, label in lifted_balls:
        stick.add_ball((ball, label))

    merge_balls(stick)
    lifted_balls.clear()
    update_sticks()






# merge balls for 3or4 continuous same color balls 
def merge_balls(stick):
    global score, score_label  
    colors = [rainbow_red, rainbow_orange, rainbow_yellow, rainbow_green, rainbow_cyan, rainbow_blue, rainbow_purple]

    while True:
        for i in range(len(stick.balls) - 2):
            color = canvas.itemcget(stick.balls[i][0], 'fill')
            if all(canvas.itemcget(stick.balls[j][0], 'fill') == color for j in range(i, i + 3)):
                remove_count = 4 if i < len(stick.balls) - 3 and canvas.itemcget(stick.balls[i + 3][0], 'fill') == color else 3
                # purple would gain score instead of becoming new color
                if color == rainbow_purple:  
                    for _ in range(remove_count):
                        # remove ball
                        canvas.delete(stick.balls[i][0])  
                        # remove label
                        canvas.delete(stick.balls[i][1])  
                        stick.balls.pop(i)
                    # gain score for purple group
                    score += 20  
                    # update total score
                    update_score_label()  
            
                else:
                    # remove balls and labels
                    for _ in range(remove_count):
                        canvas.delete(stick.balls[i][0])
                        canvas.delete(stick.balls[i][1])
                        stick.balls.pop(i)

                    # generate new color ball
                    new_color = colors[(colors.index(color) + 1) % len(colors)]
                    new_ball = create_ball(canvas, stick.x, 0, new_color)
                    stick.balls.insert(i, new_ball)
                break
        else:
            break


# update the score label temporally
def update_score_label():
    
    global score_label
    canvas.itemconfig(score_label, text=f"Score: {score}")


# get highest level of current balls
def get_highest_level():
    color_level = {rainbow_red: 1, rainbow_orange: 2, rainbow_yellow: 3, rainbow_green: 4, rainbow_cyan: 5, rainbow_blue: 6, rainbow_purple: 7}
    highest_level = 1
    for stick in sticks:
        for ball, _ in stick.balls:
            ball_color = canvas.itemcget(ball, 'fill')
            highest_level = max(highest_level, color_level[ball_color])
    return highest_level



# generate a random ball color not higher than current highest level
def generate_random_ball(level):
    
    colors = [rainbow_red, rainbow_orange, rainbow_yellow, rainbow_green, rainbow_cyan, rainbow_blue, rainbow_purple]
    return random.choice(colors[:level])


# show next falling balls for all sticks
def show_next_balls():
    global countdown_label

    for i, stick in enumerate(sticks):
        level = get_highest_level()
        color = generate_random_ball(level)
        incoming_balls[i] = create_ball(canvas, stick.x, 50, color)

    countdown_label = canvas.create_text(740, 880, text="5", fill="black", font=("Times New Roman", 20))
    update_countdown(5) 


def update_countdown(time_left):
    if time_left > 0:
        canvas.itemconfig(countdown_label, text=str(time_left))
        root.after(1000, lambda: update_countdown(time_left - 1))  
    else:
        canvas.itemconfig(countdown_label, text="")  
        drop_new_balls()  



# drop new balls to sticks, check whether it can be merged
def drop_new_balls():
    global game_over
    for i, stick in enumerate(sticks):
        if incoming_balls[i] is not None:
            ball, label = incoming_balls[i]

            if stick.is_full():
                top_ball_color = canvas.itemcget(stick.get_top_ball()[0], 'fill')
                second_ball_color = canvas.itemcget(stick.get_second_ball()[0], 'fill') if len(stick.balls) > 1 else None
                new_ball_color = canvas.itemcget(ball, 'fill')

                # check for merge
                if new_ball_color != top_ball_color or top_ball_color != second_ball_color:
                    end_game()
                    return

            stick.add_ball((ball, label))
            merge_balls(stick)
            incoming_balls[i] = None
    
    canvas.itemconfig(countdown_label, text="")
    update_sticks()
    canvas.update()

    


# click counter for random balls' drop
clicks_left = 8
click_counter_label = None

def update_click_counter():
    global clicks_left, click_counter_label
    clicks_left = clicks_left - 1 if clicks_left > 1 else 8
    canvas.itemconfig(click_counter_label, text=f"Clicks left: {clicks_left}")


# check and operate clicks on canvas
def click_on_canvas(event):
    global move_count, game_over

    
    if game_over:  
        return

    clicked_stick = None
    for i, stick in enumerate(sticks):
        if abs(event.x - stick.x) < 20:  
            clicked_stick = i
            break

    if clicked_stick is not None:

        update_click_counter()

        if lifted_balls:
            drop_balls(clicked_stick)  
        else:
            lift_balls(clicked_stick)  

        
        move_count += 1
        
        if move_count == 8:  
            move_count = 0
            show_next_balls()
            root.after(5000, drop_new_balls)

  

# end with final score
def end_game():
    
    global game_over
    game_over = True
    canvas.create_text(400, 400, text="Game Over", fill="red", font=("Times New Roman", 40))
    canvas.create_text(400, 450, text=f"Final Score: {score}", fill="black", font=("Times New Roman", 20))
    restart_button.place(x=350, y=500)


# restart
def restart_game():
    global game_over, score, sticks, lifted_balls, incoming_balls, move_count, score_label
    game_over = False
    score = 0
    canvas.delete("all")  

    sticks = [Stick(100 + i * 120, [create_ball(canvas, 100 + i * 120, 750, rainbow_red), create_ball(canvas, 100 + i * 120, 620, rainbow_red)]) for i in range(6)]
    lifted_balls = []
    incoming_balls = [None] * 6
    move_count = 0

    update_sticks()
    score_label = canvas.create_text(400, 880, text=f"Score: {score}", fill="black", font=("Times New Roman", 20))
    restart_button.place_forget()



def show_start_message():
    return canvas.create_text(400, 420,
        text=("Welcome to rainbow combination\n\n"
              "Merge Rules and Scoring:\n"
              "This is a merging game with balls of seven rainbow colors. Three or four balls of the same color "
              "can be merged into a ball of the next level. The highest level ball will disappear when merged, "
              "and the player scores 20 points.\n\n"
              "Player's Control:\n"
              "The player can click on a stick. The first click will lift the top ball on the clicked stick. "
              "Clicking on any stick again (the second click) will place the lifted ball onto that stick. "
              "Each time the lifted ball is the top ball on the stick, and if the top two are the same color, both will be lifted.\n\n"
              "Other Game Mechanics Related to Player Actions:\n"
              "After every four moves by the player (equivalent to 8 stick clicks), the system will randomly drop balls from the top. "
              "Each stick gets one ball, and the level of the ball is random but no higher than the current highest level. "
              "Before dropping, the upcoming balls are shown for 5 seconds, during which the player can continue to play "
              "and see the colors of the impending balls.\n\n"
              "Game Over Rules:\n"
              "Each stick can have up to seven balls. Attempting to place an eighth ball will cause all balls to collapse, "
              "ending the game and displaying the final score.\n\n"
              "Click to start"),
        fill="black", font=("Times New Roman", 15), width=700)


def start_game():
    canvas.delete(start_message)  
    start_button.place_forget() 
    initialize_game() 



def initialize_game():
    global sticks, lifted_balls, incoming_balls, move_count, score_label, game_over, score, clicks_left, click_counter_label,countdown_label

    game_over = False
    score = 0
    canvas.delete("all")  

    sticks = [Stick(100 + i * 120, [create_ball(canvas, 100 + i * 120, 750, rainbow_red), create_ball(canvas, 100 + i * 120, 620, rainbow_red)]) for i in range(6)]
    lifted_balls = []
    incoming_balls = [None] * 6
    move_count = 0

    update_sticks()
    score_label = canvas.create_text(400, 880, text=f"Score: {score}", fill="black", font=("Times New Roman", 20))

    clicks_left = 8
    click_counter_label = canvas.create_text(100, 880, text=f"Clicks left: {clicks_left}", fill="black", font=("Times New Roman", 20))
    
    # the line for random generation balls
    line_r = 50  
    canvas.create_line(0, line_r, canvas.winfo_width(), line_r, fill='tan')

    countdown_label = canvas.create_text(690, 880, text="Time left:", fill="black", font=("Times New Roman", 20))

    canvas.bind("<Button-1>", click_on_canvas)


def end_game():
    global game_over
    game_over = True
    canvas.create_text(400, 500, text="Game Over", fill="red", font=("Times New Roman", 40))
    canvas.create_text(400, 550, text=f"Final Score: {score}", fill="black", font=("Times New Roman", 20))
    restart_button.place(x=350, y=600)



click_counter_label = None
countdown_label = None

root = tk.Tk()
root.title("Rainbow Combination")
canvas = tk.Canvas(root, width=800, height=900, bg='#FFEDC3')
canvas.pack()

start_message = show_start_message()

start_button = tk.Button(root, text="Start", command=start_game)
start_button.place(x=350, y=650)

canvas.tag_bind(start_message, "<Button-1>", start_game)

restart_button = tk.Button(root, text="Restart", command=restart_game)

root.mainloop()