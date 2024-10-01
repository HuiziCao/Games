from graphics import *
import time

# Create a window
win = GraphWin("Susan's Journey", 800, 800)

# Draw Susan
susan = Circle(Point(400, 700), 30)
susan.setFill("white")
susan.draw(win)

# Draw Lucinda
lucinda = Circle(Point(500, 700), 30)
lucinda.setFill("gray")
lucinda.draw(win)

# Draw Bee
bee = Circle(Point(400, 100), 10)
bee.setFill("yellow")
bee.draw(win)

# Draw Apple
apple = Circle(Point(300, 700), 20)
apple.setFill("red")
apple.draw(win)

# Draw Lucinda's Garden
garden = Rectangle(Point(100, 600), Point(200, 500))
garden.setFill("green")
garden.draw(win)

# Susan and Lucinda approach the bees
for i in range(10):
    susan.move(0, -10)
    lucinda.move(0, -10)
    time.sleep(0.1)

# Dialogue 1
dialogue1 = Text(Point(win.getWidth() / 2, 20), "Lucinda, can you help me get some honey?")
dialogue1.draw(win)
time.sleep(2)
dialogue1.setText("Of course, Susan! Let's ask the bees to share some with us.")
time.sleep(2)
dialogue1.undraw()

# Susan and Lucinda dialogue with the bee
dialogue2 = Text(Point(win.getWidth() / 2, 20), "Hello bees, may we have some honey?")
dialogue2.draw(win)
time.sleep(2)
dialogue2.setText("We don't need apples, but we would love to visit Lucinda's garden!")
time.sleep(2)
dialogue2.undraw()

# Susan convinces Lucinda
dialogue3 = Text(Point(win.getWidth() / 2, 20), "They will make your flowers more beautiful.")
dialogue3.draw(win)
time.sleep(2)
dialogue3.setText("Okay, bees can visit my garden!")
time.sleep(2)
dialogue3.undraw()

# Bee moves to the garden
for i in range(20):
    bee.move(-5, 5)
    time.sleep(0.1)

# Bee 'collects honey' (animation skipped for brevity)

# Bee returns with honey
for i in range(20):
    bee.move(5, -5)
    time.sleep(0.1)

# Final dialogue
dialogue4 = Text(Point(win.getWidth() / 2, 20), "Thank you, Lucinda! Here is some fresh honey for you.")
dialogue4.draw(win)
time.sleep(2)
dialogue4.undraw()

# Pause for final view
win.getMouse()  # Pause for click in window

# Close the window
win.close()
