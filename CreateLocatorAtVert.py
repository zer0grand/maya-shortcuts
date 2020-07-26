sel = cmds.ls( selection=True )
selPos = []

for s in sel:
    ind = s.find(":")
    if ind != -1:
        indStart = s.index("[")
        start = int(s[indStart+1:ind])
        end = int(s[ind+1:-1])
        for obj in range(start, end+1):
            pos = cmds.pointPosition(s[:indStart] + "["+ str(obj) +"]")
            newLoc = cmds.spaceLocator(position=pos)
            
            print(pos)
            selPos += pos
    else:        
        pos = cmds.pointPosition(s)
        newLoc = cmds.spaceLocator(position=pos)
        
        print(pos)
        selPos += pos
