init python:
    import time

    hintUsed = False

    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        renpy.say(" ", ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec))))



# add color to characters later
define company = Character("Odyssey7")

define s1 = Character("Scientist 1")
define s2 = Character("Scientist 2")
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
    label testButton:
        scene bg blackScreen
        call screen testImgButton
        "Currently in testing label"
        show screen testImgButton
        "testing done"
        hide screen testImgButton
    
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
        mc "Wait, I should read this more carefully."
        # what email says
        company ""

    label facility:
        scene bg facilityEntrance
        s "Hello there! I see you have received our email about a new alpha test. Our game has breakthrough artificial intelligence and virtual reality technology, that we're excited for you to experience it!"

        scene bg mainFacility
        with fade

        s "Before we begin your experience, please measure and record your heart rate."

        



        




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

        show jeremy default at right

        a "Hey! I’ve never seen you before, what's your name?"

        mc "I'm [name]"

        a "Oh, hi [name]! Welcome to our village! I’m Audrey. This guy is my best friend."

        show jeremy wideSmile at right

        j "Nice to meet you, [name]!"

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
        with vpunch
        with hpunch
        



        "..."
        "This is the end of the game."
        $ end_time = time.time()
        $ time_lapsed = end_time - start_time
        $ time_convert(time_lapsed)
        
        "Test"


    return