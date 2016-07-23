#still have not add bug report for time over 59:59.0
# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables

interval = 100
canvas_w = 300
canvas_h = 200
current_time = 0
stop_counter = 0
started = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    if current_time%600/10 < 10:
       return str(int(current_time/600))+":0"+str(int(current_time%600/10))+"."+str(int(current_time%10)) 
    else:
        return str(int(current_time/600))+":"+str(int(current_time%600/10))+"."+str(int(current_time%10))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def sw_start():
    global started
    timer.start()    
    started = True
    
def sw_stop():
    global started,stop_counter
    timer.stop()
    if started:    
        stop_counter+= 1
    started = False
    print started
def sw_reset():
    global current_time,stop_counter
    if not started:
        current_time = 0
        stop_counter = 0   
    
# define event handler for timer with 0.1 sec interval
def tick():
    global current_time
    current_time+= 1 #increase 0,1sec
    print current_time

# define draw handler
def draw(canvas):
    canvas.draw_text(format(),[100,100],40,"White")
    canvas.draw_text(str(stop_counter)+"/"+str(stop_counter),[250,30],30,"Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch",canvas_w,canvas_h)
frame.add_button("Start",sw_start,100)
frame.add_button("Stop",sw_stop,100)
frame.add_button("Reset",sw_reset,100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval,tick)
# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric
