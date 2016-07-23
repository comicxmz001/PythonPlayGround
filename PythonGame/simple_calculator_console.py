#This is a simple calculator without using canvas...

import simplegui

#define global vars: two operands

oprand = 0
store = 0
#define calculator functions
#define handler
def output(): 	#show results in consoles
    print "Store is", store
    print "Operand is", oprand
    
def swap(): 		#swap
    global oprand,store
    oprand,store = store,oprand
    output()
def add():		#add
    global store
    store+= oprand
    output()
    
def minus():
    global store
    store-=oprand
    output()
def mult():
    global store
    store*=oprand
    output()
def div():
    global store
    store/=oprand
    output()
    
def enter(num): #enter new oprand
    global oprand
    #text input gets string as default, need force covert
    oprand=int(num) 
    output()
    
#create frame
f = simplegui.create_frame("Simple Calculator",200,300)

#register button handlers
f.add_button("=",output,50)
f.add_button("+",add,50)
f.add_button("-",minus,50)
f.add_button("x",mult,50)
f.add_button("/",div,50)
f.add_button("<=>",swap,50)

#register text input handler
f.add_input("Enter",enter,50)

#frame start
f.start()





