init python:
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
image slider_animated:
    "slider/03.jpg"
    pause .1
    "slider/04.jpg"
    pause .1
    "slider/05.jpg"
    pause .1
    "slider/06.jpg"
    pause .1
    "slider/07.jpg"
    pause .1
    repeat


default slider_1  = slider_class(3, 3, 128)
default slider_2  = slider_class(5, 4, 128, "slider/01.jpg")
default slider_3  = slider_class(2, 3, 256, "slider/02.jpg")
default slider_4  = slider_class(4, 4, 128, "slider_animated")
screen slider(g = slider_3):
    modal True
    style_prefix "slider"
    default shuffle = 1
    default cheating = 0
    # frame:
    #     align 0.0,0.0
    #     has vbox
    #     text "{}".format(g.missing)
    #     text "{}".format(g.win)
    #     text "{}".format(g.pieces)

    frame:
        xysize (g.columns*g.size)+40,(g.rows*g.size)+40
        background "#fff9"
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
                        text str(ii)
                    if cheating:
                        action Function(g.cheat, ii)
                    else:
                        action Function(g.slide, ii)

    if shuffle:
        timer .2 repeat True action Function(g.shuffle)
        button:
            yalign .9
            text "Start"
            action SetScreenVariable("shuffle", 0)
    elif g.win == g.pieces:
        button:
            yalign .9
            text "Proceed"
            action Return()
    else:
        hbox:
            yalign .9
            button:
                text "Shuffle"
                action Function(g.shuffle)
            button:
                text "Give up"
                action Return()
            button:
                text "Enable Cheating"
                action ToggleScreenVariable("cheating", 1, 0)

transform slider_piece(x, y):
    ease .2 xpos x ypos y
transform slider_image:
    alpha 0
    pause .4
    ease .2 alpha 1
style slider_text:
    size 30


label start:
    window hide
    show screen slider(slider_1)
    pause
    hide screen slider
    show screen slider(slider_2)
    pause
    hide screen slider
    show screen slider(slider_3)
    pause
    hide screen slider
    show screen slider(slider_4)
    pause
    hide screen slider
