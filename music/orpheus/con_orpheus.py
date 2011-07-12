import math

numLED = 16.0
d_beacon = 30 / 2
d_min = 20
d_max = 140
init_step = 12
tstep = 2
cary=[[0.3,0.7,0.1],[0.7,0.3,0.1],[0.3,0.1,0.7], [0.7,0.7,0.3]]
numPlayer = 4

tune = "1-2-2-3-2-1-1-3-1-2-3-2-3-1-1---3-1-1-3-3-1-1-2-3-1-3-1-3-1-3-1-1-2-2-3-2-1-1-3-1-2-3-2-3-1-1---3-1-1-3-3-1-1-2-3-1-3-1-3-1-1---"

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
    for i in range(int(div)):
        theta = 2 * math.pi * i / div
        if (i % tstep == 0):
            if (i == 0):
                stroke(1,0,0)
            else:
                stroke(0.5,0.5,0.5)
        else:
            stroke(0.8,0.8,0.8)
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
    if str == '3':
        return 120
    elif str == '2':
        return 80
    elif str == '1':
        return 40
    else:
        return -1

def drawTune(x, y, who, nmin, nmax):
    count = 0
    nc = [who*4, who*4+1, who*4+2, who*4+3]
    print nc
    
    for i in range(0, len(tune), numPlayer * 4):
        for j in nc:
            if (i + j) < len(tune):
                s = getNum(tune[i+j]) 
                if s != -1:
                    count+=1
                    if (nmin <= (i + j)) and ((i + j) <= nmax):
                        theta = ((i + j) /numLED) * 2 * math.pi + 0.13
                        drawBall(x + math.cos(theta) * s, 
                                 y + math.sin(theta) * s, count, who)

# --- Main
ww = 4
hh = 3

w = 300 * ww
h = 300 * hh
size(w,h)

whoo = 1
for i in range(ww):
    for j in range(hh):
        drawMap(i * 300 + 150, j * 300 + 150, numLED, i + j * ww + 1)
        for k in range(numPlayer):
            drawTune(i * 300 + 150,j * 300 + 150, k, (i + j * ww) * 16, (i + j * ww + 1) * 16 - 1)
