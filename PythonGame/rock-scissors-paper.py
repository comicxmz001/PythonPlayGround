# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors" to numbers
# as follows:
#
# 0 - rock
# 1 - scissors
# 2 - paper

# helper functions
import random

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "scissors"
    elif number == 2:
        name = "paper"
    else :
        print "No such choice!"
        name = None
    return name
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        number = 0
    elif name == "scissors":
        number = 1
    elif name == "paper":
        number = 2
    else:
        print "No such choice!"
    return number

def rps(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results
    player_choice = name
    player_choice_num = name_to_number(name)
    print "Player choose "	,	player_choice,	"." 
    
    cmp_choice_num = random.randint(0, 2)
    cmp_choice = number_to_name(cmp_choice_num)
    print "Computer choose"	,	cmp_choice,		"."

    difference = player_choice_num - cmp_choice_num
    #equals
    if difference == 0: 
        print "The two sies draw!"
    
    #player wins
    elif difference == -1 or difference == 2:
        print "Player wins!"
    else:
        print "Computer wins!"
    	return None
# test your code
rps("rock")
rps("paper")
rps("scissors")

# always remember to check your completed program against the grading rubric
