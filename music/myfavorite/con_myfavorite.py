import math

d_beacon = 30 / 2
d_min = 20
d_max = 140
init_step = 12
tstep = 20
cary=[[0.3,0.7,0.1],[0.7,0.3,0.1],[0.3,0.1,0.7]]
tune = [0,2,2,1,0,0,
        0,1,1,2,1,-1,
        0,2,2,1,0,0,
        0,1,1,2,1,-1,
        0,2,1,0,0,0,
        0,1,1,0,-1,-1,
        0,0,0,1,1,1,
        2,2,2,2,-1,-1]

"""
"t-ccmmt-c-c-"  #  1- 2
tune += "m-ccmmt-c-c-"  #  3- 4
tune += "t-tmmmm-mmcc"  #  5- 6
tune += "c-cmmcm-m---"  #  7- 8
tune += "t-ccmmt-c-c-"  #  9-10
tune += "m-ccmmt-c-c-"  # 11-12
tune += "t-tmmmm-mmcc"  # 13-14
tune += "m-mmccc-----"  # 15-16
"""

def circle(xz, yz, sz):
    return oval(xz - sz, yz - sz, sz * 2, sz * 2)

def drawBall(x, y, num, c):
    nostroke()
    fill(cary[c][0], cary[c][1], cary[c][2])
    circle(x, y, 13)
    fill(1,1,1)
    fontsize(18)
    w = textwidth(str(num))
    text(str(num), x-w/2, y+5)
    
def drawMap(x, y, div, pnum):
    translate(x,y)
    # --- division line
    for i in range(div):
        theta = 2 * math.pi * i / div
        if (i % tstep == 0):
            if (i == 0):
                stroke(1,0,0)
            else:
                stroke(0.5,0.5,0.5)
        else:
            stroke(0.9,0.9,0.9)
        line(0, 0, math.cos(theta) * d_max, math.sin(theta) * d_max)
    # --- map
    stroke(0,0,0)
    nofill()
    for i in range(d_min, d_max, (d_max-d_min) / 3):
        circle(0,0,i+(d_max-d_min) / 3)
    # --- beacon
    nostroke()
    fill(0.7,0.7,0.7)
    circle(0,0,d_beacon)
    fill(1,1,1)
    fontsize(18)
    w = textwidth(str(pnum))
    text(str(pnum), -w/2, 5)

    translate(-x,-y)

def getNum(str):
    # 20, 60, 100, 140
    #   40   80  120 
    if   str == 2:    # 2
        return 120
    elif str == 1:    # 1
        return 80
    elif str == 0:    # 0
        return 40
    else:
        return -1

def drawTune(x, y, who, nmin, nmax):
    count = 0
    nc = [who]
    for i in range(0, len(tune), 3):
        for j in nc:
            s = getNum(tune[i+j]) 
            if s != -1:
                count+=1
                if (nmin <= (i + j)) and ((i + j) < nmax):
                    theta = ((i + j) * tstep / 60.0) * 2 * math.pi
                    drawBall(x + math.cos(theta) * s, 
                             y + math.sin(theta) * s, count, who)

# --- Main
w = 300 * 4
h = 300 * 4
size(w,h)

whoo = 1
for i in range(4):
    for j in range(4):
        drawMap(i * 300 + 150, j * 300 + 150, 60, i + j * 4 + 1)
        for k in range(3):
            drawTune(i * 300 + 150,j * 300 + 150, k, (i + j * 4) * 3, (i + j * 4 + 1) * 3)
