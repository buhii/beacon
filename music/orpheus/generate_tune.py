def melody2js(melody):
    js = []
    conte = melody2conte(melody)

    tmp = []
    for i in range(len(melody)):
        t = melody[i]
        if conte[i] == -1:
            if not tmp:
                tmp = [999] * 3
	elif conte[i] == 1:
            tmp = [t, t+1, t+2]
	elif conte[i] == 2:
            tmp = [t-1, t, t+1]
	elif conte[i] == 3:
            tmp = [t-2, t-1, t]

        if len(tmp) == 3:
            tmp.append(999)
	js.append(tmp)
    return js


def melody2conte(melody):
    m_min = min(melody)
    m_max = max(map(lambda x: x if x != 999 else m_min, melody))

    d = m_max - m_min + 1

    ret = []
    for m in melody:
        if m != 999:
            ret.append(int((m - m_min) * 3.0 / d) + 1)
	else:
            ret.append(-1)
    return ret


N = 999


def quantize_3(l):
    def filter_nan(m):
        ret = filter(lambda c: c != N, m)
        if ret:
            return ret[0]
        else:
            return N

    tri = zip(l[0::3], l[1::3], l[2::3])
    return map(filter_nan, tri)


orpheus = [
    #1   2   3   4   5   6   7   8
    57, 64, 64, 66, 64, 62, 62, 66,
    
]


def print_map(l):
    print "tune = %s" % repr(l)

def print_js(l):
    count = 0
    for t in l:
        print "\t%s," % repr(t)
        count = (count + 1) % 8
        if not count: print ""

print_map(melody2conte(mito))
print_js(melody2js(quantize_3(mito)))

