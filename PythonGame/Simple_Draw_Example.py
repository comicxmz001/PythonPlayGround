#This is a simple calculator without using canvas...

import simplegui
    
def draw(canvas):
    #This is a canvas handler
    canvas.draw_text("Hello!",[70,100],24,"Red")
    #Left
    canvas.draw_line([55,70],[55,110],2,"Yellow")
    #Right
    canvas.draw_line([140,70],[140,110],2,"Yellow")
    #Up
    canvas.draw_line([55,70],[140,70],2,"Yellow")
    #Down
    canvas.draw_line([55,110],[140,110],2,"Yellow")
    
#create frame
f = simplegui.create_frame("Simple Draw Example",200,250)

#register canvas
f.set_draw_handler(draw)
#frame start
f.start()




