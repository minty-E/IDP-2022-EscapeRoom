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
    $ time = 0
    $ timer_range = 0
    $ timer_jump = "lose"
    show screen countdown
    jump prologue2


       """
    def time_convert(sec):
        sec += (hintUsed * 10)
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        #global totalTime 
        # NEED TO RUN TIME ELAPSED FOR EACH STARTING TIME
        totalActTime = ("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))

    def starting_time1():
        global start_time1 
        start_time1 = time.time()
    def starting_time2():
        global start_time2 
        start_time2 = time.time()
    def starting_time3():
        global start_time3 
        start_time3 = time.time()

    def ending_time1():
        end_time1 = time.time()
        time_lapsed1 = end_time1 - start_time1
        global totalAct1Time
        totalAct1Time = time_convert(time_lapsed1)
    def ending_time2():
        end_time2 = time.time()
        time_lapsed2 = end_time2 - start_time2
        global totalAct2Time
        totalAct2Time = time_convert(time_lapsed2)
    def ending_time3():
        end_time3 = time.time()
        time_lapsed3 = end_time3 - start_time3
        global totalAct3Time
        totalAct3Time = time_convert(time_lapsed3)
    def getTotalTime():
        global totalTime
        totalTime = totalAct1Time + totalAct2Time + totalAct3Time"""