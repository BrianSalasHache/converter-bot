from os import listdir

def seeker(ext1):
    path = listdir('./conversor')
    list = []
    for i in enumerate(path):
        r = i[1].split('.')
        ext = r[1]
        if ext == ext1:
            list.append(i[1])
    return list