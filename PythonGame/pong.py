# Implementation of classic arcade game Pong

import simplegui
import random
import math
# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [-1,-0.1] 
time = 0
score1 = 0
score2 = 0
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init():
    global ball_pos, ball_vel,time # these are vectors stored as lists
    time = 0
    if random.randint(0,1): # 1 -> leftwards
        ball_vel[0] = -random.randrange(1,30)/10
    else:
        ball_vel[0] = random.randrange(1,30)/10
    ball_vel[1] = -math.fabs(ball_vel[0]) #randomed init speed
    ball_pos = [WIDTH/2,HEIGHT/2]
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    timer.start()
# define event handlers
def tick():
    global time
    time = time + 1
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,time  # these are floats
    global score1, score2  # these are ints
    time = 0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    ball_init()
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos= paddle1_pos + paddle1_vel
    paddle2_pos= paddle2_pos + paddle2_vel
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #left paddles
    c.draw_polygon([(0,paddle1_pos),(0,paddle1_pos+PAD_HEIGHT),(PAD_WIDTH,paddle1_pos+PAD_HEIGHT),(PAD_WIDTH,paddle1_pos),(0,paddle1_pos)],1,"White","White") 
    #right paddles
    c.draw_polygon([(WIDTH-1-PAD_WIDTH,paddle2_pos),(WIDTH-1-PAD_WIDTH,paddle2_pos+PAD_HEIGHT),(WIDTH-1,paddle2_pos+PAD_HEIGHT),(WIDTH-1,paddle2_pos),(WIDTH-1-PAD_WIDTH,paddle2_pos)],1,"White","White") 
    # update ball,
    ball_pos[0]= ball_pos[0] + time * ball_vel[0] #x
    ball_pos[1]= ball_pos[1] + time * ball_vel[1] #y
    
    # collision detection
    #left collision detected
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ball_pos[1] <= paddle1_pos+ PAD_HEIGHT and ball_pos[1] >= paddle1_pos:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        #left fail
        score2 = score2 + 1
        timer.stop()
        ball_init()
    #right collision detected
    elif ball_pos[0] >= WIDTH-1-BALL_RADIUS-PAD_WIDTH and ball_pos[1] <= paddle2_pos+ PAD_HEIGHT and ball_pos[1] >= paddle2_pos:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] >= WIDTH-1-BALL_RADIUS-PAD_WIDTH:
        #right fail
        score1 = score1 +1
        timer.stop()
        ball_init()
    #up collision detected
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    #bottom collision detected
    elif ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # draw ball and  scores
    c.draw_circle(ball_pos,BALL_RADIUS,1,"Maroon","Yellow")
    c.draw_text("Player 1: ", [20,20],24,"Lime")
    c.draw_text(str(score1),[110,20],24,"Lime")
    c.draw_text("Player 2: ", [WIDTH -1 - 150,20],24,"Lime")
    c.draw_text(str(score2),[WIDTH -1 - 60,20],24,"Lime")
def keydown(key):
    global paddle1_vel, paddle2_vel
    # W&S for Player1, up&down for Player2, 
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["W"]:
        if paddle1_vel > 0:
            paddle1_vel = 0
        else:
            paddle1_vel += -1
        
    elif key == simplegui.KEY_MAP["s"] or key == simplegui.KEY_MAP["S"]:
        if paddle1_vel < 0:
            paddle1_vel = 0
        else:
            paddle1_vel += 1
        
    elif key == simplegui.KEY_MAP["up"]:
        if paddle2_vel > 0:
            paddle2_vel = 0
        else:
            paddle2_vel += -1
        
    elif key == simplegui.KEY_MAP["down"]:
        if paddle2_vel < 0:
            paddle2_vel = 0
        else:
            paddle2_vel += 1
        
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,100)
timer = simplegui.create_timer(1000,tick)
# start frame
frame.start()
timer.start()
