init python:
    import time
    import gspread
    from gspread.foauth2client.service_account import ServiceAccountCredentials
    from tabulate import tabulate

    hintUsed = 0

    def time_convert(sec):
        sec += (hintUsed * 10)
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        totalTime = ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))

    def starting_time():
        start_time = time.time()


    def ending_time():
        end_time = time.time()
        time_lapsed = end_time - start_time
        time_convert(time_lapsed)
        


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
define v = Character("Mysterious Voice")
define o = Character("Odyssey7")
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
# scientist 1 photos
image scientist1 default = "/scientists/scientist1default.png"
image scientist1 smile = "/scientists/scientist1smile.png"
# scientist 2 photos
image scientist2 default = "/scientists/scientist2default.png"
image scientist2 smile = "/sceintists/scientist2smile.png"
# guard
image guard default = "/guard/guardDefault.png"
#doortext
image doortext = "doortext.png"

#act 1 stuff
define blink = Fade(1.0, 0.0, 1.0, color= "#000")
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
    def check():
        if torch1dir == 2 and torch2dir == 0 and torch4dir == 3 and torch5dir == 1:
            renpy.call_in_new_context("act2puzzle1complete")
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
                if currentmidx != 1160 and currentbigx != 1118:
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
                if currentsmallx != 562 and currentbigx != 508:
                    drags[0].snap(536,706)
                    currentmidx = 536
                    currentmidy = 706
                    midx = 0
                    midy = 0
                    return
            if drop.drag_name == "1,0":
                if currentsmallx != 880 and currentbigx != 824:
                    drags[0].snap(849,704)
                    currentmidx = 849
                    currentmidy = 704
                    midx = 1
                    midy = 0
                    return 
            if drop.drag_name == "2,0":
                if currentsmallx != 1186 and currentbigx != 1118:
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
                if piecesinplace == 13:
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
                drags[0].snap(850,180)
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
                        action Function(g.cheat, ii)
                        
                    else:
                        action [Function(g.slide, ii), Play("sound", "/audio/tileslide.mp3")]

# this shuffles the thing idk how you can make it happen off screen
    if shuffle == 1:
        timer .2 repeat False action [Function(g.shuffle), SetVariable("shuffle", 0)]

    elif g.win == g.pieces:
        timer .2 repeat False action Return()
transform slider_piece(x, y):
    ease .2 xpos x ypos y
transform slider_image:
    alpha 0
    pause .4
    ease .2 alpha 1
style slider_text:
    size 30
  

# act 2 stuff
define torch1selected = False
define torch1dir = 0  
define torch2dir = 0
define torch3dir = 0
define torch4dir = 0
define torch5dir = 0
define firsttime1 = True
define firsttime2 = True 
define firsttime3 = True
define key1 = 0
define key2 = 0
define key3 = 0
define key4 = 0
define key5 = 0
define keyspressed = 1
define atrightstatue = False
define haspiano = False
define plantsTaken = 0
define correctPlant = False
define page = 1

# act 3 stuff
define act = 1
# backgrounds

image bg blackScreen = "/backgrounds/blackScreen.png"
image bg cave = "/backgrounds/StartCaveBackground.png"
image bg bedroom = "/backgrounds/BedRoom.png"
image bg facility = "/backgrounds/Facility.png"
image bg dungeon = "/backgrounds/Dungeon.png"
image bg tree = "/backgrounds/tree.png"
image bg memorial = "/backgrounds/memorial.png"
image bg memorialrightopen = "/backgrounds/memorialrightopen.png"
image bg plantbox = "/backgrounds/plantbox.png"
image bg caveentrance = "/backgrounds/CaveEntrance.png"
image bg memorialrightopen = "/act2/memorialrightopen.png"
image bg towerentrance = "/backgrounds/towerentrance.png"
image bg towerfloor1 = "/backgrounds/TowerFloor1.png"
image bg towerfloor2 = "/backgrounds/TowerFloor2.png"
image bg towerfloor3 = "/backgrounds/Towerfloor3.png"
image bg rightcloseup = "/act2/rightstatuecloseup.png"
image bg house = "/backgrounds/house.png"
# image ralsei default = "ralsei.jpeg"
# The game starts here.

# label addTime:
#    hintUsed++


