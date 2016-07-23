# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter=0
# Define "helper" functions
def increment():
    global counter
    counter+=1
# Define event handler functions
#this example is a timer hundler
def tick():
    increment()
    print counter
def buttonpress():
    global counter
    counter = 0
    
# Create a frame
frame_test = simplegui.create_frame("A simpleGUI frame test",200,200)

# Register event handlers
timer_test = simplegui.create_timer(1000,tick)
frame_test.add_button("Click Me",buttonpress)
# Start frame and timers
frame_test.start()
timer_test.start()
