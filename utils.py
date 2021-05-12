def returnPos(bicam_ind):
    pos1 = []
    tmppos = []
    inRange=False
    for a in range(0, len(bicam_ind)):
        if a+1<len(bicam_ind):
            if (bicam_ind[a+1]-bicam_ind[a]==1) and inRange==False:
                inRange=True
                tmppos.append(bicam_ind[a])
            elif inRange==True and (bicam_ind[a+1]-bicam_ind[a]==1):
                pass
            elif inRange==True and (bicam_ind[a+1]-bicam_ind[a]!=1):
                tmppos.append(bicam_ind[a])
                pos1.append(tmppos)
                tmppos = []
                inRange=False
        elif inRange==True:
                tmppos.append(bicam_ind[a])
                pos1.append(tmppos)
    return pos1