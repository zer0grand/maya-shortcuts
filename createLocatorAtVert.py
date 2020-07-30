### WARNING ###
# execute the following command before you select an object, then after you have made your selection run the rest
cmds.selectPref(trackSelectionOrder=True)
###
sel = cmds.ls( os=True )
locGroup = []

for s in sel:
    ind = s.find(":")
    if ind != -1:
        indStart = s.index("[")
        start = int(s[indStart+1:ind])
        end = int(s[ind+1:-1])
        for obj in range(start, end+1):
            pos = cmds.pointPosition(s[:indStart] + "["+ str(obj) +"]")
            newLoc = cmds.spaceLocator()
            cmds.move(pos[0], pos[1], pos[2], newLoc)
            locGroup += newLoc
    else:        
        pos = cmds.pointPosition(s)
        newLoc = cmds.spaceLocator()
        cmds.move(pos[0], pos[1], pos[2], newLoc)
        locGroup += newLoc

cmds.group(locGroup)
