import os
import maya.cmds as cmds
os.chdir("PATH GOES HERE")

# this script is made to take TSV motion capture data from the Qualysis Tracking Manager and import it into Autodesk Maya

################################################################################

objName = "mocap_"
initframe = 0

def mocapRig(markers, objName, finalFrame):
   for i,frame in enumerate(range(0,finalFrame+1)):
       cmds.currentTime( i, update=True, edit=True )
       
       for marker in markers:
           #Can query multple keyframes to make faster:
           # Query all keyframes of object "surface1" within the time range 0 to 20.
           #cmds.keyframe( 'surface1', time=(0,20), query=True, valueChange=True, timeChange=True);

           mcPos = cmds.xform(marker,q=1,ws=1,rp=1)
           
           cmds.select( marker[len(objName):] )
           cmds.move( mcPos[0]-markers[marker][0], mcPos[1]-markers[marker][1], mcPos[2]-markers[marker][2], r=1 )
           cmds.setKeyframe( marker[len(objName):], attribute='translateX', t=0 )
           cmds.setKeyframe( marker[len(objName):], attribute='translateY', t=0 )
           cmds.setKeyframe( marker[len(objName):], attribute='translateZ', t=0 )

################################################################################

firstFrame = 0 # first frame
lastFrame = 20 # last frame
defPos = 0 # frame with default position
mcGroup = "allMarkers" # name of group with all markers
root = "back" # root node of rig

global objName
objName = "mocap_" # mocap tracker prefix
global mcDef
mcDef = getDefaultPosition(mcGroup, defPos) #default mocap position
global rigPos
rigPos = {}

def getDefaultPosition(mcGroup, defPos): # creates dictionary of default values of mocap
    cmds.currentTime(defPos, update=True, edit=True)
    markers = cmds.listRelatives(mcGroup)
    returned={}
    for i,marker in enumerate(markers):
        if cmds.getAttr(marker+'.visibility'):
            returned[marker] = cmds.xform(marker,q=1,ws=1,rp=1)
    return returned

def markerData(markers):
    for marker in markers:
        rigPos[marker[len(objName):]] = cmds.xform(marker, q=1, ws=1, rp=1)

def moveMarkers(root, markers): # pre order traversal of tree to match nodes with mocap
    nodes = cmds.listRelatives(root)
    if objName+root in markers:
        # move and keyframe node
        mcPos = cmds.xform(objName+root, q=1, ws=1, rp=1)
        cmds.select(root)
        cmds.move(mcPos[0]-mcDef[objName+root][0]+rigPos[root][0], mcPos[1]-mcDef[objName+root][1]+rigPos[root][1], mcPos[2]-mcDef[objName+root][2]+rigPos[root][2])
        cmds.setKeyframe(root, attribute='translateX')
        cmds.setKeyframe(root, attribute='translateY')
        cmds.setKeyframe(root, attribute='translateZ')
            
    if nodes == None:
        return
    for i,node in enumerate(nodes):
        moveMarkers(nodes[i], markers)

def matchToRig(root, markers, firstFrame, lastFrame):
    for i,frame in enumerate(range(firstFrame, lastFrame+1)): # iterate through all frames
        cmds.currentTime(i, update=True, edit=True)
        markerData(markers)
        moveMarkers(root, markers)

matchToRig(root, getDefaultPosition(mcGroup, defPos), firstFrame, lastFrame)

################################################################################


cmds.select("allMarkers")
children = cmds.ls( dag=True, ap=True, sl=True )
markers={}
for i,elem in enumerate(children):
   if i%2 == 1:
       markers[elem] = cmds.xform(elem,q=1,ws=1,rp=1)

mocapRig(markers, objName, 2000)

##x=cmds.xform('head',q=1,ws=1,rp=1)
##cmds.move(x[0]+1, x[1], x[2], worldSpaceDistance=True, absolute=False)

##cmds.select( 'head' )
##cmds.move(1,0,0, r=1)


#get default
part = "head"
defaultPose = 0
cmds.currentTime( defaultPose, update=True, edit=True )
mcDef = cmds.xform("mocap_"+part,q=1,ws=1,rp=1)

#at time t
t = 1000
cmds.currentTime( t, update=True, edit=True )
mcPos = cmds.xform("mocap_"+part,q=1,ws=1,rp=1)

cmds.select( part )
cmds.move( mcPos[0]-mcDef[0]+rigPos[0], mcPos[1]-mcDef[1]+rigPos[1], mcPos[2]-mcDef[2]+rigPos[2])

###########################################################################

def getDefaultPosition(groupName, defaultFrame): # creates dictionary of default values of mocap
    cmds.currentTime(defaultFrame, update=True, edit=True)
    markers = cmds.listRelatives(groupName)
    returned={}
    for i,marker in enumerate(markers):
        if cmds.getAttr(marker+'.visibility'):
            returned[marker] = cmds.xform(marker,q=1,ws=1,rp=1)
    return returned

def nullMarkers()

def moveMarkers(root, defaultPosition): # pre order traversal of tree to match nodes with mocap
    nodes = cmds.listRelatives(root)
    if objName+root in markers:
        # move and keyframe node
        mcPos = cmds.xform(objName+root, q=1, ws=1, rp=1)
        cmds.select(root)
        cmds.move(mcPos[0]-mcDef[objName+root][0]+rigPos[root][0], mcPos[1]-mcDef[objName+root][1]+rigPos[root][1], mcPos[2]-mcDef[objName+root][2]+rigPos[root][2])
        cmds.setKeyframe(root, attribute='translateX')
        cmds.setKeyframe(root, attribute='translateY')
        cmds.setKeyframe(root, attribute='translateZ')

moveMarkers("back", getDefaultPosition("allMarkers", 156))
