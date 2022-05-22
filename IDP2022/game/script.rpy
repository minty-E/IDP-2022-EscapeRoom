init python:
    import time

    hintUsed = 0

    def time_convert(sec):
        #sec += (hintUsed * 10)
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        renpy.say(" ", ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec))))



# add color to characters later
define company = Character("Email")
define s1 = Character("Scientist 1", color = "#808080")
define s2 = Character("Scientist 2", color = "#808080")
define j = Character("Jeremy")
define a = Character("Audrey")
define mc = Character("[name]")
define vc = Character("Village Chief")
define hinter = Character("Puzzle Master")
define vt = Character("Voice in the Tower")
define hacker = Character("Mysterious Hacker")
define g = Character("Guard")
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

image bg blackScreen = "/backgrounds/blackScreen.png"
image bg cave = "/backgrounds/StartCaveBackground.png"
image bg bedroom = "/backgrounds/BedRoom.png"
image bg facility = "/backgrounds/Facility.png"

# image ralsei default = "ralsei.jpeg"
# The game starts here.

# label addTime:
#    hintUsed++


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
        mc "Odyssey7 sent me this?!{w} No way, I love their games!"
        # what email says
        company "Hello!{w} Odyssey7 would like to invite you to the facility where we make our games. We have just developed a new VR game, but we would like you to beta-test it. Please see the link to the address below.{w} See you soon,{w} \nOdyssey7"

    label facility:
        scene bg facility
        s1 "Hello there [name]! I see you received our email about testing our new game."
        mc "Of course. It would be a shame if I pass up such a good opportunity."
        s1 "I’m glad to hear that!{w} Now, enough said, let’s get you into the game. Follow me!"

        scene bg facility
        with fade

        s1 "Before we begin your experience, please measure and record your heart rate."
        $ hRate = renpy.input("Enter heart rate and press enter: ")
        $ hRate = hRate.strip()

        #s2 helps with vr headset

        s2 "...{w} Alright, you’re all set. Just remember that the game is still in early stages, so please expect a lot of bugs. Please report anything you find to us through the direct messaging system in your control panel."

        # HOOKED TO VR


    "..."


    label introAct:
        "...{w} Start of Prologue"
        scene bg blackScreen
        $ renpy.pause(delay = 2, hard = True)

        scene bg cave
        with fade
        # entering the game

        "Huh..? Where am I?{w} Am I in a cave?"
        "I should climb up."

        # exits cave
        #scene bg outsideOfCave

        mc "Wow... I expected no less from Odyssey7!"

        # pan or show village

        mc "Now if this game follows every videogame trope ever, the quest would start in that village over there."
        mc "I should head over to the village."

        # maybe fade to black and play footstep noises?

        scene bg blackScreen
        with fade

        # introduction to jeremy and audrey

        scene bg berries 
        with fade

        "Huh, are those people?{w} They must be the new AI characters that Odyssey said they made. I should go up to them!"
        "..."
        mc "Hey, you two! Hey!"

        scene bg berriesWithout

        # talk to jeremy and audrey

        show audrey default at left
        #show jeremy default at right

        show jeremy default at right

        a "Hey!{w} I’ve never seen you before, what's your name?"
        mc "I'm [name]."

        show audrey happy at left

        a "Oh, hi [name]! Welcome to our village! I’m Audrey. This guy is my best friend."

        show jeremy wideSmile at right

        j "Nice to meet you, [name]!"

        show jeremy smile at right

        j "You should come with us to the village chief.{w} Audrey and I have an important task. You could help us!"
        mc "Well alright!"

        scene bg villageHouse
        show audrey default at left
        show jeremy default at right
        show chief happy 

        vc "Welcome back Audrey and Jeremy. I see you brought a friend as well!"

        show jeremy confused at right

        j "Yes, we found [name] wandering around the tree."

        show chief scrunched

        vc " Oh, you’re interested in Yggdrasil? It was cursed a few years ago by an evil wizard…. The surrounding area of the tree to sink miles down from the surface, hence the massive rock walls surrounding our land. It is slowly making our land infertile, meaning we’ll run out of food soon."

        mc "Ah, that’s unfortunate. What can I do to help?"

        show chief happy

        vc "Our villager scientists devised a cure with rare ingredients being locked away in 3 hidden locations.{w} We want to send our best adventurers, like Audrey and Jeremy here, to get them.{w} [name], you can help out as well. "

        show audrey happy at left
        show jeremy smile at right

        j "Yeah, [name], you should come!"
        mc "Sure, I'll help you guys. Where do we start searching?"

        show audrey default at left
        a "Well, we can always start at the heart of the problem."


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
        with fade

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

            g "...{w} Hello."
            g "I'm "

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
        
    #    "Test"


    return