class TripletError(Exception): pass

Z = 999
melody = [
    #1   2   3   4   5   6   7   8
    57, 64, 64, 66, 64, 62, 62, 66,
    67, 71, 74, 71, 71, 69, 69,  Z,

    71, 61, 61, 71, 69, 62, 62, 66,
    66, 64, 66, 64, 66, 64, 66, 64,

    57, 64, 64, 66, 64, 62, 62, 66,
    67, 71, 74, 71, 71, 69, 69,  Z,
    
    71, 61, 61, 71, 69, 62, 62, 66,
    66, 64, 66, 64, 64, 62, 62,  Z,
]


def print_js(l):
    count = 0
    for t in l:
        print "\t%s," % repr(t)
        count = (count + 1) % 8
        if not count: print ""


def div_bar(l, div=4):
    tmp = []
    for i in range(len(l) / div):
        tmp.append(l[i * div: (i + 1) * div])
    return tmp


def gen_triplet(l):
    sorted_list = sorted(list(set(l)))
    if Z in sorted_list:
        sorted_list.remove(Z)

    if len(sorted_list) > 3:
        raise TripletError("over 3!", l)
    elif len(sorted_list) == 2:
        if (max(sorted_list) - min(sorted_list)) > 5:
            # very far
            center = (min(sorted_list) + max(sorted_list)) / 2
            sorted_list.insert(1, center)
        else:
            sorted_list.append(max(sorted_list) + 2)
            
    elif len(sorted_list) == 1:
        p = sorted_list[0]
        sorted_list.insert(0, p - 2)
        sorted_list.append(p + 2)
    return sorted_list


def print_js(triplets):
    for tpl in triplets:
        tmp = tpl[:]
        tmp.append(Z)
        for i in range(4):
            print "\t%s," % tmp


def print_map(melody, triplets):
    tune = ""
    for i, melody_fragment in enumerate(div_bar(melody)):
        for c in melody_fragment:
            if c in triplets[i]:
                tune += str(triplets[i].index(c) + 1)
            else:
                tune += '-'
            tune += '-'
    print "tune = \"%s\"" % tune
    


if __name__ == '__main__':
    triplets = map(gen_triplet, div_bar(melody))
    print_js(triplets)
    print_map(melody, triplets)


