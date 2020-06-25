import os
import json
import maya.cmds as cmds
os.chdir("C:\Users\point_rain\Downloads")

fileName = "Measurement643.tsv"
objName = "mocap3_"

cmds.currentUnit( time="30fps" )
cmds.playbackOptions( min='0', max='2000' )

thresh = 10

#def readFile(fileName):
frame=0
with open(fileName) as f:
    for i, line in enumerate(f):
        if i == thresh-1:
            markers = line.strip().split("\t")
            markers = markers[1:]
            for j, marker in enumerate(markers):
                markers[j] = objName+marker
                cmds.spaceLocator(name=objName+marker)
        elif i > thresh-1:
            coords = line.strip().split("\t")
            counter = 0
            counterMarker = 0
            while counter != len(coords):
                cmds.setKeyframe( markers[counterMarker], t=frame, at='tx', v=float(coords[counter])/100 )
                cmds.setKeyframe( markers[counterMarker], t=frame, at='tz', v=float(coords[counter+1])/100 )
                cmds.setKeyframe( markers[counterMarker], t=frame, at='ty', v=float(coords[counter+2])/100 )
                counter+=3
                counterMarker+=1
            frame+=1
