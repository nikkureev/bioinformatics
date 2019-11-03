def samoe_bolshoe(l):
    naibolshee = l[0]
    for i in l:
        if i > naibolshee:
            naibolshee = i
    return naibolshee
