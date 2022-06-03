# NEED ACT EMDS 
# NEEDS TESTING

define e = Character("Emily")
init python:
    import time

    hintUsed = 0
    timer_jump = 0
    timer_range = 0
    time = 0
    minutes = 0
    seconds = 0
    final_minutes = 0
    final_seconds = 0
    def countdown(st, at, length=0.0):
        global time
        global minutes
        global seconds
        minutes = time // 60
        seconds = time % 60
        for i in range(10):
            if seconds == i:
                seconds = str("0" + str(i))
        
        return Text(str(str(minutes) + ":" + str(seconds)), color="#fff", size=48), .1
    def time_finish(st, at, length=0.0):
        global time
        global minutes
        global seconds
        global final_minutes
        global final_seconds
        final_minutes = minutes
        final_seconds = seconds
        return Text(str(str(final_minutes) + ":" + str(final_seconds)), color="#fff", size=48), .1

screen countdown():
    timer 1 repeat True action If(time >= 0, true = SetVariable("time", time + 1), false = [Hide("countdown"), Jump(timer_jump)])
    imagebutton:
        xpos 50
        ypos 50
        idle DynamicDisplayable(countdown, length = 0)
        hover DynamicDisplayable(countdown, length = 0)
        action Null

screen time_finish():
    imagebutton:
        xpos 50
        ypos 50
        idle DynamicDisplayable(time_finish, length = 0)
        hover DynamicDisplayable(time_finish, length = 0)
        action Null

label timer_start:
    $ global time
    $ time = 0
    $ timer_range = 0
    $ timer_jump = "lose"
    show screen countdown
    jump firstAct




label start:
    

    #jump timer_start


    #$ starting_time1()

    e "Hello!"
    
    $ renpy.input("HUH1")
    jump timer_start
    #$ ending_time1()
    label firstAct:
        
        # ENDING
        $ act1_time = time
        $ act1_minutes = minutes
        $ act1_seconds = seconds
        $ act1_time_string = str(str(act1_minutes) + ":" + str(act1_seconds))

    $ renpy.input("HUH2")
    label secondAct: 

        $ act2_time = time
        $ act2_minutes = minutes
        $ act2_seconds = seconds
        $ act2_time_string = str(str(act2_minutes) + ":" + str(act2_seconds))

    $ renpy.input("HUH3")
    label thirdAct:
        $ act3_time = time
        $ act3_minutes = minutes
        $ act3_seconds = seconds
        $ act3_time_string = str(str(act3_minutes) + ":" + str(act3_seconds))
    $ renpy.input("HUH4")
    label endGame:
        $ act4_time = time
        $ act4_minutes = minutes
        $ act4_seconds = seconds
        $ act4_time_string = str(str(act4_minutes) + ":" + str(act4_seconds))
    $ renpy.input("HUH5")
    label epilogue:
        $ final_seconds = seconds
        $ final_minutes = minutes
    # change variable
    #$ renpy.notify(totalAct1Time)

    #show screen time_finish()
    #$ getTotalTime()

    python:
        import requests

        URL = "https://script.google.com/macros/s/AKfycbxmTCKt-S3ux72ZFPvVaJDOJQRb7iEjHSFhDp2CYb6UgxgS1uly/exec"
        name = "conners"
        totalTime = "90"
        hRate = "80"
        currentHrate = "90"
        rating = "5"
        enjoyment = "5"
        likedMost = "puzzle"
        recommend = "yes"
        act1Time = act1_time_string
        act2Time = act2_time_string
        act3Time = act3_time_string
        endGameTime = act4_time_string
        totalTime = str(str(final_minutes) + ":" + str(final_seconds))
        # Finaltimeseconds = (int(final_minutes) * 60) + int(final_seconds)

        #requests.post(URL, json={'totalTime' : totalTime, 'username' : name, 'heartRateBefore' : hRate, 'heartRateAfter' : currentHrate,'act1Time' :  act1Time, 'act2Time' : act2Time, 'act3Time' : act3Time, 'endGameTime' : endGameTime, 'rating' : rating, 'enjoyment' : enjoyment, 'likedMost' : likedMost, 'recommend' : recommend, 'FinalTime' : FinalTime}, timeout=5)
    
    # jump leaderboard




label leaderboard:
    $ lb1 = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vTac-e8kK_vcXTVWUdi6zw3UjdFl86QrT3JFeZfQVzLmQeM-bdhtbMwcBmGxojIToDNI-Jj_7SPyTXA/pub?gid=57334158&single=true&output=csv")
    $ lb2 = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vTac-e8kK_vcXTVWUdi6zw3UjdFl86QrT3JFeZfQVzLmQeM-bdhtbMwcBmGxojIToDNI-Jj_7SPyTXA/pub?gid=423134835&single=true&output=csv")
    show screen leaderboard
    hide screen countdown
    "Leaderboard:"

    return

screen leaderboard():
    vbox:
        xpos 0.5
        ypos 0.5
        text ("{color=#fff}{size=30}[lb1.text]{/size}{/color}")
    vbox:
        xpos 50
        ypos 50
        text ("{color=#fff}{size=30}[lb2.text]{/size}{/color}")


return