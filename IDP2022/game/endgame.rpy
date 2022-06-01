image audrey black = "/audrey/audreyBlack.png"
image bg lastfloor = "/backgrounds/TowerLastFloor.png"
define m = Character("???")
define bookpage = 1
define spell = 1
define died = False
define lives = 3
define doingSomething = False 
image audrey hacked = "/audrey/audreyhacked.png"
image audrey hacked2 = "/audrey/audreyhacked2.png"
image audrey hacked3 = "/audrey/audreyhacked3.png"
label endgame:
    scene bg lastfloor
    show audrey black with fade
    m "..."
    m "Haha.... You're so slow."
    mc "Who's there?"
    show audrey evil at truecenter
    a "First you forget about Jeremy and now me?"
    show audrey mad 
    a "You must be thinking you're play some kind of game now?!"
    hide audrey mad
    show audrey hacked
    $renpy.pause(delay=0.1, hard = True) 
    hide audrey hacked
    show audrey hacked2
    $renpy.pause(delay=0.1, hard = True) 
    hide audrey hacked2  
    show audrey hacked3
    $renpy.pause(delay=0.1, hard = True) 
    show audrey evil
    a "You've gotten so far. This isn't supposed to happen."
    a "You won't leave this game."
    mc "Are you the hacker that locked me in here or something?"
    a "Too bad, you will never understand. Say goodbye to that damned company and your life."
    hide audrey hacked3
    company "The hacker is about to code something that can kill you! Hit the incoming blows to block them."
    company "We've handed a spellbook to you that should be in your inventory."
    company "Use the 3 spells that we tell you to use to defeat the hacker and beat the game safely."
    company "Due to a firewall placed by the hacker we can't  say the exact name of the spells you must use."
    company "But we can tell you through hints and clues..."
    company "Be careful, using the wrong spell might backfire and injure you. Take too much damage and you might die."
    show screen bookUI
    show screen health
    show screen hints
    jump endgamesetup

label endgamesetup:
 
    if died == True:
        scene bg lastfloor with eyeopen
        "..."
        "I'm back here again..."
        show audrey evil with fade
        $renpy.pause(delay=2, hard= True)
        mc "Yeah, whatever you're the hacker."
        a "You've gotten so f- ..."
        a "How did you know already.."
        a "It doesn't matter."
        a "Die."
        hide audrey evil
        "Seems like I have to do the same thing...."
        window hide
        $died = False
    show audrey evil
    show screen bookUI
    show screen health
    show screen hints
    show audrey evil 
    $ cont = 0 #continue variable
    $ arr_keys = ["a", "c", "e", "K_UP", "K_SPACE"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys
    if doingSomething == False:
            show screen health
            $renpy.pause(delay= 5, hard = True)
            $renpy.play("audio/warn.mp3", channel = None)
            call qte_setup(1.5, 1.5, 0.1, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    while cont == 1:
        show screen health
        if doingSomething == False:
                $renpy.pause(delay= renpy.random.randint(3, 7), hard = True)
                $renpy.play("audio/warn.mp3", channel = None)
                call qte_setup(1.5, 1.5, 0.1, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        # to repeat the qte events until it is missed
    if doingSomething == False:
        $lives = lives - 1
        if lives == 0:
            hide screen lives
            hide screen doorUI
            hide screen hints 
            $died = True
            $lives = 3
            $renpy.restart_interaction()
            scene bg blackScreen with eyeclose
            $renpy.pause(delay=3, hard= True)
            jump endgamesetup
        else:
            $renpy.restart_interaction()
            show screen health
            jump endgamesetup
        $renpy.restart_interaction()
        show screen health
        jump endgamesetup
        return 
label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_button
    # can change to "call screen qte_button" to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return
screen qte_button:
    #button press qte

    button:
        action NullAction()
        align 0.5, 0.5
        background "/backgrounds/TowerLastFloor.png"
    add "/audrey/audreyEvilLaugh.png" xalign 0.5
    add "/endgame/health{}.png".format(lives) 

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])
    #see above



    vbox:
        xalign x_align yalign y_align spacing 25

        imagebutton:
            action Return(1)
            xalign 0.5
            yalign 0.5
            xysize 250,250
            idle Animation("/endgame/spell1.png", 0.25, "/endgame/spell2.png", 0.25, "/endgame/spell3.png", 0.25) #change to image, etc
            #same function as the key input


        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
screen hints():
    add "/endgame/hint{}.png".format(spell)
screen lives():
     add "/endgame/health{}.png".format(lives) 
screen bookUI():
    imagebutton:
        focus_mask True
        idle "/Inventory Items/inventory-book.png"
        xpos 29
        ypos 862
        action [Show("spellbook"), Hide("bookUI")] 
screen health:
    add "/endgame/health{}.png".format(lives)
screen spellbook():
    $global currentscreen
    add "/spellbook pages/bookpage{}.png".format(bookpage) xalign 0.5 yalign 0.5
    
    imagebutton:
        focus_mask True 
        idle "/UI/exitui.png"
        xpos 367
        ypos -83
        action [Hide("spellbook", transition= None), Show("bookUI")]
    imagebutton auto "/UI/rightarrow-%s.png":
        focus_mask True
        xpos 1678
        ypos 465     
        action [SetVariable("bookpage", If(bookpage == 13, true= 13, false= bookpage + 1)), Function(refresh)]
    imagebutton auto "/UI/leftarrow-%s.png":
        focus_mask True 
        xpos 107
        ypos 462
        action [SetVariable("bookpage", If(bookpage == 1, true= 1, false= bookpage - 1)), Function(refresh)]
    showif spell == 1 and bookpage != 10:
        button:
            xpos 434
            ypos 169
            xsize 1049
            ysize 705
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
    showif spell == 2 and bookpage == 4:
        button:
            xpos 434
            ypos 382
            xsize 399
            ysize 167
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("audreyInjured", transition = fade)]
        button:
            xpos 416
            ypos 188
            xsize 1094
            ysize 189
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
        button:
            xpos 413
            ypos 600
            xsize 1094
            ysize 189
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
                                           
    showif spell == 1 and bookpage == 10:
        button:
            xpos 966
            ypos 190
            xsize 541
            ysize 364
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]            
        button:
            xpos 423
            ypos 201
            xsize 503
            ysize 618
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
        button:
            xpos 979
            ypos 571
            xsize 525
            ysize 290
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("audreyInjured", transition = fade)]
    showif spell == 2 and bookpage != 4:
        button:
            xpos 434
            ypos 169
            xsize 1049
            ysize 705
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
    showif spell == 3 and bookpage != 2:
        button:
            xpos 434
            ypos 169
            xsize 1049
            ysize 705
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
    showif spell == 3 and bookpage == 2:
        button:
            xpos 434
            ypos 382
            xsize 399
            ysize 167
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("audreyInjured", transition = fade)]
        button:
            xpos 416
            ypos 188
            xsize 1094
            ysize 189
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
        button:
            xpos 413
            ypos 600
            xsize 1094
            ysize 189
            action [Hide("spellbook"), SetVariable("doingSomething", True), ShowMenu("gotSpellWrong", transition= None)]
    

init python:
    def addbook():
        addToInventory(["book"])
        inventory_SM.redraw(0)
        environment_SM.redraw(0)
        renpy.restart_interaction()