label start:
    $config.after_load_callbacks = [prepareLoad]
    $config.rollback_enabled = False
    $quick_menu = False
    $environment_SM = SpriteManager(event = environmentEvents)
    $inventory_SM = SpriteManager(update= inventoryUpdate, event= inventoryEvents)
    $environment_sprites = []
    $inventory_sprites = []
    $environment_items = []
    $inventory_items = []
    $environment_item_names = []
    $inventory_item_names = ["ThumbPiano", "MusicBox", "Axade", "GlowingFluxroot", "Huxtous", "Kreaf", "Ootross", "WildSorrel", "Xoom", "Zum"]
    $current_scene = "scene1"
    $inventory_rb_enabled = False
    $inventory_lb_enabled = False
    $inventory_slot_size = (160, 140)
    $inventory_slot_padding = 34 / 2
    $inventory_first_slot_x = 525
    $dialogue = {}
    $inventory_drag = False
    $item_dragged = ""
    $mousepos = (0.0, 0.0)
    $i_overlap = False
    $ie_overlap = False
    $currentscreen = ""
    $guardspoke = False


    
    scene bg blackScreen
    
    $ name = renpy.input("What is your name?")
    $ name = name.strip()
    $ start_time = time.time()


    scene bg bedroom with fade

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
        mc "This is crazy."
        mc "I guess I'll head over to their facility now."
    label facility:
        scene bg facility
        mc "This is so high tech..."
        show scientist1 smile at right
        s1 "Hello there [name]! I see you received our email about testing our new game."
        mc "Of course. It would be a shame if I pass up such a good opportunity."
        s1 "I’m glad to hear that!{w} Now, enough said, let’s get you into the game. Follow me!"
        hide scientist1 smile
        scene bg facility
        with fade
        show scientist1 default at right
        s1 "Before we begin your experience, please measure and record your heart rate."
        $ hRate = renpy.input("Enter heart rate and press enter: ")
        $ hRate = hRate.strip()
        hide scientist1 default
        #s2 helps with vr headset
        show scientist2 default at left
        s2 "...{w} Alright, you’re all set. Just remember that the game is still in early stages, so please expect a lot of bugs. Please report anything you find to us through the direct messaging system in your control panel."
        hide scientist2 default
        # HOOKED TO VR


    "..."


    label introAct:
        "...{w}"
        scene bg blackScreen
        $ renpy.pause(delay = 2, hard = True)

        scene bg cave
        with fade
        # entering the game

        "Huh..? Where am I?{w} Am I in a cave?"
        "I should climb up."

        # exits cave
        #scene bg outsideOfCave
        scene bg tree with fade

        mc "Wow... I expected no less from Odyssey7!"

        # pan or show village

        mc "Odyssey7 never game me any instructions as to where to go..."
        mc "I guess I could just explore around here."

        "Huh, are those people?{w} They must be the new AI characters that Odyssey said they made. I should go up to them!"
        "..."
        mc "Hey, you two! Hey!"
        # maybe fade to black and play footstep noises?

        show audrey default at left with fade
        #show jeremy default at right

        show jeremy default at right with fade

        a "Hey!{w} I’ve never seen you before, what's your name?"
        mc "I'm [name]."

        show audrey happy at left

        a "Oh, hi [name]! Welcome to our village! I’m Audrey. This guy is my best friend."

        show jeremy wideSmile at right

        j "Nice to meet you, [name]!"

        show jeremy smile at right

        j "You should come with us to the village chief.{w} Audrey and I have an important task. You could help us!"
        mc "Well alright!"

        scene bg house with fade
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
        scene bg blackScreen with fade
        with vpunch

    # act 1
    label act1:
        scene bg dungeon with blink
        scene bg dungeon with blink
        scene bg dungeon with blink

        mc "..."
        mc "What just happened?"
        mc "Where am I?"

        "WE HAVE JUST RECIEVED WORD THAT A HACKER HAS TRAPPED YOU INSIDE THE GAME"
        "YOUR REAL BODY IS CURRENTLY IN A COMA STATE."
        "BEAT THE GAME AND CURE THE TREE AND WE MIGHT BE ABLE TO BRING YOU BACK"
        "IF YOU FAIL TO DO SO IN 30 MINUTES..."
        with vpunch
        with hpunch
        "YOU WILL BE TRAPPED FOREVER"
        with vpunch
        with hpunch
        "YOUR REAL BODY WILL DIE"
        "THE HACKER TRIED TO TRAP YOU IN A DUNGEON FOUND WITHIN THE GAME...BUT THAT IS WHERE THE FIRST INGREDIENT IS GROWN"
        "HOWEVER, IT IS GUARDED BY PUZZLES"
        "TRY YOUR BEST... YOUR LIFE DEPENDS ON IT"
        "We'll contact you once you finish the puzzles here."
        "Good luck."
        with fade
        window hide
        mc "Seriously? Am I living in some video game plot or what?"
        mc "30 minutes is barely enough time..."
        mc "Jeremy? Audrey? Are you there?"
        show jeremy confused at right with fade
        j "Yeah, I'm here. That drop hurt a little bit... Audrey, where are you?!"
        show audrey default at left with fade
        a "I'm more or less fine. Are you guys okay?"
        mc "Yes, surprisingly."
        mc "We have to get out of here. Let's just look around this room, maybe we can find a way to get out."
        hide jeremy confused with fade
        hide audrey default with fade 

        call screen door()
        mc "It's locked."
        mc "Wait.. there's a small piece of text on the door."
        show doortext with fade
        mc "What does this mean? Jeremy, do you think you could read this for me? I can't understand it."
        show jeremy wideSmile at right
        j "Oh, of course! Let me see..."
        show jeremy smile at right
        j "It says something about guiding light towards the door..."
        mc "Hmm.. okay. Thank you."
        j "Yeah, no problem!"
        hide jeremy wideSmile 
        hide jeremy smile with fade
        hide doortext with fade
        "This room has mirrors in it and a ray of light shooting at one of the crystals."
        "I should check out the pedestal here on the left. Maybe I could move it."

        call screen puzzle1()
        show screen slider with fade
        mc "What is this?"
        mc "Looks like a scrambled image of Yggdrasil..."
        mc "These tiles look like they can be moved."
        mc "Maybe I should try correcting the image."
        window hide
        $firsttouch = False
        call screen slider()
        show bg blackScreen with fade
        show screen puzzle1complete with fade
        mc "The mirror moved. The light is pointing to the pedestal on the right now."
        mc "I should check it out."
        window hide
        call screen puzzle1complete()
        scene puzzle1complete
        show screen pedestal3close with fade
        mc "The mirror is shattered. I should put the pieces back together."
        window hide
        call screen pedestal3close()
        show screen puzzle2complete with fade
        show screen pedestal2close with fade
        mc "What is this supposed to be?"
        mc "There's a small piece of text here..."
        window hide 
        call screen pedestal2close()

        # where is ending?
        $ ending_time()
        $ starting_time()

        renpy.say(" ", ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec))))
label puzzle2complete:
    scene puzzle2complete
    call screen puzzle2completescreen() with fade
    show screen pedestal2close with fade
    mc "What are these rings? I don't quite understand..."
    show jeremy wideSmile at left
    j "There's a piece of text under here!"
    hide jeremy wideSmile
    show screen puzzle3instr with fade
    mc "..."
    mc "So I have to stack the rings on the third pole..."
    mc "without stacking a bigger one on a smaller."
    hide screen puzzle3instr with fade
    call screen pedestal2close()

    $ ending_time()
    $ starting_time()

