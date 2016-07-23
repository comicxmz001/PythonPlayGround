#a timer programme

import simplegui

#define a handler
def tick():
    print "tick"

#register handler

timer2 = simplegui.create_timer(100,tick)
timer2.start()
print timer2.is_running()


#write handler
#then register the handler
#finally run the functions