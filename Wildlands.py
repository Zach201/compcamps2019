import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
sniper = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After what seemed to be a horrifying nightmare, you awaken in a thick, dark forest." 
  "You soon realize that you are in a lot of pain, your right arm is broken, and you have cuts and bruises all over your body." 
  "All of a sudden you spot a man walking through the forest, he looks like a hunter and could be a threat. You will:")
  time.sleep(1)
  print ("""  A. Scream to get the hunters attention,and ask him if he can help you
  B. Get up and attack the hunter
  C. Lie down in the grass and hope he doesn't spot you""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_help()
  elif choice in answer_B:
    print ("\nYou get up off the ground in pain and you grab a stick from a nearby tree and charge at the hunter, Out of pure fright the hunter loads his rifle and shoots you! "
    "\n\nYou died!")
  elif choice in answer_C:
    option_liedown()
  else:
    print (required)
    intro()

def option_help(): 
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
    option_help()

def option_questions():
  print ("\nThe Hunter tells you to slow down and just listen, the hunter tells you that his name is Mitchell, he tells you that you are in a forest "
      "and that he was just wandering the forest when he saw you fall right out of the sky, but he has no idea where you came from " 
      "Apparently you appeared out of thin air " "Mitchell tells you that he has an extra sniper and that you should take it " "Say YES to take the sniper")
  choice = input(">>> ")
  if choice in yes:
    sniper = 1 #adds a sniper
  else:
    sniper = 0
  print ("\nYou take the sniper and Mitchell says that you should maybe take some practice shots to test your aim. "
       "However, you only have 6 rounds left, so you might want to save them for later. You decide it's best if you:")
  time.sleep(1)
  print ("""  A. Shoot Mitchell with the sniper and take his gear
  B. Skip the practice because you only have 6 rounds and you don't want to waste them.
  C. Take some practice shots so that you are familiar with how to properly shoot the sniper""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nYou decide to shoot Mitchell, as you aim the sniper at Mitchell ready to shoot him, "
    "you realize you have no idea how to use a gun and you miss by a mile. Mitchell realizes you tried to shoot him, so he grabs his sniper and shoots you "
    "Well then, maybe that gun practice would have been helpful after all.\n\nYou died!")
  elif choice in answer_B:
   if sniper > 0:
    print ("\nYou skip the sniper practice because you don't want to waste any ammo "
    "Mitchell says that you should come with him to his camp. "
    "You agree with Mitchell and the two of you head off to his camp "
    "You aren't sure if you should fully trust Mitchell "
    "But he's been trustworthy so far.")
   else: #If the user didn't take the sniper
     print ("\nYou should have picked up that sniper. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As you hold the sniper, you load it with 3 bullets, "
    "as you go to shoot at the target on a nearby tree, you spot a bear to your right. You're several feet away from the bear, and it does not see you. "
    "You decide to:")
    time.sleep(1)
    print (""" A. Shoot at the target on the tree
    B. Shoot at the bear and try to kill it""")
    choice = input(">>> ")
    if choice in answer_A:
        print ("\nYou load the sniper, aim down sight, and shoot at the target. BULLSEYE!")
    elif choice in answer_B:
     print ("You load the sniper, aim down sight, the bear is right in the middle of your crosshair. "
            "You pull the trigger. the bullet hits the bear but the bear seems to not care!"
            "The bear comes running at you and before you can reload your gun, the bear jumps on you and begins to eat you!\n\nYou died!")
    option_liedown()
  else:
    print (required)
    option_questions()

def option_liedown():
  print ("\nYou stay hidden within the bushes and trees of the forest, " "Moments later you hear the hunter asking you to come out of hiding, "
      "You think it's safe to come out but then you hear the hunter load his gun and start laughing "
  "You need to make a decision! Will you:")
  time.sleep(1)
  print ("""  A. Stay hidden and hope he doesn't spot you
  B. Try to sneak behind the hunter and knock him out
  C. Get up and charge the hunter head on and try to kill him""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted by the hunter "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou sneak through the bushes and get right behind the hunter "
    "You see a rock the size of a football on the ground " "You take the rock and slam it against the hunters head! " 
    "You knocked the hunter out!")
  elif choice in answer_C:
      print ("You grab a stick from the ground and attack the hunter! "
      "He sees you running at him with a stick, confused he hesitates for a second giving you a chance to take his gun and shoot him "
      "However, you think it's a better idea to use your stick... " "The hunter simply aims at you, pulls the trigger and kills you...\n\nYou died!")
  else:
    print (required)
    option_liedown()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the orc to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending orc.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the orc. It does! The orc was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the flower
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

intro()