label puzzle3complete:
    scene puzzle3complete with fade
<<<<<<< HEAD
    # show screen dooropen with fade
    scene caveentrance with fade
    $act = 2
    "I do really feel bad for Audrey.. but I can't focus on that."
    "I have to get the next ingredient."
    "My life is at stake here. They're just programmed NPC's, not even real people."
    "The company said the entrance is through this cave."
    "It looks oddly similar to the one you start in."
    scene darkwall with fade
    show screen torchpuzzle
    "A dead end?"
    "Odyssey7 said the entrance to the memorial would be right here."
    "Maybe I should inspect these torches."
    "I might find something useful."
    call screen torchpuzzle()

label act2puzzle1complete:
    
    scene memorial with fade
    "So this is the memorial they were talking about... "
    "It seems very peaceful."
    show guard default at right
    g "Hello adventurer! It appears that you've gotten through the cave."
    g "If you're here you must be looking for (ingredient name)."
    g "One of the past village chiefs has locked it inside his statue and put a series of puzzles in place to make sure it wouldn't fall into the wrong hands."
    g "If you wish to recieve the ingredient you must solve the puzzles he has laid out."
    g "Start by checking out the statue on the right."
    g "I wish you the best of luck."
    hide guard default
    show screen UI
    "The guard said to check out the right statue..."
    "I guess I'll head there first."
    call screen rightstatue()
    scene rightstatuecloseup with fade
    "It says this guy wished to hear a tune his mother alwyays sung to him."
    "What is the tune though?"
    "Oh, wait, there's a music box on the side here."
    $addmusicbox()
    call screen rightstatueclose()
    call screen memorial()
screen rightstatueclose:
    timer .2 repeat False action SetVariable("atrightstatue", True)
    add "/act2/rightstatuecloseup.png"
    imagebutton:
        focus_mask True 
        idle "UI/exitui.png"
        xpos -1245
        ypos -86
        action [Show("memorial", transition = fade), Hide("rightstatueclose")]
label act2puzzle2complete:
    scene memorialrightopen with fade
    "The statue opened!"
    "Is there anything inside?"
=======
    pause
    # put open door thing
    $ ending_time()
    $ starting_time()

label endingSurvey:
    #finish fail safe
    q1 = input("What was the best or worst puzzle in the game and why?")
    q2 = input("How would you rate the overall experience 1 to 5?")
    q3 = input("Would you recommend it to a friend?")
    q4 = input("On a scale from  1 to 5, how engaging were the puzzles?")
    q5 = input("How were you feeling throughout the game? Select all that apply.")
>>>>>>> main

    call screen rightcompartment()
    pause

label leftstatue:
    "It says something about this guy having rashes on his hands.."
    "The journal might have something about rashes in it."
    call screen act2puzzle3screen()
    pause
label plantboxlabel:
    if guardspoke == False:
        show guard default at right
        g "I see that you've made it this far."
        g "However, I cannot permit you to grab any more than 2 plants from this plant box."
        g "Choose wisely."
        hide guard default
        $ guardspoke = True
    mc "Okay, I have to choose the correct plant according to the statue I read earlier."
    mc "I can use this plant journal to identify these plants and make the right decision."
    mc "Best not to find out what happens when I get the wrong one."
    $environment_items = ["axade", "glowingfluxroot", "huxtous", "kreaf", "ootross", "wildsorrel", "xoom", "zum"]
    python:
        for item in environment_items:
            idle_image = Image("Environment Items/{}-idle.png".format(item))
            hover_image = Image("Environment Items/{}-hover.png".format(item))
            t = Transform(child= idle_image)
            environment_sprites.append(environment_SM.create(t))
            environment_sprites[-1].type = item
            environment_sprites[-1].idle_image = idle_image
            environment_sprites[-1].hover_image = hover_image
            # sets up positions of the items change for our items
            if item == "axade":
                environment_sprites[-1].width = 217
                environment_sprites[-1].height = 386 
                environment_sprites[-1].x = 999
                environment_sprites[-1].y = 135
            elif item == "glowingfluxroot":
                environment_sprites[-1].width = 215
                environment_sprites[-1].height = 368
                environment_sprites[-1].x = 581
                environment_sprites[-1].y = 146
            elif item == "huxtous":
                environment_sprites[-1].width = 214
                environment_sprites[-1].height = 351
                environment_sprites[-1].x = 1400
                environment_sprites[-1].y = 163
            elif item == "kreaf":
                environment_sprites[-1].width = 344
                environment_sprites[-1].height = 352
                environment_sprites[-1].x = 716
                environment_sprites[-1].y = 162
            elif item == "ootross":
                environment_sprites[-1].width = 213
                environment_sprites[-1].height = 352
                environment_sprites[-1].x = 119
                environment_sprites[-1].y = 162
            elif item == "wildsorrel":
                environment_sprites[-1].width = 203
                environment_sprites[-1].height = 372
                environment_sprites[-1].x = 1588
                environment_sprites[-1].y = 142
            elif item == "xoom":
                environment_sprites[-1].width = 297
                environment_sprites[-1].height = 332
                environment_sprites[-1].x = 1159
                environment_sprites[-1].y = 182
            elif item == "zum":
                environment_sprites[-1].width = 368
                environment_sprites[-1].height = 430
                environment_sprites[-1].x = 261
                environment_sprites[-1].y = 84
    scene plantbox
    show screen UI
    call screen plantboxclose
screen plantboxclose():
    $currentscreen = "plantboxclose"
    add environment_SM
label act2puzzle3:
    scene memorialrightopen
    show screen UI
    pause
    call screen act2puzzle3leftstatue()
    mc "The statue says something about this past village chief always having a rash on his hand."
    mc "Maybe I could help get rid of them with something."
    call screen act2puzzle3screen()
