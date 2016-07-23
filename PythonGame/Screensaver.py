# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
msg = "Python is niubility!"
weight = 500
height = 500
position = [50,50]

# Handler for text box
def get_input(var):
    global msg
    msg = var
    
# Handler for timer
def tick():
    global position
    position[0] = random.randrange(0,weight)
    position[1] = random.randrange (0,height)

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(msg,position,40,"Red")
    
# Create a frame 
frame = simplegui.create_frame("Screensaver",weight,height)
timer = simplegui.create_timer(1000,tick)
frame.set_draw_handler(draw)
# Register event handlers
frame.add_input("New words:",get_input,200)

# Start the frame animation
frame.start()
timer.start()