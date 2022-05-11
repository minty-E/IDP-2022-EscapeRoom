# add color to characters later
define company = Character("Odyssey7")

define j = Character("Jeremy")
define a = Character("Audrey")
define mc = Character("[name]")
define vc = Character("Village Chief")
define hinter = Character("Puzzle Master")
define vt = Character("Voice in the Tower")

# audrey photos
image audrey default = "/audrey/audreyDefault.png"
image audrey confused = "/audrey/audreyConfused.png"
image audrey evil = "/audrey/audreyEvilLaugh.png"
image audrey happy = "/audrey/audreyHappy.png"
image audrey mad = "/audrey/audreyMad.png"

# jeremy photos
image jeremy default = "/jeremy/jeremyDefault.png"
image jeremy confused = "/jeremy/jeremyConfused.png"
image jeremy smile = "/jeremy/jeremyOpenSmile.png"
image jeremy wideSmile = "/jeremy/jeremyToothySmile.png"

# village chief photos, CHECK IF WORKING
image chief happy = "/villageChief/chiefHappy.png"
image chief scrunched = "/villageChief/chiefScrunched.png"

# guard
image guard default = "/guard/guardDefault.png"

# backgrounds
image bg bedroom = "/backgrounds/bedroom.png"
image bg blackScreen = "/backgrounds/blackScreen.png"
# The game starts here.

label settings:
        scene bg blackScreen
        "...Hm. There isn't anything on here."
        jump startOrSettings



label start:
    
    
    scene bg blackScreen
    
    $ name = renpy.input("What is your name?")
    $ name = name.strip()


    scene bg bedroom

    label startOrSettings:
        scene bg titleScreen
        "What should I press?"
    menu: 
        "Play":
            jump play

        "Settings":
            jump settings


    label play:
        scene bg cave
        with fade
        # entering the game

        "Huh..? Where am I?"
        "It's so dark..."
        "Wait, I see a light! I should head to it."

        # exits cave
        #scene bg outsideOfCave

        # introduction to jeremy and audrey
        #scene bg berries

        "Huh, are those people? They must be the new AI characters that Odyssey said they made. I should go up to them!"
        "..."

        mc "Hey, you two! Hey!"

        scene bg berriesWithout

        # talk to jeremy and audrey

        show audrey evil at left
        #show jeremy default at right

        show jeremy wideSmile at right

        a "Hello there!"

        j "Hi!"

        a "We'll take you to our Village Chief."

        scene bg village

        show chief happy 

        vc "insert dialogue"

        # insert line to line dialogue of conversation

        # move to tree

        scene bg treeNormal

        # tour

        scene bg village

        # more dialogue to return to the tree

        scene bg treeNormal

        # outsider touches tree

        scene bg treeRed

        # dialogue about tree

        scene bg hole

        # special effects rumbling
        

    #show Odyssey7 default at center 

    #company "Dear valued customer, \n You have been selected to be an alpha tester of our brand new game! We have spent the last ___ years developing this exciting new open world fantasy adventure game!"



    

    return