screen act2puzzle3leftstatue():
    imagebutton auto "act2/leftstatue-%s.png":
        focus_mask True
        action Return()
screen act2puzzle3screen():
    $currentscreen = "act2puzzle3screen"
    add "/act2/memorialrightopen.png"
    imagebutton auto "act2/plantbox-%s.png":
        focus_mask True 
        action ShowMenu("plantboxlabel")

screen rightcompartment():
    imagebutton auto "act2/rightcompartment-%s.png":
        focus_mask True 
        action Function(addplantjournal)
screen rightstatue():
    imagebutton auto "act2/musicstatue-%s.png":
        focus_mask True 
        action Return()
label pianolabel:
    call screen piano()
    pause
label musiclabel:
    call screen musicbox()
    pause
label plantlabel:
    if currentscreen == "rightstatueclose":
        show screen rightstatueclose
    elif currentscreen == "memorial":
        show screen memorial
    elif currentscreen == "plantboxclose":
        show screen plantboxclose
    elif currentscreen == "act2puzzle3screen":
        show screen act2puzzle3screen
    call screen plantjournal()
    pause
label gotCorrectPlant:
    show guard default at right
    g "Good job adventurer!"
    g "You have recieved the correct plant."
    g "Huxtous is in fact the ingredient you have been searching for."
    g "I wish you the best of luck on the rest of your journey."
    hide guard default
    "Hello [name]! Good job for getting the next ingredient. You're journey is almost complete."
    "The last place you have to go to is a tall tower near the memorial."
    "You should actually be able to see it from there."
    "Good luck."
    jump act3
label gotWrongPlant:
    "Hello."
    "This is Odyssey7 speaking."
    "I'm afraid that you failed this puzzle. We can give you the right plant via our computers."
    "However, the time to get you will be shortened by a few minutes."
    $ addToInventory(["huxtous"])
    $ renpy.show_screen("inspectItem", ["huxtous"])
    mc "Oh."
    mc "I've screwed myself over."
    mc "Now I have to work faster to escape with my life..."
    "The next area you must go to is the tower in the back of the memorial. Be careful however."
    "To retrieve the last and final ingredient you must prove your worth."
    jump act3
label act3:
    scene towerEntrance with fade
    $act = 3
    "So this is the tower they were talking about."
    "Look menacing..."
    "I guess I'll head in."
    scene towerfloor1 with fade
    "What is this place.."
    "And why is it so messy?"
    with hpunch
    v "W H O. G O E S. T H E R E."
    v "You must be here to recieve a special item, but if you wish to do so..."
    with vpunch
    v "You must prove that you are worthy enough."
    v "I have 3 tasks for you."
    v "Fail to do them correctly, and you'll but just another simpleton."
    v "The first thing you must do is follow the instructions on the wall to make a potion."
    "I better make sure to not mess up or do anything wrong."
    "Odyssey7 might have to intervene to help me..."
    "Which in turn will shorten the time to get me out.."
    show screen UI
    $refreshEnvironment()
    call screen act3puzzle1Instructions()
    $addnote()

label Potions:
    show screen UI
    $environment_items = ["blue", "red"]
    python:
        for item in environment_items:
            idle_image = Image("Environment Items/{}-idle.png".format(item))
            hover_image = Image("Environment Items/{}-hover.png".format(item))
            t = Transform(child= idle_image)
            environment_sprites.append(environment_SM.create(t))
            environment_sprites[-1].type = item
            environment_sprites[-1].idle_image = idle_image
            environment_sprites[-1].hover_image = hover_image
            # sets up positions of the items change for our items
            if item == "blue":
                environment_sprites[-1].width = 130
                environment_sprites[-1].height = 199
                environment_sprites[-1].x = 571
                environment_sprites[-1].y = 820
            elif item == "red":
                environment_sprites[-1].width = 125
                environment_sprites[-1].height = 177
                environment_sprites[-1].x = 400
                environment_sprites[-1].y = 169
           
    scene towerfloor1
    show screen UI
    call screen towerfloor1Potions()

screen towerfloor1Potions:
    add environment_SM 
label act3puzzle1complete:
    v "Good job adventurer."
    v "Onto the next one."
    v "They'll only get harder from here."
label act3puzzle2:

label tooManyPlants:
    show guard default at right 
    g "You have already chose a plant. I'm afraid I can't let you get another one."
    hide guard default at right
    call screen plantboxclose
    pause
label torchinstructions:
    show screen torchinstr with fade
    mc "What is this?"
    mc "It seems like it has to do with the level of fire each torch has..."
    mc "... and the direction they turn."
    mc "I can't move this torch so I'm guessing it's already in the right spot."
    mc "This engraving also has 2 empty spots here."
    mc "I wonder what those could be?"
    hide screen torchinstr with fade
    # put dialogue
    # put open door thing
    $ ending_time()
    $ starting_time()

label endingSurvey:
    #finish fail safe
    q1 = input("What was the best or worst puzzle in the game and why?")
    q2 = input("How would you rate the overall experience 1 to 5?")
    q3 = input("Would you recommend it to a friend?")
    q4 = input("On a scale from  1 to 5, how engaging were the puzzles?")
    q5 = input("How were you feeling throughout the game? Select all that apply.")

screen puzzle3instr:
    add "pedestals/puzzle3instr.png" xalign 0 yalign 0
screen act3puzzle1Instructions():
    imagebutton auto "/act3/note-%s.png":
        focus_mask True 
        action Return()

screen door():
    imagebutton auto "door-%s":
        focus_mask True
        action [Play("sound", "audio/click.mp3"), Return()]
screen puzzle1():   
    imagebutton auto "pedestal1-%s":
        focus_mask True
        action [Play("sound", "audio/click.mp3"), Return()]
