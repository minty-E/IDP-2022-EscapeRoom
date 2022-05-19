init python:
    import time

    hintUsed = 0

    def time_convert(sec):
        sec += (hintUsed * 10)
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
define hacker = Character("Mysterious Hacker")

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

label addTime:
    hintUsed++


label start:
    label testButton:
        scene bg blackScreen
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
        company "filler here"

    label facility:
        scene bg facilityEntrance
        s "Hello there! I see you have received our email about a new alpha test. Our game has breakthrough artificial intelligence and virtual reality technology, that we're excited for you to experience it!"

        scene bg mainFacility
        with fade

        s "Before we begin your experience, please measure and record your heart rate."

        # HOOKED TO VR


    "..."


    label introAct:
        

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


    # act 1
    label act1:
        "..."
        "Where am I...?"

        # fade in background or simulate looking around

        scene bg dungeon
        with fade()

        "..."
        "ALERT: YOU HAVE BEEN TRAPPED IN A GAME, WE ARE WORKING TO FREE YOU."
        with vpunch
        

        label puzzle1: 
            hacker "filler, either give instructions here or"
            "have the mc figure it out themselves"

            # enter or implement dragging code 

            # hanoi puzzle IMPORTANT

            # drag and drop pieces of mirror, get artist to do this

        # death of jeremy and audrey leaves

        # get ingredient

        # contact by company, move to cave

    


    label act2:
        "..."
        # arrive in cave

        "Hm, the cave is blocked."

        label puzzle2:
            # torch puzzle, clicking image buttons to change orientation

            # move to memorial where npc guard instructs to solve puzzles

            # recreate a piano melody

            # find correct part of statue and drag and drop on it

            

        # receive 2nd ingredient

    label act3: 
        # enter tower

        # voice in tower calls out to pass trial 

        # each task will form more stairs

        label puzzle3:
            # make a light purple, code different color combinations, drag and drop

            # shuffle different letters to form words

            # slide on image, maze puzzle

        # arrive at top of tower

    label ending: 
        # audrey shows up hacked
        # hacker sends spells through audrey, quick time events to stop
        # health bar will lower if user fails 
        # company sends spell book to kill audrey
        # mixes three ingredients to cure the tree
        # curing tree leads to exiting the game
        # hacker gets arrested and user gets sent home



    "..."
    "This is the end of the game."
    $ end_time = time.time()
    $ time_lapsed = end_time - start_time
    $ time_convert(time_lapsed)
        
        "Test"


    return