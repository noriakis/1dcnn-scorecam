def returnPos(cam_ind):
    pos1 = []
    tmppos = []
    inRange=False
    for a in range(0, len(cam_ind)):
        if a+1<len(cam_ind):
            if (cam_ind[a+1]-cam_ind[a]==1) and inRange==False:
                inRange=True
                tmppos.append(cam_ind[a])
            elif inRange==True and (cam_ind[a+1]-cam_ind[a]==1):
                pass
            elif inRange==True and (cam_ind[a+1]-cam_ind[a]!=1):
                tmppos.append(cam_ind[a])
                pos1.append(tmppos)
                tmppos = []
                inRange=False
        elif inRange==True:
                tmppos.append(cam_ind[a])
                pos1.append(tmppos)
    return pos1