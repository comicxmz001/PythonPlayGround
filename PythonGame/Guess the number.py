# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
# initialize global variables used in your code

cmp_num = 0
msg_h = "Higher"
msg_r = "Correct!"
msg_l = "Lower"
counter_default = 8
counter = counter_default
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global cmp_num,counter
    counter = counter_default
    cmp_num = random.randint(0,100)
    print "New game. Range is from 0 to 100"
#    print cmp_num
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global cmp_num,counter
    counter = counter_default
    cmp_num = random.randint(0,1000)    
    print "New game. Range is from 0 to 1000"
    
def get_input(guess):
    # main game logic goes here	
    global counter
    counter -= 1
    if counter <= 0:
        print "Out of attempts! Please start a new game."
        print "The ture number is ", cmp_num
        return None
        
    print "Guess was", guess
    print "Number of remaining guesses is ",counter 

    if int(guess) == cmp_num:
        print msg_r
    elif int(guess) < cmp_num:
        print msg_l
    else:
        print msg_h
    
# create frame
f = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements
f.add_button("Range is [0,100]",range100,200)
f.add_button("Range is [0,1000]", range1000,200)
f.add_input("Enter a guess",get_input,200)
# start frame
print "Welcome to Guess the number!"
f.start()

# always remember to check your completed program against the grading rubric
