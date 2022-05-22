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


# slider_class(3,3,210) means 3 rows, 3 columns, size is 210
default slider_1  = slider_class(3, 3, 205)
screen slider(g = slider_1):
    modal True
    style_prefix "slider"
    default shuffle = 1
    default cheating = 0

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
                        image "images/{}.png".format(ii)
                    if cheating:
                        action Function(g.cheat, ii)
                    else:
                        action Function(g.slide, ii)

# this shuffles the thing idk how you can make it happen off screen
    if shuffle:
        timer .2 repeat False action Function(g.shuffle)
        button:
            yalign .9
            text "Start"
            action Return()
    elif g.win == g.pieces:
        button:
            yalign .9
            text "Proceed"
            # change action to mirror turn and user saying smth idk
            action Return()

transform slider_piece(x, y):
    ease .2 xpos x ypos y
transform slider_image:
    alpha 0
    pause .4
    ease .2 alpha 1
style slider_text:
    size 30
# make sure to add wall background. phong has it i think
screen pedestal:
    add "pedestal1.png"
    modal True

label start:
    window hide
    show screen pedestal
    scene pedestal1
    show screen slider(slider_1)
    pause
