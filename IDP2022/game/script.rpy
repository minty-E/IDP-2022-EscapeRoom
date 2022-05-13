init python:
    import time

    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        renpy.say(mc, ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec))))



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
#image bg bedroom = "/backgrounds/bedroom.png"
image bg blackScreen = "/backgrounds/blackScreen.png"
image bg cave = "/backgrounds/cave.png"
image bg bedroom = "/backgrounds/BedRoom2.png"

# image ralsei default = "ralsei.jpeg"
# The game starts here.



label settings:
        scene bg blackScreen
        "...Hm. There isn't anything on here."
        jump startOrSettings





label start:
    
    
    scene bg blackScreen
    
    $ name = renpy.input("What is your name?")
    $ name = name.strip()
    $ start_time = time.time()


    scene bg bedroom

    "..."
    mc "Huh, I wonder who sent me an email this late at night."
    menu: 
        "Open the email":
            jump emailScene


    label emailScene:
        mc "Oh wait..."
        #scene bg email
        scene bg bedroom
        with vpunch
        mc "Odyssey7 sent me this?! No way, I love their games!"
        mc "I have to test this out now, I need a break from all the work I'm doing anyways."


    "..."

    scene bg titleScreen
    "Huh, the title screen is kind of bare. There's only Start and Settings."

    label startOrSettings:
        scene bg titleScreen
        "What should I press?"
    menu: 
        "Play":
            jump play

        "Settings":
            jump settings


    label play:
        "Whatever, doesn't matter if the appearance is lacking. I just want to play the game!"

        scene bg blackScreen
        $ renpy.pause(delay = 2, hard = True)

        scene bg cave
        with fade
        # entering the game

        "Huh..? Where am I?"
        "It's so dark..."
        "Wait, I see a light! Am I in a cave?"
        "I should head to it."

        # exits cave
        #scene bg outsideOfCave

        "Oh wow! The world is so detailed!"

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

        #call screen ralsei default

        

        # tour

        scene bg village

        # more dialogue to return to the tree

        scene bg treeNormal

        # outsider touches tree

        scene bg treeRed

        # dialogue about tree

        scene bg hole

        # special effects rumbling

        "..."
        "This is the end of the game."
        $ end_time = time.time()
        $ time_lapsed = end_time - start_time
        $ time_convert(time_lapsed)
        
        "Test"
    
    return
