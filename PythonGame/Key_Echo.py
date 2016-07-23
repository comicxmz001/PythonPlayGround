# This is a keyboard echo programme

import simplegui

#global vars
current_key = " "
#def 
def key_down(key):
    global current_key
    current_key = chr(key)

def key_up(key):
    global current_key
    current_key = " "

def draw(canvas):
    canvas.draw_text(current_key,[10,25],24,"Yellow")
#create frame

frame = simplegui.create_frame("Keyboard echo",35,35)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
#start frame
frame.start()