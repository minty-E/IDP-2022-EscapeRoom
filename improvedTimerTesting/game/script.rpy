init python:
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




define e = Character("Eileen")


# The game starts here.

label start:
    show screen countdown()
   

    scene bg room
    label startTime:
        show screen time_finish()

    label stopTime:
        show screen 

    

    show eileen happy

   
    return
