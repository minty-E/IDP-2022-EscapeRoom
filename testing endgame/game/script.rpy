define page = 1
label start:
    scene transparent
    $ cont = 0 #continue variable
    $ arr_keys = ["a", "c", "e", "K_UP", "K_SPACE"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys

    call qte_setup(5, 5, 0.1, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    while cont == 1:
        $renpy.pause(delay= 1, hard = True)
        call qte_setup(5, 5, 0.1, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        # to repeat the qte events until it is missed

    "{b}GAME OVER{/b}"

    return



init python:
    def refresh():  
        renpy.restart_interaction()
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
        action Return(0) #miss
        align 0.5, 0.5
        background "images/transparent.png"
        #to add a click sensor *outside* of button (if player presses outside button area) and return false


    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])
    #see above

    vbox:
        xalign x_align yalign y_align spacing 25

        imagebutton:
            action Return(1)
            xalign 0.5
            yalign 0.5
            xysize 250,250
            idle Animation("spell1.png", 0.25, "spell2.png", 0.25, "spell3.png", 0.25) #change to image, etc
            #same function as the key input


        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"


screen spellbook():
    $global currentscreen
    add "/bookpage{}.png".format(page) xalign 0.5 yalign 0.5
    imagebutton:
        focus_mask True 
        idle "/exitui.png"
        xpos 367
        ypos -83
        action Hide("spellbook", transition= None)
    imagebutton auto "/rightarrow-%s.png":
        focus_mask True     
        action [SetVariable("page", If(page == 3, true= 3, false= page + 1)), Function(refresh)]
    imagebutton auto "/leftarrow-%s.png":
        focus_mask True 
        xpos 107
        ypos 462
        action [SetVariable("page", If(page == 1, true= 1, false= page - 1)), Function(refresh)]


