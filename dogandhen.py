def dghn (heads,legs):
    dogs=(legs-heads*2)/2
    if dogs<0 or dogs%1:
        return None
    dogs=int(dogs)
    hen=heads-dogs
    if hen< 0:
        return None
    return [hen,dogs]