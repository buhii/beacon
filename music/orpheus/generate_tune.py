class TripletError(Exception): pass


Z = 999
melody = """
62  Z  Z  Z | 64 67 66 64 | 69  Z 69  Z | 69 71 66 67
64  Z 64  Z | 64 67 66 64 | 62 74 73 71 | 69 67 66 64

62  Z  Z  Z | 64 67 66 64 | 69  Z 69  Z | 69 71 66 67
64  Z 64  Z | 64 67 66 64

74  Z 62  Z | 64  Z 66  Z | 69 67 73 71 | 69 79 78 76
74  Z 62  Z | 64  Z 66  Z | 69 67 73 71 | 69 79 78 76

74  Z  Z  Z | 74  Z  Z  Z | 74  Z  Z  Z | 74  Z  Z  Z
74  Z  Z  Z | Z   Z  Z  Z | 62  Z  Z  Z 
"""


def div_bar(l, div=2):
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
            # near
            if max(sorted_list) < 68:
                sorted_list.append(max(sorted_list) + 2)
            else:
                sorted_list.insert(0, min(sorted_list) - 2)
    elif len(sorted_list) == 1:
        p = sorted_list[0]
        if p < 63:
            sorted_list.append(p + 2)
            sorted_list.append(p + 4)
        elif p < 69:
            sorted_list.insert(0, p - 2)
            sorted_list.append(p + 2)
        else:
            sorted_list.insert(0, p - 2)
            sorted_list.insert(0, p - 4)
    return sorted_list


def print_js(triplets):
    for tpl in triplets:
        if tpl:
            tmp = tpl[:]
        else:
            tmp = [Z, Z, Z]
        tmp.append(Z)
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


def prepare_melody(raw_melody):
    def str2num(s):
        if s == 'Z':
            return Z
        elif s.isdigit():
            return int(s)
        else:
            raise ValueError("not digit", s)
    melody = raw_melody.translate(None, '|').split()
    return map(str2num, filter(lambda c: c, melody))


if __name__ == '__main__':
    melody = prepare_melody(melody)
    triplets = map(gen_triplet, div_bar(melody))
    print_js(triplets)
    print_map(melody, triplets)

