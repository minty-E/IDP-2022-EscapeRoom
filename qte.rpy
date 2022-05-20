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

        button:
            action Return(1)
            xalign 0.5
            xysize 100, 100
            background Animation("#000", 0.5, "#fff", 0.5) #change to image, etc
            activate_sound "sounds/hit.mp3"
            #same function as the key input


        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"