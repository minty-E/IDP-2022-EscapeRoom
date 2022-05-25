init python:
    import time
    from tabulate import tabulate

    hintUsed = 0

    def time_convert(sec):
        sec += (hintUsed * 10)
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

#act 1 stuff
define shuffle = 1
define firsttouch = True
init python:
    piecesinplace = 0
    currentlayer = 1
    currentsmallx = 568
    currentsmally = 514
    currentmidx = 542
    currentmidy = 611
    currentbigx = 508 
    currentbigy = 707
    smallx = 0
    smally = 2
    midx = 0
    midy = 1
    bigx = 0 
    bigy = 0 
    def refresh():
        renpy.restart_interaction()
    def dragringsmall(drags, drop):
        global smallx 
        global smally 
        global currentsmallx
        global currentsmally
        global currentmidx
        global currentbigx
        if drop:
            if drop.drag_name == "0,0":
                if currentmidx != 536 and currentbigx != 508:
                    drags[0].snap(562,706)
                    currentsmallx = 562
                    currentsmally = 706
                    smallx = 0
                    smally = 0
                    return
            if drop.drag_name == "0,1":
                if currentmidx != 542:
                    if currentmidx == 536 or currentbigx == 508:
                        drags[0].snap(564, 607)
                        currentsmallx = 564
                        currentsmally = 607
                        smallx = 0
                        smally = 1
                        return
            if drop.drag_name == "0,2":
                if currentmidx == 542:
                    drags[0].snap(568, 514)
                    currentsmallx = 568
                    currentsmally = 514
                    smallx = 0
                    smally = 2
                    return  
            if drop.drag_name == "1,0":
                if currentmidx != 849 and currentbigx != 824:
                    drags[0].snap(880,707)
                    currentsmallx = 880
                    currentsmally = 707
                    smallx = 1
                    smally = 0
                    return
                        
            if drop.drag_name == "1,1":
                if currentmidx != 851:
                    if currentmidx == 849 or currentbigx == 824:
                        drags[0].snap(875, 607)
                        currentsmallx = 875
                        currentsmallly = 607
                        smallx = 1
                        smally = 1
                        return
            if drop.drag_name == "1,2":
                if currentmidx == 851:
                    drags[0].snap(874, 511)
                    currentsmallx = 874
                    currentsmallly = 511
                    smallx = 1
                    smally = 2        
                    return            
            if drop.drag_name == "2,0":
                if currentmidx != 1160:
                    drags[0].snap(1186, 706)
                    currentsmallx = 1186
                    currentsmallly = 70 
                    smallx = 2
                    smally = 0   
                    return
            if drop.drag_name == "2,1":
                if currentmidx != 1164:
                    if currentmidx == 1160 or currentbigx == 1118:
                        drags[0].snap(1187, 607)
                        currentsmallx = 1187
                        currentsmally = 607   
                        smallx = 2
                        smally = 1 
                        return
            if drop.drag_name == "2,2":
                if currentmidx == 1164:
                    drags[0].snap(1185,511)
                    currentsmallx = 1185
                    currentsmally = 511
                    smallx = 2
                    smally = 2
                    renpy.call_in_new_context("puzzle3complete")
                    return  
               
        drags[0].snap(currentsmallx,currentsmally)
        renpy.show_screen("pedestal2close")
        return
    def dragringmid(drags, drop):
        global midx 
        global midy 
        global currentmidx
        global currentmidy
        global currentsmallx
        global currentbigx
        if drop:
            if drop.drag_name == "0,0":
                if currentsmallx != 562 or currentbigx != 508:
                    drags[0].snap(536,706)
                    currentmidx = 536
                    currentmidy = 706
                    midx = 0
                    midy = 0
                    return
            if drop.drag_name == "1,0":
                if currentsmallx != 880 or currentbigx != 824:
                    drags[0].snap(849,704)
                    currentmidx = 849
                    currentmidy = 704
                    midx = 1
                    midy = 0
                    return 
            if drop.drag_name == "2,0":
                if currentsmallx != 1186 or currentbigx != 1118:
                    drags[0].snap(1160, 704)
                    currentmidx = 1160
                    currentmidy = 704
                    midx = 2
                    midy = 0
                    return
            if drop.drag_name == "0,1":
                if currentsmallx != 564:
                    if currentbigx == 508:
                        drags[0].snap(542,611)
                        currentmidx = 542
                        currentmidy = 611
                        midx = 0
                        midy = 1
            if drop.drag_name == "1,1":
                if currentsmallx != 875:
                    if currentbigx == 824:
                        drags[0].snap(851,608)
                        currentmidx = 851
                        currentmidy = 608
                        midx = 1
                        midy = 1
            if drop.drag_name == "2,1":
                if currentsmallx != 1187:
                    if currentbigx == 1118:
                        drags[0].snap(1164,607)
                        currentmidx = 1164
                        currentmidy = 607
                        midx = 2
                        midy = 1

        drags[0].snap(currentmidx,currentmidy)

        return
    def dragringbig(drags, drop):
        global bigx 
        global bigy 
        global currentbigx
        global currentbigy
        global currentsmallx
        global currentmidx
        if drop:
            if drop.drag_name == "0,0":
                if currentsmallx != 562 and currentmidx != 536:
                    drags[0].snap(508, 707)
                    currentbigx = 508
                    currentbigy = 707
                    bigx = 0
                    bigy = 0
            if drop.drag_name == "1,0":
                if currentsmallx != 880 and currentmidx != 849:
                    drags[0].snap(824,707)
                    currentbigx = 824
                    currentbigy = 707
                    bigx = 1
                    bigy = 0
            if drop.drag_name == "2,0":
                if currentsmallx != 1186 and currentmidx != 1160:
                    drags[0].snap(1118,707)
                    currentbigx = 1118
                    currentbigy = 707
                    bigx = 2
                    bigy = 0
        drags[0].snap(currentbigx,currentbigy)
        return          
    def snapinplace1(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 790:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 1:
                    renpy.call_in_new_context("puzzle2complete")   
                return

    def snapinplace2(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 885:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace3(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 812:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace4(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 1012:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                    return
    def snapinplace5(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 903:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace6(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 850:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace7(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 970:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace8(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 1026:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace9(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 799:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace10(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 1089:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace11(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 1007:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace12(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 850:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return
    def snapinplace13(drags, drop):
        global piecesinplace
        if drop:
            if drop.x == 978:
                drags[0].snap(drop.x,drop.y)
                drags[0].draggable = False
                piecesinplace = piecesinplace + 1
                if piecesinplace == 13:
                    renpy.call_in_new_context("puzzle2complete")
                return

    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop[0].drag_name

        return True
    from copy import deepcopy
    class slider_class:
        def __init__(self, rows, columns, size, image = None):
            self.rows = rows
            self.columns = columns
            self.pieces = []
            self.size = size
            self.image = image
            self.crops = []
            self.missing = None
            self.win = None

            self.build()
        def win_check(self):
            if all(item in self.pieces for item in self.win):
                return True
        def slide(self, index):
            if self.check(index):
                m = self.pieces[index]
                self.pieces[index] = self.missing
                self.missing = m
        def shuffle(self):
            for ii,i in enumerate(self.pieces):
                r = renpy.random.randint(0, len(self.pieces)-1)
                self.pieces[ii], self.pieces[r] = self.pieces[r], self.pieces[ii]

        def check(self, index):
            if self.pieces[index][0] == self.missing[0]:
                if self.pieces[index][1]+1 == self.missing[1] or self.pieces[index][1]-1 == self.missing[1]:
                    return True
            if self.pieces[index][1] == self.missing[1]:
                if self.pieces[index][0]+1 == self.missing[0] or self.pieces[index][0]-1 == self.missing[0]:
                    return True
            return False

        def build(self):
            self.pieces = []
            for i in range(self.rows):
                for ii in range(self.columns):
                    self.pieces.append([ii, i])
                    if self.image:
                        self.crops.append(Crop((ii*self.size, i*self.size, self.size, self.size), self.image))
            self.missing = self.pieces.pop(-1)
            self.win = deepcopy(self.pieces)
        def cheat(self, index):
            m = self.pieces[index]
            self.pieces[index] = self.missing
            self.missing = m


# slider_class(3,3,210) means 3 rows, 3 columns, size is 210
default slider_1  = slider_class(3, 3, 205)
screen slider(g = slider_1):
    add "backgrounds/dungeonwall.png"
    add "pedestals/pedestal1.png"
    modal True

    style_prefix "slider"
    default cheating = 1

    frame:
        xysize (g.columns*g.size)+30,(g.rows*g.size)+30
        xpos 625
        ypos 370
        background None
        if g.image and g.win == g.pieces:
            add g.image at slider_image
        for ii,i in enumerate(g.pieces):
            if i:
                button:
                    xysize g.size,g.size
                    at slider_piece(i[0]*g.size,i[1]*g.size)
                    anchor 0.0,0.0
                    if g.image:
                        add g.crops[ii]
                    else:
                        image "images/pieces/{}.png".format(ii)
                    if cheating:
                        if firsttouch == False:
                            action Function(g.cheat, ii)
                        
                    else:
                        action Function(g.slide, ii)

# this shuffles the thing idk how you can make it happen off screen
    if shuffle == 1:
        timer .2 repeat False action [Function(g.shuffle), SetVariable("shuffle", 0)]

    elif g.win == g.pieces:
        button:
            yalign 0.5
            xalign 0.5
            xsize 5000
            ysize 5000
            text "Proceed"
            hovered Return()
            action NullAction()

transform slider_piece(x, y):
    ease .2 xpos x ypos y
transform slider_image:
    alpha 0
    pause .4
    ease .2 alpha 1
style slider_text:
    size 30
        

# backgrounds

image bg blackScreen = "/backgrounds/blackScreen.png"
image bg cave = "/backgrounds/StartCaveBackground.png"
image bg bedroom = "/backgrounds/BedRoom.png"
image bg facility = "/backgrounds/Facility.png"
image bg dungeon = "/backgrounds/Dungeon.png"

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
        scene dungeon
        with fade

        "..."
        "ALERT: YOU HAVE BEEN TRAPPED IN A GAME, WE ARE WORKING TO FREE YOU."
        with vpunch
        window hide 
        call screen puzzle1()
        show screen slider with fade
        mc "What is this?"
        mc "Looks like a scrambled image of Yggdrasil..."
        mc "These tiles look like they can be moved."
        mc "Maybe I should try correcting the image."
        window hide
        $firsttouch = False
        call screen slider()
        show screen puzzle1complete with fade
        mc "The mirror moved. The light is pointing to the pedestal on the right now."
        mc "I should check it out."
        call screen puzzle1complete()
        show screen pedestal3close() with fade
        mc "The mirror is shattered. I should put the pieces back together."
        call screen pedestal3close()
        show screen puzzle2complete with fade
        show screen pedestal2close with fade
        mc "What is this supposed to be?"
        mc "There's a small piece of text here..."
        call screen pedestal2close()
label puzzle2complete:
    scene puzzle2complete
    call screen puzzle2completescreen() with fade
    show screen pedestal2close with fade
    mc "hm."
    call screen pedestal2close()

label puzzle3complete:
    scene puzzle3complete with fade
    pause
    # put open door thing
    


screen puzzle1():   
    modal True 
    imagebutton auto "pedestal1-%s":
        focus_mask True
        action Return()
screen puzzle1complete():
    add "backgrounds/puzzle1complete.png"
    modal True
    imagebutton auto "pedestal3-%s":
        focus_mask True
        action Return()

screen pedestal3close():
    add "backgrounds/dungeonwall.png"
    add "pedestals/pedestal3.png"
    modal True

    draggroup:
        drag:
            drag_name "piece1"
            child "mirror pieces/piece1.png"
            xpos 0.1
            ypos 0.75
            draggable True
            droppable False
            dragged snapinplace1
            drag_raise True
        drag:
            drag_name "piece2"
            child "mirror pieces/piece2.png"
            xpos 1
            ypos 0.75
            draggable True
            droppable False
            dragged snapinplace2
            drag_raise True
        drag:
            drag_name "piece3"
            child "mirror pieces/piece3.png"
            xpos 0.98  
            ypos 0.75
            draggable True
            droppable False
            dragged snapinplace3
            drag_raise True
        drag:
            drag_name "piece4"
            child "mirror pieces/piece4.png"
            xpos 0.75
            ypos 0.75
            draggable True
            droppable False
            dragged snapinplace4
            drag_raise True
        drag:
            drag_name "piece5"
            child "mirror pieces/piece5.png"
            xpos 0.1
            ypos 0.5
            draggable True
            droppable False
            dragged snapinplace5
            drag_raise True
        drag:
            drag_name "piece6"
            child "mirror pieces/piece6.png"
            xpos 0.3
            ypos 0.5
            draggable True
            droppable False
            dragged snapinplace6
            drag_raise True
        drag:
            drag_name "piece7"
            child "mirror pieces/piece7.png"
            xpos 0
            ypos 0.5
            draggable True
            droppable False
            dragged snapinplace7
            drag_raise True
        drag:
            drag_name "piece8"
            child "mirror pieces/piece8.png"
            xpos 0.75
            ypos 0.5
            draggable True
            droppable False
            dragged snapinplace8
            drag_raise True
        drag:
            drag_name "piece9"
            child "mirror pieces/piece9.png"
            xpos 1
            ypos 0.5
            draggable True
            droppable False
            dragged snapinplace9
            drag_raise True
        drag:
            drag_name "piece10"
            child "mirror pieces/piece10.png"
            xpos 1
            ypos 0.5874
            draggable True
            droppable False
            dragged snapinplace10
            drag_raise True
        drag:
            drag_name "piece11"
            child "mirror pieces/piece11.png"
            xpos 0.2
            ypos 0.471
            draggable True
            droppable False
            dragged snapinplace11
            drag_raise True
        drag:
            drag_name "piece12"
            child "mirror pieces/piece12.png"
            xpos 0.1
            ypos 0.2328
            draggable True
            droppable False
            dragged snapinplace12
            drag_raise True
        drag:
            drag_name "piece13"
            child "mirror pieces/piece13.png"
            xpos 0.1
            ypos 0.58329
            draggable True
            droppable False
            dragged snapinplace13
            drag_raise True
        drag:
            drag_name "piece1"
            xpos 790
            ypos 202
            draggable False
            droppable True
            xsize 93
            ysize 141

        drag:
            drag_name "piece2"
            xpos 885
            ypos 384
            xsize 137
            ysize 117
            draggable False
            droppable True
        drag:
            drag_name "piece3"
            xpos 812
            ypos 360
            xsize 105
            ysize 110
            draggable False
            droppable True
        drag:
            drag_name "piece4"
            xpos 1012
            ypos 420
            xsize 70
            ysize 78
            draggable False
            droppable True
        drag:
            drag_name "piece5"
            xpos 903
            ypos 321
            xsize 139
            ysize 96
            draggable False
            droppable True
        drag:
            drag_name "piece6"
            xpos 850
            ypos 180
            xsize 208
            ysize 87
            draggable False
            droppable True
        drag:
            drag_name "piece7"
            xpos 970
            ypos 213
            xsize 64
            ysize 73
            draggable False
            droppable True
        drag:
            drag_name "piece8"
            xpos 1026
            ypos 213
            xsize 96
            ysize 105
            draggable False
            droppable True
        drag:
            drag_name "piece9"
            xpos 799
            ypos 295
            xsize 132
            ysize 101
            draggable False
            droppable True
        drag:
            drag_name "piece10"
            xpos 1089
            ypos 306
            xsize 38
            ysize 89
            draggable False
            droppable True
        drag:
            drag_name "piece11"
            xpos 1007
            ypos 321
            xsize 114
            ysize 141
            draggable False
            droppable True
        drag:
            drag_name "piece12"
            xpos 850
            ypos 248
            xsize 139
            ysize 79
            draggable False
            droppable True
        drag:
            drag_name "piece13"
            xpos 978
            ypos 257
            xsize 126
            ysize 97
            draggable False
            droppable True




            # enter or implement dragging code 

            # hanoi puzzle IMPORTANT

            # drag and drop pieces of mirror, get artist to do this

        # death of jeremy and audrey leaves

        # get ingredient

        # contact by company, move to cave

    


    #label act2:
        # arrive in cave
        # "Hm, the cave is blocked."

        # label puzzle2:
            # torch puzzle, clicking image buttons to change orientation

            # move to memorial where npc guard instructs to solve puzzles

           # g "...{w} Hello."
           # g "I'm "

            # recreate a piano melody

            # find correct part of statue and drag and drop on it

            

        # receive 2nd ingredient

    #label act3: 
        # enter tower

        # voice in tower calls out to pass trial 

        # each task will form more stairs

        #label puzzle3:
            # make a light purple, code different color combinations, drag and drop

            # shuffle different letters to form words

            # slide on image, maze puzzle

        # arrive at top of tower

    # label ending: 
        # audrey shows up hacked
        # hacker sends spells through audrey, quick time events to stop
        # health bar will lower if user fails 
        # company sends spell book to kill audrey
        # mixes three ingredients to cure the tree
        # curing tree leads to exiting the game
        # hacker gets arrested and user gets sent home



    #"..."
    # "This is the end of the game."
    #$ end_time = time.time()
    #$ time_lapsed = end_time - start_time
    #$ time_convert(time_lapsed)
        
    #    "Test"

screen puzzle2completescreen:
    add "backgrounds/puzzle2complete.png"
    modal True
    imagebutton auto "pedestal2-%s":
        focus_mask True
        action Return()
screen pedestal2close:
    add "backgrounds/dungeonwall.png"
    add "pedestals/renpypedestal2.png"
    modal True
    timer .2 repeat True action Function(refresh)
    draggroup:
        drag:
            focus_mask True
            drag_name "bigring"
            child "tower of hanoi/bigring.png"
            xpos 508
            ypos 707
            dragged dragringbig
            draggable If(bigy + 1 == smally and bigx == smallx or bigy + 1 == midy and bigx == midx,true= False,false= True)
            droppable False
            drag_raise True

        drag:
            focus_mask True
            drag_name "midring"
            child "tower of hanoi/midring.png"
            xpos 542
            ypos 611
            dragged dragringmid
            draggable If(midy + 1 == smally and midx == smallx,true= False,false= True)
            droppable False
            drag_raise True

        drag:
            focus_mask True
            drag_name "smallring"
            child "tower of hanoi/smallring.png"
            xpos 568
            ypos 514
            dragged dragringsmall
            draggable True
            droppable False
        drag:
            drag_name "0,0"
            xpos 567
            ypos 706
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag:
            drag_name "0,1"
            xpos 568
            ypos 607
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag:
            drag_name "0,2"
            xpos 566
            ypos 511
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag:
            drag_name "1,0"
            xpos 880
            ypos 707
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag:
            drag_name "1,1"
            xpos 875
            ypos 608
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag:
            drag_name "1,2"
            xpos 881
            ypos 512
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag:
            drag_name "2,0"
            xpos 1124
            ypos 708
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag:
            drag_name "2,1"
            xpos 1187
            ypos 609
            xsize 100
            ysize 60
            draggable False
            droppable True
        drag: 
            drag_name "2,2"
            xpos 1183
            ypos 513
            xsize 100
            ysize 60
            draggable False
            droppable True



#    return
 
