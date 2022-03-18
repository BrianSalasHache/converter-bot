from os import listdir

def seeker(ext1, *args):
    path = listdir('./conversor')
    list = []
    for i in enumerate(path):
        r = i[1].rsplit('.', 1)
        name, ext = r
        if ext == ext1 and not args:
            list.append(i[1])
        if args and ext == ext1:
            list.append([name, ext1, args[0]])
    return list