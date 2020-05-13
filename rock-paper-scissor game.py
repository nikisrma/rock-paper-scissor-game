#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random 

def name_to_number(name):
    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    return result

def number_to_name(number):
    if number == 0:
        result = "rock"
    elif number == 1:
        result = "Spock"
    elif number == 2:
        result = "paper"
    elif number == 3:
        result = "lizard"
    elif number == 4:
        result = "scissors"
    return result


def rpsls(player_choice): 
    print("") 
    
    print("player chooses", player_choice)
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
   
    print("computer chooses", comp_choice)
    
    if (comp_number+1) % 5 == player_number:
        print("player wins!")
    elif (comp_number+2) % 5 == player_number:
        print("player wins!")
    elif comp_number== player_number:
        print("player and computer tie!")
    else:
        print("computer wins!")
    
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


# In[ ]:




