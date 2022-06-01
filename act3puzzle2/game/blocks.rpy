
define e = Character("Eileen")
define taken1 = False
define taken2 = False
define taken3 = False
define taken4 = False
define spot1 = ""
define spot2 = ""
define spot3 = ""
define spot4 = ""
define Aspot = 0
define Avisible = True
define Abutton = False


define Bspot = 0
define Bbutton = False
define Bvisible = True


define Cbutton = False
define Cspot = 0
define Cvisible = True


define Dspot = 0
define Dbutton = False
define Dvisible = True


define Espot = 0
define Ebutton = False
define Evisible = True

define E2spot = 0
define E2button = False
define E2visible = True

define Fspot = 0
define Fbutton = False
define Fvisible = True

define Gspot = 0
define Gvisible = True
define Gbutton = False

define Hspot = 0
define Hvisible = True
define Hbutton = False
define Ispot = 0
define Ibutton = False
define Ivisible = True

define Jspot = 0
define Jbutton = False
define Jvisible = True
define Kspot = 0
define Kbutton = False
define Kvisible = True
define Lspot = 0
define Lbutton = False
define Lvisible = True
define Mspot = 0
define Mbutton = False
define Mvisible = True
define Nspot = 0
define Nbutton = False
define Nvisible = True
define Ospot = 0
define Obutton = False
define Ovisible = True
define Pspot = 0
define Pbutton = False
define Pvisible = True
define Rspot = 0
define Rbutton = False
define Rvisible = True
define Sspot = 0
define Sbutton = False
define Svisible = True
define Tspot = 0
define Tbutton = False
define Tvisible = True
define Uspot = 0
define Ubutton = False
define Uvisible = True

label start:
    scene tower
    e "move blocks"
    call screen blocks()


init python:
    spot = 0
    def refresh():
        renpy.restart_interaction()
    def checkblocks():
        if Tspot == 1 and Rspot == 2 and Espot == 3 and E2spot == 4 or Tspot == 1 and Rspot == 2 and E2spot == 3 and Espot == 4:
                renpy.say(e, "OMG YAS SLAY")
    def blockdrag(drags, drop):
        global taken1
        global taken2
        global taken3
        global taken4
        Ax = 1688
        Ay =856
        global Avisible
        global Abutton
        global Aspot
        Bx = 0
        By = 820
        global Bbutton
        global Bvisible
        global Bspot
        Cx = 215
        Cy = 834
        global Cbutton
        global Cvisible
        global Cspot
        Dx = 382
        Dy = 719
        global Dbutton
        global Dvisible
        global Dspot
        E2x = 0
        E2y = 703
        global E2button
        global E2visible
        global E2spot
        Ex = 1513
        Ey = 865
        global Ebutton
        global Evisible
        global Espot
        Fx = 494
        Fy = 720
        global Fbutton
        global Fvisible
        global Fspot
        Gx = 1478
        Gy = 758
        global Gbutton
        global Gvisible
        global Gspot
        Hx = 603
        Hy = 724
        global Hbutton
        global Hvisible
        global Hspot
        Ix = 855
        Iy = 880
        global Ibutton
        global Ivisible
        global Ispot
        Jx = 448
        Jy = 623
        global Jbutton
        global Jvisible
        global Jspot
        Kx = 552
        Ky = 620
        global Kbutton
        global Kvisible
        global Kspot
        Lx = 1283
        Ly = 662
        global Lbutton
        global Lvisible
        global Lspot
        Mx = 133
        My = 703
        global Mbutton
        global Mvisible
        global Mspot
        Nx = 1361
        Ny = 756
        global Nbutton
        global Nvisible
        global Nspot
        Ox = 426
        Oy = 849
        global Obutton
        global Ovisible
        global Ospot
        Px = 1193
        Py = 667
        global Pbutton
        global Pvisible
        global Pspot
        Rx = 925
        Ry = 699
        global Rbutton
        global Rvisible
        global Rspot
        Sx = 1110
        Sy = 859
        global Sbutton
        global Svisible
        global Sspot
        Tx = 821
        Ty = 701
        global Tbutton
        global Tvisible
        global Tspot
        Ux = 1240
        Uy = 567
        global Ubutton
        global Uvisible
        global Uspot
        global spot1
        global spot2
        global spot3
        global spot4
        # put each latter in if taken_
        if drop:
            if taken1 == False and drop.drag_name == "1":
                if drags[0].drag_name == "A":
                    drags[0].snap(Ax,Ay)
                    Aspot = 1
                    Avisible = False
                    Abutton = True
                    spot1 = "A"
                elif drags[0].drag_name == "B":
                    drags[0].snap(Bx,By)
                    Bspot = 1
                    Bvisible = False
                    Bbutton = True
                elif drags[0].drag_name == "C":
                    drags[0].snap(Cx,Cy)
                    Cspot = 1
                    Cvisible = False
                    Cbutton = True
                    spot1 = "C"
                elif drags[0].drag_name == "D":
                    drags[0].snap(Dx,Dy)
                    letter = "D"
                    Dspot = 1
                    Dvisible = False
                    Dbutton = True
                    spot1 = "D"
                elif drags[0].drag_name == "E":
                    drags[0].snap(Ex,Ey)
                    Espot = 1
                    Evisible = False
                    Ebutton = True
                    spot1 = "E"

                elif drags[0].drag_name == "E2":
                    drags[0].snap(E2x,E2y)
                    E2spot = 1
                    E2visible = False
                    E2button = True

                elif drags[0].drag_name == "F":
                    drags[0].snap(Fx,Fy)
                    Fspot = 1
                    Fvisible = False
                    Fbutton = True
                    spot1 = "F"
                elif drags[0].drag_name == "G":
                    drags[0].snap(Gx,Gy)
                    Gspot = 1
                    Gvisible = False
                    Gbutton = True
                    spot1 = "G"
                elif drags[0].drag_name == "H":
                    drags[0].snap(Hx,Hy)
                    Hspot = 1
                    Hvisible = False
                    Hbutton = True
                    spot1 = "H"
                elif drags[0].drag_name == "I":
                    drags[0].snap(Ix,Iy)
                    Ispot = 1
                    Ivisible = False
                    Ibutton = True
                    spot1 = "I"
                elif drags[0].drag_name == "J":
                    drags[0].snap(Jx,Jy)
                    Jspot = 1
                    Jvisible = False
                    Jbutton = True
                elif drags[0].drag_name == "K":
                    drags[0].snap(Kx,Ky)
                    Kspot = 1
                    Kvisible = False
                    Kbutton = True
                    spot1 = "K"
                elif drags[0].drag_name == "L":
                    drags[0].snap(Lx,Ly)
                    Lspot = 1
                    Lvisible = False
                    Lbutton = True
                    spot1 = "L"
                elif drags[0].drag_name == "M":
                    drags[0].snap(Mx,My)
                    Mspot = 1
                    Mvisible = False
                    Mbutton = True
                    spot1 = "M"
                elif drags[0].drag_name == "N":
                    drags[0].snap(Nx,Ny)
                    Nspot = 1
                    Nvisible = False
                    Nbutton = True
                    spot1 = "N"
                elif drags[0].drag_name == "O":
                    drags[0].snap(Ox,Oy)
                    Ospot = 1
                    Ovisible = False
                    Obutton = True
                    spot1 = "O"
                elif drags[0].drag_name == "P":
                    drags[0].snap(Px,Py)
                    Pspot = 1
                    Pvisible = False
                    Pbutton = True
                    spot1 = "P"
                elif drags[0].drag_name == "R":
                    drags[0].snap(Rx,Ry)
                    Rspot = 1
                    Rvisible = False
                    Rbutton = True
                    spot1 = "R"
                elif drags[0].drag_name == "S":
                    drags[0].snap(Sx,Sy)
                    Sspot = 1
                    Svisible = False
                    Sbutton = True
                    spot1 = "S"
                elif drags[0].drag_name == "T":
                    drags[0].snap(Tx,Ty)
                    Tspot = 1
                    Tvisible = False
                    Tbutton = True
                    spot1 = "T"
                elif drags[0].drag_name == "U":
                    drags[0].snap(Ux,Uy)
                    Uspot = 1
                    Uvisible = False
                    Ubutton = True
                    spot1 = "U"
                taken1 = True
            if taken2 == False and drop.drag_name == "2":
                if drags[0].drag_name == "A":
                    drags[0].snap(Ax,Ay)
                    Aspot = 2
                    Avisible = False
                    Abutton = True
                    spot2 = "A"
                elif drags[0].drag_name == "B":
                    drags[0].snap(Bx,By)
                    Bspot = 2
                    Bvisible = False
                    Bbutton = True
                    spot2 = "B"
                elif drags[0].drag_name == "C":
                    drags[0].snap(Cx,Cy)
                    Cspot = 2
                    Cvisible = False
                    Cbutton = True
                    spot2 = "C"
                elif drags[0].drag_name == "D":
                    drags[0].snap(Dx,Dy)
                    Dspot = 2
                    Dvisible = False
                    Dbutton = True
                elif drags[0].drag_name == "E":
                    drags[0].snap(Ex,Ey)
                    Espot = 2
                    Evisible = False
                    Ebutton = True
                elif drags[0].drag_name == "E2":
                    drags[0].snap(E2x,E2y)
                    E2spot = 2
                    E2visible = False
                    E2button = True

                elif drags[0].drag_name == "F":
                    drags[0].snap(Fx,Fy)
                    Fspot = 2
                    Fvisible = False
                    Fbutton = True
                elif drags[0].drag_name == "G":
                    drags[0].snap(Gx,Gy)
                    Gspot = 2
                    Gvisible = False
                    Gbutton = True
                elif drags[0].drag_name == "H":
                    drags[0].snap(Hx,Hy)
                    Hspot = 2
                    Hvisible = False
                    Hbutton = True
                elif drags[0].drag_name == "I":
                    drags[0].snap(Ix,Iy)
                    Ispot = 2
                    Ivisible = False
                    Ibutton = True
                elif drags[0].drag_name == "J":
                    drags[0].snap(Jx,Jy)
                    Jspot = 2
                    Jvisible = False
                    Jbutton = True
                elif drags[0].drag_name == "K":
                    drags[0].snap(Kx,Ky)
                    Kspot = 2
                    Kvisible = False
                    Kbutton = True
                elif drags[0].drag_name == "L":
                    drags[0].snap(Lx,Ly)
                    Lspot = 2
                    Lvisible = False
                    Lbutton = True
                elif drags[0].drag_name == "M":
                    drags[0].snap(Mx,My)
                    Mspot = 2
                    Mvisible = False
                    Mbutton = True
                elif drags[0].drag_name == "N":
                    drags[0].snap(Nx,Ny)
                    Nspot = 2
                    Nvisible = False
                    Nbutton = True
                elif drags[0].drag_name == "O":
                    drags[0].snap(Ox,Oy)
                    Ospot = 2
                    Ovisible = False
                    Obutton = True
                elif drags[0].drag_name == "P":
                    drags[0].snap(Px,Py)
                    Pspot = 2
                    Pvisible = False
                    Pbutton = True
                elif drags[0].drag_name == "R":
                    drags[0].snap(Rx,Ry)
                    Rspot = 2
                    Rvisible = False
                    Rbutton = True
                elif drags[0].drag_name == "S":
                    drags[0].snap(Sx,Sy)
                    Sspot = 2
                    Svisible = False
                    Sbutton = True
                elif drags[0].drag_name == "T":
                    drags[0].snap(Tx,Ty)
                    Tspot = 2
                    Tvisible = False
                    Tbutton = True
                elif drags[0].drag_name == "U":
                    drags[0].snap(Ux,Uy)
                    Uspot = 2
                    Uvisible = False
                    Ubutton = True
                taken2 = True
            if taken3 == False and drop.drag_name == "3":
                if drags[0].drag_name == "A":
                    drags[0].snap(Ax,Ay)
                    Aspot = 3
                    Avisible = False
                    Abutton = True
                elif drags[0].drag_name == "B":
                    drags[0].snap(Bx,By)
                    Bspot = 3
                    Bvisible = False
                    Bbutton = True
                elif drags[0].drag_name == "C":
                    drags[0].snap(Cx,Cy)
                    Cspot = 3
                    Cvisible = False
                    Cbutton = True
                elif drags[0].drag_name == "D":
                    drags[0].snap(Dx,Dy)
                    letter = "D"
                    Dspot = 3
                    Dvisible = False
                    Dbutton = True
                elif drags[0].drag_name == "E":
                    drags[0].snap(Ex,Ey)
                    Espot = 3
                    Evisible = False
                    Ebutton = True
                elif drags[0].drag_name == "E2":
                    drags[0].snap(E2x,E2y)
                    E2spot = 3
                    E2visible = False
                    E2button = True

                elif drags[0].drag_name == "F":
                    drags[0].snap(Fx,Fy)
                    Fspot = 3
                    Fvisible = False
                    Fbutton = True
                elif drags[0].drag_name == "G":
                    drags[0].snap(Gx,Gy)
                    Gspot = 3
                    Gvisible = False
                    Gbutton = True
                elif drags[0].drag_name == "H":
                    drags[0].snap(Hx,Hy)
                    Hspot = 3
                    Hvisible = False
                    Hbutton = True
                elif drags[0].drag_name == "I":
                    drags[0].snap(Ix,Iy)
                    Ispot = 3
                    Ivisible = False
                    Ibutton = True
                elif drags[0].drag_name == "J":
                    drags[0].snap(Jx,Jy)
                    Jspot = 3
                    Jvisible = False
                    Jbutton = True
                elif drags[0].drag_name == "K":
                    drags[0].snap(Kx,Ky)
                    Kspot = 3
                    Kvisible = False
                    Kbutton = True
                elif drags[0].drag_name == "L":
                    drags[0].snap(Lx,Ly)
                    Lspot = 3
                    Lvisible = False
                    Lbutton = True
                elif drags[0].drag_name == "M":
                    drags[0].snap(Mx,My)
                    Mspot = 3
                    Mvisible = False
                    Mbutton = True
                elif drags[0].drag_name == "N":
                    drags[0].snap(Nx,Ny)
                    Nspot = 3
                    Nvisible = False
                    Nbutton = True
                elif drags[0].drag_name == "O":
                    drags[0].snap(Ox,Oy)
                    Ospot = 3
                    Ovisible = False
                    Obutton = True
                elif drags[0].drag_name == "P":
                    drags[0].snap(Px,Py)
                    Pspot = 3
                    Pvisible = False
                    Pbutton = True
                elif drags[0].drag_name == "R":
                    drags[0].snap(Rx,Ry)
                    Rspot = 3
                    Rvisible = False
                    Rbutton = True
                elif drags[0].drag_name == "S":
                    drags[0].snap(Sx,Sy)
                    Sspot = 3
                    Svisible = False
                    Sbutton = True
                elif drags[0].drag_name == "T":
                    drags[0].snap(Tx,Ty)
                    Tspot = 3
                    Tvisible = False
                    Tbutton = True
                elif drags[0].drag_name == "U":
                    drags[0].snap(Ux,Uy)
                    Uspot = 3
                    Uvisible = False
                    Ubutton = True
                taken3 = True
            if taken4 == False and drop.drag_name == "4":
                if drags[0].drag_name == "A":
                    drags[0].snap(Ax,Ay)
                    Aspot = 4
                    Avisible = False
                    Abutton = True
                elif drags[0].drag_name == "B":
                    drags[0].snap(Bx,By)
                    Bspot = 4
                    Bvisible = False
                    Bbutton = True
                elif drags[0].drag_name == "C":
                    drags[0].snap(Cx,Cy)
                    Cspot = 4
                    Cvisible = False
                    Cbutton = True
                elif drags[0].drag_name == "D":
                    drags[0].snap(Dx,Dy)
                    letter = "D"
                    Dspot = 4
                    Dvisible = False
                    Dbutton = True
                elif drags[0].drag_name == "E":
                    drags[0].snap(Ex,Ey)
                    Espot = 4
                    Evisible = False
                    Ebutton = True
                elif drags[0].drag_name == "E2":
                    drags[0].snap(E2x,E2y)
                    E2spot = 4
                    E2visible = False
                    E2button = True
                elif drags[0].drag_name == "F":
                    drags[0].snap(Fx,Fy)
                    Fspot = 4
                    Fvisible = False
                    Fbutton = True
                elif drags[0].drag_name == "G":
                    drags[0].snap(Gx,Gy)
                    Gspot = 4
                    Gvisible = False
                    Gbutton = True
                elif drags[0].drag_name == "H":
                    drags[0].snap(Hx,Hy)
                    Hspot = 4
                    Hvisible = False
                    Hbutton = True
                elif drags[0].drag_name == "I":
                    drags[0].snap(Ix,Iy)
                    Ispot = 4
                    Ivisible = False
                    Ibutton = True
                elif drags[0].drag_name == "J":
                    drags[0].snap(Jx,Jy)
                    Jspot = 4
                    Jvisible = False
                    Jbutton = True
                elif drags[0].drag_name == "K":
                    drags[0].snap(Kx,Ky)
                    Kspot = 4
                    Kvisible = False
                    Kbutton = True
                elif drags[0].drag_name == "L":
                    drags[0].snap(Lx,Ly)
                    Lspot = 4
                    Lvisible = False
                    Lbutton = True
                elif drags[0].drag_name == "M":
                    drags[0].snap(Mx,My)
                    Mspot = 4
                    Mvisible = False
                    Mbutton = True
                elif drags[0].drag_name == "N":
                    drags[0].snap(Nx,Ny)
                    Nspot = 4
                    Nvisible = False
                    Nbutton = True
                elif drags[0].drag_name == "O":
                    drags[0].snap(Ox,Oy)
                    Ospot = 4
                    Ovisible = False
                    Obutton = True
                elif drags[0].drag_name == "P":
                    drags[0].snap(Px,Py)
                    Pspot = 4
                    Pvisible = False
                    Pbutton = True
                elif drags[0].drag_name == "R":
                    drags[0].snap(Rx,Ry)
                    Rspot = 4
                    Rvisible = False
                    Rbutton = True
                elif drags[0].drag_name == "S":
                    drags[0].snap(Sx,Sy)
                    Sspot = 4
                    Svisible = False
                    Sbutton = True
                elif drags[0].drag_name == "T":
                    drags[0].snap(Tx,Ty)
                    Tspot = 4
                    Tvisible = False
                    Tbutton = True
                elif drags[0].drag_name == "U":
                    drags[0].snap(Ux,Uy)
                    Uspot = 4
                    Uvisible = False
                    Ubutton = True
                taken4 = True
            renpy.restart_interaction()

