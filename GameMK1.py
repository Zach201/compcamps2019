import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
pistol = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After what seemed to be a horrifying nightmare, you awaken in a thick, dark forest." 
  "You soon realize that you are in a lot of pain, your right arm is broken, and you have cuts and bruises all over your body." 
  "All of a sudden another man approches you, he looks like a hunter and could be a threat. You will:")
  time.sleep(1)
  print ("""  A. Scream to get the hunters attention,and ask him if he can help you
  B. Try and get up and attack the hunter
  C. Lie down in the grass and hope he doesn't spot you""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_scream()
  elif choice in answer_B:
    print ("\nYou get up off the ground, in pain you grab a stick from a tree and charge at the hunter, Out of pure fright, the hunter loads his rifle and shoots you. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_liedown()
  else:
    print (required)
    intro()

def option_scream(): 
  print ("\nThe hunter hears you calling for him, he quickly runs towards you. The hunter "
  "asks if you are ok, and if you can walk. You respond:")
  time.sleep(1)
  print ("""  A. NO YOU FOOL!!! I AM NOT OK !!! JUST LEAVE!!!
  B. No, I am not ok, but I can walk
  C. What? Who, who are you? Where am I?!?""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nYou decide that yelling at the hunter and telling him to leave is a good idea, The hunter listens to you and begins to leave  " 
    "as you watch the hunter walk away you realize that maybe you should have let him help you. With the hunter gone you realize that your time on earth is coming to an end "
    "all of a sudden the tree you are next to breaks and starts falling. You are too hurt to move so the tree crushes you. \n\nYou died! but atleast you are one with nature.")
  elif choice in answer_B:
    print ("\nYou tell the hunter that you are in a lot of pain, and you have a broken arm, The hunter offers to patch you up and take you to his camp " 
    "you accept his offer, the hunter patches you up, and the two of you begin to walk to the hunters camp.")
  elif choice in answer_C:
    option_questions()
  else:
    print (required)
    option_scream()    

def option_questions():
  print ("\nThe Hunter tells you to slow down and just listen, the hunter tells you that his name is Mitchell, he tells you that you are in a forest "
      "Mitchell tells you that he was just wandering the forest when he saw you fall right out of the sky, but he has no idea where you came from " 
      "Apparently you appeared out of thin air " "Mitchell tells you that he has an extra pistol for you. You respond:")  

def option_liedown():
  print ("\nThe hunter does not see you as you lie down in the forest, he passes by you, However, you accidentaly layed right next to a group of fire ants, they burn you alive. "
  "\n\nYou died!")