screen puzzle1complete():
    add "backgrounds/puzzle1complete.png"
    imagebutton auto "pedestal3-%s":
        focus_mask True
        action [Play("sound", "audio/click.mp3"), Return()]

screen pedestal3close():
    modal True
    add "backgrounds/dungeonwall.png"
    add "pedestals/pedestal3.png"   
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
    
        
    #    "Test"

screen puzzle2completescreen:
    add "backgrounds/puzzle2complete.png"
    imagebutton auto "pedestal2-%s":
        focus_mask True
        action Return()
screen pedestal2close:
    add "backgrounds/dungeonwall.png"
    add "pedestals/pedestal2.png"
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
            xsize 205
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
screen torchpuzzle():
    timer .2 repeat True action Function(check)

    imagebutton auto "torches/torch3-%s.png":
        focus_mask True
        xpos 1238
        ypos 620
        action ShowMenu("torchinstructions", transition= None)
    if torch1dir == 0:
        imagebutton:
            idle "torch1-0-idle"
            hover "torch1-0-hover"
            focus_mask True
            xpos 695
            ypos 445
            action [SetVariable("torch1dir", 1), Function(refresh)]
    if torch1dir == 1:
        imagebutton:
            idle "torch1-1-idle"
            hover "torch1-1-hover"
            focus_mask True
            xpos 695
            ypos 445
            action [SetVariable("torch1dir", 2), Function(refresh)]
    if torch1dir == 2:
        imagebutton:
            idle "torch1-2-idle"
            hover "torch1-2-hover"
            focus_mask True
            xpos 695
            ypos 445
            action [SetVariable("torch1dir", 3), Function(refresh)]
    if torch1dir == 3: 
        imagebutton:
            idle "torch1-3-idle"
            hover "torch1-3-hover"
            focus_mask True
            xpos 695
            ypos 445
            action [SetVariable("torch1dir", 0), Function(refresh)]


    if torch2dir == 0:
        imagebutton auto "torches/torch2-%s.png":
            focus_mask True
            xpos 1043
            ypos 161
            action SetVariable("torch2dir", 1)
    if torch2dir == 1:
        imagebutton auto "torches/torch2R-%s.png":
            focus_mask True
            xpos 1043
            ypos 161
            action SetVariable("torch2dir", 2)
    if torch2dir == 2:
        imagebutton auto "torches/torch2D-%s.png":
            focus_mask True
            xpos 1043
            ypos 161
            action SetVariable("torch2dir", 3)
    if torch2dir == 3: 
        imagebutton auto "torches/torch2L-%s.png":
            focus_mask True
            xpos 1043
            ypos 161
            action SetVariable("torch2dir", 0)

    if torch4dir == 0:
        imagebutton auto "torches/torch4U-%s.png":
            focus_mask True
            xpos 1006
            ypos 664
            action SetVariable("torch4dir", 1)
    if torch4dir == 1:
        imagebutton auto "torches/torch4R-%s.png":
            focus_mask True
            xpos 1006
            ypos 664
            action SetVariable("torch4dir", 2)
    if torch4dir == 2:
        imagebutton auto "torches/torch4D-%s.png":
            focus_mask True
            xpos 1006
            ypos 664
            action SetVariable("torch4dir", 3)
    if torch4dir == 3: 
        imagebutton auto "torches/torch4L-%s.png":
            focus_mask True
            xpos 1006
            ypos 664
            action SetVariable("torch4dir", 0)


    if torch5dir == 0:
        imagebutton auto "torches/torch5U-%s.png":
            focus_mask True
            xpos 1237
            ypos 300
            action SetVariable("torch5dir", 1)
    if torch5dir == 1:
        imagebutton auto "torches/torch5R-%s.png":
            focus_mask True
            xpos 1237
            ypos 300
            action SetVariable("torch5dir", 2)
    if torch5dir == 2:
        imagebutton auto "torches/torch5D-%s.png":
            focus_mask True
            xpos 1237
            ypos 300
            action SetVariable("torch5dir", 3)
    if torch5dir == 3: 
        imagebutton auto "torches/torch5L-%s.png":
            focus_mask True
            xpos 1237
            ypos 300
            action SetVariable("torch5dir", 0)

screen musicbox():
    modal True
    add "Items Pop Up/items-pop-up-bg.png" xalign 0.5 yalign 0.5
    imagebutton:
        focus_mask True
        idle "Items Pop Up/musicbox-pop-up.png" 
        xalign 0.5
        yalign 0.5
        action Play("sound", "<from 2.5 to 10>audio/fullsong.mp3")
    imagebutton:
        focus_mask True
        idle "UI/exitui.png"
        action [Hide("musicbox", transition= None), Show("UI", transition = None), If(atrightstatue == False, true= Show("memorial", transition= fade), false= Show("rightstatueclose", transition = fade))]