screen blocks:
    timer .2 repeat True action Function(checkblocks)
    showif Abutton == True:
        showif Aspot == 1:
            imagebutton:
                idle "Aspot1.png"
                focus_mask True
                action [SetVariable("Avisible", True), SetVariable("Abutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Aspot == 2:
            imagebutton:
                idle "Aspot2.png"
                focus_mask True
                action [SetVariable("Avisible", True), SetVariable("Abutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Aspot == 3:
            imagebutton:
                idle "Aspot3.png"
                focus_mask True
                action [SetVariable("Avisible", True), SetVariable("Abutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Aspot == 4:
            imagebutton:
                idle "Aspot4.png"
                focus_mask True
                action [SetVariable("Avisible", True), SetVariable("Abutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Bbutton == True:
        showif Bspot == 1:
            imagebutton:
                idle "Bspot1.png"
                focus_mask True
                action [SetVariable("Bvisible", True), SetVariable("Bbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Bspot == 2:
            imagebutton:
                idle "Bspot2.png"
                focus_mask True
                action [SetVariable("Bvisible", True), SetVariable("Bbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Bspot == 3:
            imagebutton:
                idle "Bspot3.png"
                focus_mask True
                action [SetVariable("Bvisible", True), SetVariable("Bbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Bspot == 4:
            imagebutton:
                idle "Bspot4.png"
                focus_mask True
                action [SetVariable("Bvisible", True), SetVariable("Bbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Cbutton == True:
        showif Cspot == 1:
            imagebutton:
                idle "Cspot1.png"
                focus_mask True
                action [SetVariable("Cvisible", True), SetVariable("Cbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Cspot == 2:
            imagebutton:
                idle "Cspot2.png"
                focus_mask True
                action [SetVariable("Cvisible", True), SetVariable("Cbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Cspot == 3:
            imagebutton:
                idle "Cspot3.png"
                focus_mask True
                action [SetVariable("Cvisible", True), SetVariable("Cbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Cspot == 4:
            imagebutton:
                idle "Cspot4.png"
                focus_mask True
                action [SetVariable("Cvisible", True), SetVariable("Cbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Dbutton == True:
        showif Dspot == 1:
            imagebutton:
                idle "Dspot1.png"
                focus_mask True
                action [SetVariable("Dvisible", True), SetVariable("Dbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Dspot == 2:
            imagebutton:
                idle "Dspot2.png"
                focus_mask True
                action [SetVariable("Dvisible", True), SetVariable("Dbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Dspot == 3:
            imagebutton:
                idle "Dspot3.png"
                focus_mask True
                action [SetVariable("Dvisible", True), SetVariable("Dbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Dspot == 4:
            imagebutton:
                idle "Dspot4.png"
                focus_mask True
                action [SetVariable("Dvisible", True), SetVariable("Dbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Ebutton == True:
        showif Espot == 1:
            imagebutton:
                idle "Espot1.png"
                focus_mask True
                action [SetVariable("Evisible", True), SetVariable("Ebutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Espot == 2:
            imagebutton:
                idle "Espot2.png"
                focus_mask True
                action [SetVariable("Evisible", True), SetVariable("Ebutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Espot == 3:
            imagebutton:
                idle "Espot3.png"
                focus_mask True
                action [SetVariable("Evisible", True), SetVariable("Ebutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Espot == 4:
            imagebutton:
                idle "Espot4.png"
                focus_mask True
                action [SetVariable("Evisible", True), SetVariable("Ebutton", False), SetVariable("taken4", False), Function(refresh)]
    showif E2button == True:
        showif E2spot == 1:
            imagebutton:
                idle "Espot1.png"
                focus_mask True
                action [SetVariable("E2visible", True), SetVariable("E2button", False), SetVariable("taken1", False), Function(refresh)]
        showif E2spot == 2:
            imagebutton:
                idle "Espot2.png"
                focus_mask True
                action [SetVariable("E2visible", True), SetVariable("E2button", False), SetVariable("taken2", False), Function(refresh)]
        showif E2spot == 3:
            imagebutton:
                idle "Espot3.png"
                focus_mask True
                action [SetVariable("E2visible", True), SetVariable("E2button", False), SetVariable("taken3", False), Function(refresh)]
        showif E2spot == 4:
            imagebutton:
                idle "Espot4.png"
                focus_mask True
                action [SetVariable("E2visible", True), SetVariable("E2button", False), SetVariable("taken4", False), Function(refresh)]
    showif Fbutton == True:
        showif Fspot == 1:
            imagebutton:
                idle "Fspot1.png"
                focus_mask True
                action [SetVariable("Fvisible", True), SetVariable("Fbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Fspot == 2:
            imagebutton:
                idle "Fspot2.png"
                focus_mask True
                action [SetVariable("Fvisible", True), SetVariable("Fbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Fspot == 3:
            imagebutton:
                idle "Fspot3.png"
                focus_mask True
                action [SetVariable("Fvisible", True), SetVariable("Fbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Fspot == 4:
            imagebutton:
                idle "Fspot4.png"
                focus_mask True
                action [SetVariable("Fvisible", True), SetVariable("Fbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Gbutton == True:
        showif Gspot == 1:
            imagebutton:
                idle "Gspot1.png"
                focus_mask True
                action [SetVariable("Gvisible", True), SetVariable("Gbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Gspot == 2:
            imagebutton:
                idle "Gspot2.png"
                focus_mask True
                action [SetVariable("Gvisible", True), SetVariable("Gbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Gspot == 3:
            imagebutton:
                idle "Gspot3.png"
                focus_mask True
                action [SetVariable("Gvisible", True), SetVariable("Gbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Gspot == 4:
            imagebutton:
                idle "Gspot4.png"
                focus_mask True
                action [SetVariable("Gvisible", True), SetVariable("Gbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Hbutton == True:
        showif Hspot == 1:
            imagebutton:
                idle "Hspot1.png"
                focus_mask True
                action [SetVariable("Hvisible", True), SetVariable("Hbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Hspot == 2:
            imagebutton:
                idle "Hspot2.png"
                focus_mask True
                action [SetVariable("Hvisible", True), SetVariable("Hbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Hspot == 3:
            imagebutton:
                idle "Hspot3.png"
                focus_mask True
                action [SetVariable("Hvisible", True), SetVariable("Hbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Hspot == 4:
            imagebutton:
                idle "Hspot4.png"
                focus_mask True
                action [SetVariable("Hvisible", True), SetVariable("Hbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Ibutton == True:
        showif Ispot == 1:
            imagebutton:
                idle "Ispot1.png"
                focus_mask True
                action [SetVariable("Ivisible", True), SetVariable("Ibutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Ispot == 2:
            imagebutton:
                idle "Ispot2.png"
                focus_mask True
                action [SetVariable("Ivisible", True), SetVariable("Ibutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Ispot == 3:
            imagebutton:
                idle "Ispot3.png"
                focus_mask True
                action [SetVariable("Ivisible", True), SetVariable("Ibutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Ispot == 4:
            imagebutton:
                idle "Ispot4.png"
                focus_mask True
                action [SetVariable("Ivisible", True), SetVariable("Ibutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Jbutton == True:
        showif Jspot == 1:
            imagebutton:
                idle "Jspot1.png"
                focus_mask True
                action [SetVariable("Jvisible", True), SetVariable("Jbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Jspot == 2:
            imagebutton:
                idle "Jspot2.png"
                focus_mask True
                action [SetVariable("Jvisible", True), SetVariable("Jbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Jspot == 3:
            imagebutton:
                idle "Jspot3.png"
                focus_mask True
                action [SetVariable("Jvisible", True), SetVariable("Jbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Jspot == 4:
            imagebutton:
                idle "Jspot4.png"
                focus_mask True
                action [SetVariable("Jvisible", True), SetVariable("Jbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Kbutton == True:
        showif Kspot == 1:
            imagebutton:
                idle "Kspot1.png"
                focus_mask True
                action [SetVariable("Kvisible", True), SetVariable("Kbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Kspot == 2:
            imagebutton:
                idle "Kspot2.png"
                focus_mask True
                action [SetVariable("Kvisible", True), SetVariable("Kbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Kspot == 3:
            imagebutton:
                idle "Kspot3.png"
                focus_mask True
                action [SetVariable("Kvisible", True), SetVariable("Kbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Kspot == 4:
            imagebutton:
                idle "Kspot4.png"
                focus_mask True
                action [SetVariable("Kvisible", True), SetVariable("Kbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Lbutton == True:
        showif Lspot == 1:
            imagebutton:
                idle "Lspot1.png"
                focus_mask True
                action [SetVariable("Lvisible", True), SetVariable("Lbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Lspot == 2:
            imagebutton:
                idle "Lspot2.png"
                focus_mask True
                action [SetVariable("Lvisible", True), SetVariable("Lbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Lspot == 3:
            imagebutton:
                idle "Lspot3.png"
                focus_mask True
                action [SetVariable("Lvisible", True), SetVariable("Lbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Lspot == 4:
            imagebutton:
                idle "Lspot4.png"
                focus_mask True
                action [SetVariable("Lvisible", True), SetVariable("Lbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Mbutton == True:
        showif Mspot == 1:
            imagebutton:
                idle "Mspot1.png"
                focus_mask True
                action [SetVariable("Mvisible", True), SetVariable("Mbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Mspot == 2:
            imagebutton:
                idle "Mspot2.png"
                focus_mask True
                action [SetVariable("Mvisible", True), SetVariable("Mbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Mspot == 3:
            imagebutton:
                idle "Mspot3.png"
                focus_mask True
                action [SetVariable("Mvisible", True), SetVariable("Mbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Mspot == 4:
            imagebutton:
                idle "Mspot4.png"
                focus_mask True
                action [SetVariable("Mvisible", True), SetVariable("Mbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Nbutton == True:
        showif Nspot == 1:
            imagebutton:
                idle "Nspot1.png"
                focus_mask True
                action [SetVariable("Nvisible", True), SetVariable("Nbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Nspot == 2:
            imagebutton:
                idle "Nspot2.png"
                focus_mask True
                action [SetVariable("Nvisible", True), SetVariable("Nbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Nspot == 3:
            imagebutton:
                idle "Nspot3.png"
                focus_mask True
                action [SetVariable("Nvisible", True), SetVariable("Nbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Nspot == 4:
            imagebutton:
                idle "Nspot4.png"
                focus_mask True
                action [SetVariable("Nvisible", True), SetVariable("Nbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Obutton == True:
        showif Ospot == 1:
            imagebutton:
                idle "Ospot1.png"
                focus_mask True
                action [SetVariable("Ovisible", True), SetVariable("Obutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Ospot == 2:
            imagebutton:
                idle "Ospot2.png"
                focus_mask True
                action [SetVariable("Ovisible", True), SetVariable("Obutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Ospot == 3:
            imagebutton:
                idle "Ospot3.png"
                focus_mask True
                action [SetVariable("Ovisible", True), SetVariable("Obutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Ospot == 4:
            imagebutton:
                idle "Ospot4.png"
                focus_mask True
                action [SetVariable("Ovisible", True), SetVariable("Obutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Pbutton == True:
        showif Pspot == 1:
            imagebutton:
                idle "Pspot1.png"
                focus_mask True
                action [SetVariable("Pvisible", True), SetVariable("Pbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Pspot == 2:
            imagebutton:
                idle "Pspot2.png"
                focus_mask True
                action [SetVariable("Pvisible", True), SetVariable("Pbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Pspot == 3:
            imagebutton:
                idle "Pspot3.png"
                focus_mask True
                action [SetVariable("Pvisible", True), SetVariable("Pbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Pspot == 4:
            imagebutton:
                idle "Pspot4.png"
                focus_mask True
                action [SetVariable("Pvisible", True), SetVariable("Pbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Rbutton == True:
        showif Rspot == 1:
            imagebutton:
                idle "Rspot1.png"
                focus_mask True
                action [SetVariable("Rvisible", True), SetVariable("Rbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Rspot == 2:
            imagebutton:
                idle "Rspot2.png"
                focus_mask True
                action [SetVariable("Rvisible", True), SetVariable("Rbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Rspot == 3:
            imagebutton:
                idle "Rspot3.png"
                focus_mask True
                action [SetVariable("Rvisible", True), SetVariable("Rbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Rspot == 4:
            imagebutton:
                idle "Rspot4.png"
                focus_mask True
                action [SetVariable("Rvisible", True), SetVariable("Rbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Sbutton == True:
        showif Sspot == 1:
            imagebutton:
                idle "Sspot1.png"
                focus_mask True
                action [SetVariable("Svisible", True), SetVariable("Sbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Sspot == 2:
            imagebutton:
                idle "Sspot2.png"
                focus_mask True
                action [SetVariable("Svisible", True), SetVariable("Sbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Sspot == 3:
            imagebutton:
                idle "Sspot3.png"
                focus_mask True
                action [SetVariable("Svisible", True), SetVariable("Sbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Sspot == 4:
            imagebutton:
                idle "Sspot4.png"
                focus_mask True
                action [SetVariable("Svisible", True), SetVariable("Sbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Tbutton == True:
        showif Tspot == 1:
            imagebutton:
                idle "Tspot1.png"
                focus_mask True
                action [SetVariable("Tvisible", True), SetVariable("Tbutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Tspot == 2:
            imagebutton:
                idle "Tspot2.png"
                focus_mask True
                action [SetVariable("Tvisible", True), SetVariable("Tbutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Tspot == 3:
            imagebutton:
                idle "Tspot3.png"
                focus_mask True
                action [SetVariable("Tvisible", True), SetVariable("Tbutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Tspot == 4:
            imagebutton:
                idle "Tspot4.png"
                focus_mask True
                action [SetVariable("Tvisible", True), SetVariable("Tbutton", False), SetVariable("taken4", False), Function(refresh)]
    showif Ubutton == True:
        showif Uspot == 1:
            imagebutton:
                idle "Uspot1.png"
                focus_mask True
                action [SetVariable("Uvisible", True), SetVariable("Ubutton", False), SetVariable("taken1", False), Function(refresh)]
        showif Uspot == 2:
            imagebutton:
                idle "Uspot2.png"
                focus_mask True
                action [SetVariable("Uvisible", True), SetVariable("Ubutton", False), SetVariable("taken2", False), Function(refresh)]
        showif Uspot == 3:
            imagebutton:
                idle "Uspot3.png"
                focus_mask True
                action [SetVariable("Uvisible", True), SetVariable("Ubutton", False), SetVariable("taken3", False), Function(refresh)]
        showif Uspot == 4:
            imagebutton:
                idle "Uspot4.png"
                focus_mask True
                action [SetVariable("Uvisible", True), SetVariable("Ubutton", False), SetVariable("taken4", False), Function(refresh)]
    # keep in order depending on
    showif E2visible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "E2"
                child "E2.png"
                xpos 0
                ypos 703
                xsize 232
                ysize 224
                draggable True
                droppable False
                dragged blockdrag
                drag_raise True
    showif Svisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "S"
                child "S.png"
                xpos 1110
                ypos 859
                draggable True
                droppable False
                dragged blockdrag
                drag_raise True
    showif Lvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "L"
                child "L.png"
                xpos 1283
                ypos 662
                xsize 291
                ysize 281
                draggable True
                droppable False
                dragged blockdrag
                drag_raise True
    showif Gvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "G"
                child "G.png"
                xpos 1478
                ypos 758
                draggable True
                droppable False
                dragged blockdrag
                drag_raise True
    showif Mvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "M"
                child "M.png"
                xpos 133
                ypos 703
                draggable True
                droppable False
                dragged blockdrag
                drag_raise True
    showif Nvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "N"
                child "N.png"
                xpos 1361
                ypos 756
                draggable True
                droppable False
                dragged blockdrag
    showif Dvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "D"
                child "D.png"
                xpos 382
                ypos 719
                draggable True
                droppable False
                dragged blockdrag
    showif Ivisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "I"
                child "I.png"
                xpos 855
                ypos 880
                draggable True
                droppable False
                dragged blockdrag
    showif Bvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "B"
                child "B.png"
                xpos 0
                ypos 820
                xsize 291
                ysize 281
                draggable True
                droppable False
                dragged blockdrag
    showif Avisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "A"
                child "A.png"
                xpos 1688
                ypos 856
                xsize 232
                ysize 224
                draggable True
                droppable False
                dragged blockdrag
    showif Cvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "C"
                child "C.png"
                xpos 215
                ypos 834
                draggable True
                droppable False
                dragged blockdrag
    showif Fvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "F"
                child "F.png"
                xpos 494
                ypos 720
                draggable True
                droppable False
                dragged blockdrag
    showif Hvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "H"
                child "H.png"
                xpos 603
                ypos 724
                draggable True
                droppable False
                dragged blockdrag
    showif Pvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "P"
                child "P.png"
                xpos 1193
                ypos 667
                draggable True
                droppable False
                dragged blockdrag
    showif Rvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "R"
                child "R.png"
                xpos 925
                ypos 699
                draggable True
                droppable False
                dragged blockdrag
    showif Jvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "J"
                child "J.png"
                xpos 448
                ypos 623
                draggable True
                droppable False
                dragged blockdrag
    showif Kvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "K"
                child "K.png"
                xpos 552
                ypos 620
                draggable True
                droppable False
                dragged blockdrag
    showif Ovisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "O"
                child "O.png"
                xpos 426
                ypos 849
                draggable False
                droppable True
                dragged blockdrag
    showif Tvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "T"
                child "T.png"
                xpos 821
                ypos 701
                draggable True
                droppable False
                dragged blockdrag
    showif Uvisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "U"
                child "U.png"
                xpos 1240
                ypos 567
                draggable True
                droppable False
                dragged blockdrag
    showif Evisible == True:
        draggroup:
            drag:
                drag_name "1"
                xpos 471
                ypos 146
                xsize 177
                ysize 173
                draggable False
                droppable True
            drag:
                drag_name "2"
                xpos 655
                ypos 123
                xsize 166
                ysize 157
                draggable False
                droppable True
            drag:
                drag_name "3"
                xpos 863
                ypos 130
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "4"
                xpos 1066
                ypos 128
                xsize 162
                ysize 153
                draggable False
                droppable True
            drag:
                drag_name "E"
                child "E.png"
                xpos 1513
                ypos 865
                draggable True
                droppable False
                dragged blockdrag