screen piano():
    modal True
    add "Items Pop Up/items-pop-up-bg.png" xalign 0.5 yalign 0.5
    add "images/Items Pop Up/thumbpiano-pop-up.png" 
    imagebutton:
        focus_mask True
        idle "UI/exitui.png"
        action [Hide("piano", transition= None), Show("UI", transition = None), If(atrightstatue == True, true= Show("rightstatueclose", transition = fade), false= Show("memorial", transition = fade))]
    imagebutton auto "images/piano/key1-%s.png":
        focus_mask True
        action [Play("sound", "<from 0.7 to 1.5>audio/pianokey1.mp3"), SetVariable("key{}".format(keyspressed), 1), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key2-%s.png":
        focus_mask True
        action [Play("sound", "<from 0.7 to 1.5>audio/pianokey2.mp3"), SetVariable("key{}".format(keyspressed), 2), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key3-%s.png":
        focus_mask True
        action [Play("sound", "<from 0.7 to 1.5>audio/pianokey3.mp3"), SetVariable("key{}".format(keyspressed), 3), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key4-%s.png":
        focus_mask True
        action [Play("sound", "<from 0.7 to 1.5>audio/pianokey4.mp3"), SetVariable("key{}".format(keyspressed), 4), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key5-%s.png":
        focus_mask True
        action [Play("sound", "<from 1.25 to 1.75>audio/pianokey5.mp3"), SetVariable("key{}".format(keyspressed), 5), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key6-%s.png":
        focus_mask True
        action [Play("sound", "<from 1.0 to 1.75>audio/pianokey6.mp3"), SetVariable("key{}".format(keyspressed), 6), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key7-%s.png":
        focus_mask True
        action [Play("sound", "<from 1.25 to 2>audio/pianokey7.mp3"), SetVariable("key{}".format(keyspressed), 7), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key8-%s.png":
        focus_mask True
        action [Play("sound", "<from 0.7 to 1.5>audio/pianokey8.mp3"), SetVariable("key{}".format(keyspressed), 8), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
    imagebutton auto "images/piano/key9-%s.png":
        focus_mask True
        action [Play("sound", "<from 0.7 to 1.5>audio/pianokey9.mp3"), SetVariable("key{}".format(keyspressed), 9), If(atrightstatue == True, true = SetVariable("keyspressed", keyspressed + 1), false = NullAction()), Function(checkpiano)]
screen memorial():
    $atrightstatue = False 
    timer .2 repeat False action [Show("UI", transition = None), SetVariable("atrightstatue", False)]
    add "/backgrounds/memorial.png"
    imagebutton auto "act2/musicstatue-%s.png":
        focus_mask True 
        action [Show("rightstatueclose", transition = fade), Hide("memorial")]
    imagebutton auto "act2/righthand-%s.png":
        focus_mask True
        action If(haspiano == False, true= [Function(addpiano), SetVariable("haspiano", True)], false = NullAction())
screen plantjournal():
    $global currentscreen
    add "/act2/journalpage{}.png".format(page)
    imagebutton:
        focus_mask True 
        idle "UI/exitui.png"
        xpos 367
        ypos -83
        action [Hide("plantjournal", transition= None), Show("UI", transition = None), If(currentscreen == "act2puzzle3screen", true = ShowMenu("act2puzzle3screen", transition= fade), false = Show("plantboxclose"))]
    imagebutton auto "/act2/rightarrow-%s.png":
        focus_mask True 
        action [SetVariable("page", If(page == 3, true= 3, false= page + 1)), Function(refresh)]
    imagebutton auto "/act2/leftarrow-%s.png":
        focus_mask True 
        xpos 107
        ypos 462
        action [SetVariable("page", If(page == 1, true= 1, false= page - 1)), Function(refresh)]


screen torchinstr:
    add "torches/torch3close.png" xalign 0.5

init python:
    def refreshEnvironment():
        for item in environment_sprites:
            removeEnvironmentItem(item)
        for item in inventory_sprites:
            removeInventoryItem(item)
        environment_SM.redraw(0)
        inventory_SM.redraw(0)
        repositionInventoryItems()
        renpy.restart_interaction()
    def checkpiano():
        global key1
        global key2
        global key3
        global key4
        global key5
        global keyspressed
        if keyspressed == 6:
            # change to the correct keys to press. ex: 1457 or smth
            if key1 == 4 and key2 == 9 and key3 == 7 and key4 == 5 and key5 == 6:
                #i kept getting an error if i didn't put interact = False so keep that in mind w/ dialogue
                renpy.hide_screen("piano")
                renpy.call_in_new_context("act2puzzle2complete")
                keyspressed = 1
            else:
                # this resets the keys you pressed so you can try again
                renpy.say([name],"that wasn't right.. let me try again.", interact = False)
                keyspressed = 1
    def addnote():
        addToInventory(["note"])
        renpy.show_screen("inspectItem", ["note"])
        characterSay(who = "[name]", what = ["A note.", "I wonder what's on it."], inspectItem = True)
        inventory_SM.redraw(0)
        environment_SM.redraw(0)
        renpy.restart_interaction()   
    def addmusicbox():
        addToInventory(["musicbox"])
        renpy.show_screen("inspectItem", ["musicbox"])
        characterSay(who = "(mc)", what = ["This must play the tune that the statue is talking about.", "I just need to find something to play it on now."], inspectItem = True)
        inventory_SM.redraw(0)
        environment_SM.redraw(0)
        renpy.restart_interaction()
    def addplantjournal():
        addToInventory(["plantjournal"])
        renpy.show_screen("inspectItem", ["plantjournal"])
        inventory_SM.redraw(0)
        environment_SM.redraw(0)
        renpy.restart_interaction()

    def addpiano():
        addToInventory(["thumbpiano"])
        renpy.show_screen("inspectItem", ["thumbpiano"])
        characterSay(who = "(mc)", what = ["A thumb piano.", "Maybe I could play the tune on this in front of the statue."], inspectItem = True)
        inventory_SM.redraw(0)
        environment_SM.redraw(0)
        renpy.restart_interaction()
        
   
    def inventoryUpdate(st):
        if inventory_drag == True:
            for item in inventory_sprites:
                if item.type == item_dragged:
                    item.x = mousepos[0] - item.width / 2
                    item.y = mousepos[1] - item.height / 2
                    item.zorder = 99
            return 0
        return None
    def inventoryEvents(event, x, y, at):
        global plantsTaken
        global mousepos
        global dialogue
        global inventory_drag
        global i_overlap
        global ie_overlap
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
                for item1 in inventory_sprites:
                    if item1.visible == True:
                        if item1.x <= x <= item1.x + item1.width and item1.y <= y <= item1.y + item1.height:
                            inventory_drag = False
                            i_combine = False
                            ie_combine = False
                            for item2 in inventory_sprites:
                                items_overlap = checkItemsOverlap(item1, item2)
                                # what happens when you combine items in inventory. change for specific items
                                if items_overlap == True:
                                    i_overlap = True
                                    if (item1.type == "red" or item1.type == "blue") and (item2.type == "red" or item2.type == "blue"):
                                        i_combine = True
                                        removeInventoryItem(item1)
                                        removeInventoryItem(item2)
                                        addToInventory(["purple"])
                                        renpy.show_screen("inspectItem", ["purple"])
                                        renpy.call_in_new_context("act3puzzle1complete")
                                    
                            if i_combine == False:
                                for item3 in environment_sprites:
                                    items_overlap = checkItemsOverlap(item1, item3)
                                    if items_overlap == True:
                                        ie_overlap = True
                                        if item1.type == "huxtous" and item3.type == "hand":
                                            ie_combine = True
                                           
                                            characterSay(who = "Claire", what = ["yas"], inspectItem = False)
                                            inventory_SM.redraw(0)
                                            environment_SM.redraw(0)
                                            renpy.restart_interaction()
                                            break
                            if i_combine == False and ie_combine == False:
                                item1.x = item1.original_x
                                item1.y = item1.original_y
                                item1.zorder = 0
        if event.type == renpy.pygame_sdl2.MOUSEMOTION:
            mousepos = (x, y)
            if inventory_drag == False:
                for item in inventory_sprites:
                    if item.visible == True:
                        if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                            renpy.show_screen("inventoryItemMenu", item = item)
                            renpy.restart_interaction()
                            break
                        else:
                            renpy.hide_screen("inventoryItemMenu")
                            renpy.restart_interaction()
    def environmentEvents(event, x, y, at):
        global plantsTaken
        global correctPlant
        if event.type == renpy.pygame_sdl2.MOUSEMOTION:
            for item in environment_sprites:
                if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                    t = Transform(child= item.hover_image, zoom= 1)
                    item.set_child(t)
                    environment_SM.redraw(0)
                else:
                    t = Transform(child= item.idle_image, zoom= 1)
                    item.set_child(t)
                    environment_SM.redraw(0)
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
                for item in environment_sprites:
                    if i_overlap == False and ie_overlap == False:
                        if item.x <= x <= item.x + item.width and item.y <= y <= item.y + item.height:
                                if act == 2:
                                    if plantsTaken < 1:

                                        if item.type == "axade":
                                            addToInventory(["axade"])
                                       
                                            renpy.show_screen("inspectItem", ["axade"])
                                    
                                        elif item.type == "zum":
                                            addToInventory(["zum"])
                                       
                                            renpy.show_screen("inspectItem", ["zum"])
                                        
                                        elif item.type == "glowingfluxroot":
                                            addToInventory(["glowingfluxroot"])
                                        
                                            renpy.show_screen("inspectItem", ["glowingfluxroot"])
                                
                                        elif item.type == "huxtous":
                                            correctPlant = True
                                            addToInventory(["huxtous"])
                                            renpy.show_screen("inspectItem", ["huxtous"])
                                        
                                        elif item.type == "kreaf":
                                            addToInventory(["kreaf"])
                                            renpy.show_screen("inspectItem", ["kreaf"])
                                  
                                        elif item.type == "ootross":
                                            addToInventory(["ootross"])
                                            renpy.show_screen("inspectItem", ["ootross"])
                                     
                                        elif item.type == "wildsorrel":
                                            addToInventory(["wildsorrel"])
                                            renpy.show_screen("inspectItem", ["wildsorrel"])
                                      
                                        elif item.type == "xoom":
                                            addToInventory(["xoom"])
                                            renpy.show_screen("inspectItem", ["xoom"])
                                    refreshEnvironment()
                                    refreshEnvironment()
                                    if correctPlant == True:
                                        renpy.call_in_new_context("gotCorrectPlant")
                                    else:
                                        renpy.call_in_new_context("gotWrongPlant")
                                else:
                                    if item.type == "blue":
                                        addToInventory(["blue"])
                                        renpy.show_screen("inspectItem", ["blue"])
                                    elif item.type == "red":
                                        addToInventory(["red"])
                                        renpy.show_screen("inspectItem", ["blue"])
                                


                            #what happens if you try to press an item that's locked
                global i_overlap
                global ie_overlap
                i_overlap = False
                ie_overlap = False

    def startDrag(item):
        global inventory_drag
        global item_dragged
        inventory_drag = True
        item_dragged = item.type
        inventory_SM.redraw(0)
    def checkItemsOverlap(item1, item2):
        if abs((item1.x + item1.width / 2) - (item2.x + item2.width / 2)) * 2 < item1.width + item2.width and abs((item1.y + item1.height / 2) - (item2.y + item2.height / 2)) * 2 < item1.height + item2.height and item1.type != item2.type:
            return True
        else:
            return False
    def characterSay(who, what, inspectItem = False):
        if isinstance(what, str):
            renpy.call_screen("characterSay", who = who, what = what)
        elif isinstance(what, list):
            global dialogue
            dialogue = {"who" : who, "what" : what}
            if inspectItem == False:
                renpy.show_screen("characterSay")
                renpy.restart_interaction()
    def repositionInventoryItems():
        global inventory_lb_enabled
        global inventory_rb_enabled

        for i, item in enumerate(inventory_sprites):
            if i == 0:
                item.x = inventory_first_slot_x
                inventory_sprites[-1].original_x = item.x
            else:
                item.x = (inventory_first_slot_x + inventory_slot_size[0] * i) + (inventory_slot_padding * i)
                inventory_sprites[-1].original_x = item.x
            if item.x < inventory_first_slot_x or item.x > (inventory_first_slot_x + (item.width * 7)) + (inventory_slot_padding * 5):
                setItemVisibility(item = item, visible = False)
            elif item != "":
                setItemVisibility(item = item, visible = True)
        renpy.retain_after_load()

    def addToInventory(items):
        for item in items:
            inventory_items.append(item)
            # for items with a specific state
            if item == "lantern":
                item_image = Image("Inventory Items/inventory-lantern-unlit.png")
            else:
                item_image = Image("Inventory Items/inventory-{}.png".format(item))

            t = Transform(child = item_image, zoom = 0.5)
            inventory_sprites.append(inventory_SM.create(t))
            inventory_sprites[-1].width = inventory_slot_size[0]
            inventory_sprites[-1].height = inventory_slot_size[1]
            inventory_sprites[-1].type = item
            inventory_sprites[-1].item_image = item_image
            inventory_sprites[-1].y = 920
            inventory_sprites[-1].x = 400
            inventory_sprites[-1].original_y = 920
            inventory_sprites[-1].original_x = 400
            inventory_sprites[-1].visible = True
            # for specific state
            if item == "lantern":
                inventory_sprites[-1].state = "unlit"
            else:
                inventory_sprites[-1].state = "default"

            for envitem in environment_sprites:
                if envitem.type == item:
                    removeEnvironmentItem(item= envitem)
                    break

            repositionInventoryItems()

            inventory_SM.redraw(0)
            environment_SM.redraw(0)
            renpy.restart_interaction()

    def removeEnvironmentItem(item):
        item.destroy()
        environment_sprites.pop(environment_sprites.index(item))
        environment_items.pop(environment_items.index(item.type))

    def removeInventoryItem(item):
        item.destroy()
        inventory_sprites.pop(inventory_sprites.index(item))
        inventory_items.pop(inventory_items.index(item.type))
        repositionInventoryItems()

    def setItemVisibility(item, visible):
        if visible == False:
            item.visible = False
            t = Transform(child = item.item_image, zoom = 0.75, alpha = 0)
            item.set_child(t)
        else:
            item.visible = True
            t = Transform(child = item.item_image, zoom = 0.75, alpha = 100)
            item.set_child(t)
        inventory_SM.redraw(0)

    def prepareLoad():
        global dialogue
        global inventory_drag
        for item in inventory_sprites:
            if item_dragged == item.type:
                item.x = item.original_x
                item.y = item.original_y
                item.zorder = 0
        dialogue = {}
        inventory_drag = False
        renpy.hide_screen("characterSay")

screen UI:
    zorder 1
    image "UI/inventory-icon-bg.png" xpos 0 ypos 0.8 at test
    imagebutton auto "UI/inventory-icon-%s.png" action If(renpy.get_screen("inventory") == None, true= Show("inventory"), false= Hide("inventory")) xpos 0.03 ypos 0.825 at test
    add environment_SM
screen inventory:
    zorder 3
    image "UI/inventory-bg.png" xpos 0.17 ypos 0.8 at test
    image "UI/inventory-slots.png" xpos 0.274 ypos 0.845 at test

    add inventory_SM
transform test:
    zoom 0.75
screen inventoryItemMenu(item):
    zorder 7
    frame:
        xysize (inventory_slot_size[0], inventory_slot_size[1])
        background "#FFFFFF30"
        xpos item.x
        ypos item.y
        imagebutton auto "UI/view-inventory-item-%s.png" align (0.0, 0.5) at half_size action [Show("inspectItem", items = [item.type]), Hide("inventoryItemMenu")]
        imagebutton auto "UI/use-inventory-item-%s.png" align (1.0, 0.5) at half_size action [Function(startDrag, item = item), Hide("inventoryItemMenu")]

screen inspectItem(items):
    modal True
    zorder 4
    if items[0] == "thumbpiano" and firsttime2 == False:
        timer .2 repeat False action ShowMenu("pianolabel", transition = None)
    elif items[0] == "musicbox" and firsttime1 == False:
        timer .2 repeat False action ShowMenu("musiclabel", transition = None)
    elif items[0] == "plantjournal" and firsttime3 == False:
        timer .2 repeat False action ShowMenu("plantlabel", transition = None)
    else:

        button:
            xfill True
            yfill True
            action [If(len(items) > 1, true = RemoveFromSet(items, items[0]), false= [Hide("inspectItem"), If(len(dialogue) > 0, true= Show("characterSay"), false= NullAction())]), If(firsttime1 == True, true = SetVariable("firsttime1", False), false= If(firsttime2 == True, true = SetVariable("firsttime2", False), false= SetVariable("firsttime3", False))), If(items[0] == "plantjournal", true= ShowMenu("act2puzzle3", transition= fade), false= None)]
            image "Items Pop Up/items-pop-up-bg.png" align (0.5, 0.5) at half_size

            python:
                item_name = ""
                for name in inventory_item_names:
                    temp_name = name.replace(" ", "-")
                    if temp_name.lower() == items[0]:
                        item_name = name

            text "{}".format(item_name) size 20 align (0.5, 0.25) color "#000000"
            image "Items Pop Up/{}-pop-up.png".format(items[0]) align (0.5, 0.5) at half_size


screen characterSay(who = None, what = None):
    modal True
    zorder 6
    style_prefix "say"

    window:
        id "window"
        window:
            padding (20, 20)
            id "namebox"
            style "namebox"
            if who is not None:
                text who id "who"
            else:
                text dialogue["who"]    

        if what is not None:
            text what id "what" xpos 0.25 ypos 0.4 xanchor 0.0
        else:
            text dialogue["what"][0] xpos 0.25 ypos 0.4 xanchor 0.0

    button:
        xfill True
        yfill True
        if what is None:
            action If(len(dialogue["what"]) > 1, true= RemoveFromSet(dialogue["what"], dialogue["what"][0]), false= [Hide("characterSay"), SetVariable("dialogue", {})])
        else:
            action Return(True)


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

transform half_size:
    zoom 0.75


#    return
 
