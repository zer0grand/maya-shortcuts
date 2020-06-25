import os
import json
import maya.cmds as cmds
os.chdir("C:\Users\point_rain\Desktop")

fileName = "newfile.txt"
objName = "object_"

cmds.currentUnit( time="30fps" )
cmds.playbackOptions( min='0', max='2000' )

thresh = 1

#def readFile(fileName):
frame=0
with open(fileName) as f:
    for i, line in enumerate(f):
        if i == thresh-1:
            markers = line.strip().split(" ")
            markers = markers[2:]
            print(markers)
            for j, marker in enumerate(markers):
                markers[j] = objName+marker
                cmds.spaceLocator(name=objName+marker)
        elif i > thresh-1:
            coords = line.strip().split("\t")
            print(coords)
            counter = 1
            counterMarker = 0
            while counter != len(coords):
                cmds.setKeyframe( markers[counterMarker], t=frame, at='tx', v=float(coords[counter]) )
                cmds.setKeyframe( markers[counterMarker], t=frame, at='ty', v=float(coords[counter+1]) )
                cmds.setKeyframe( markers[counterMarker], t=frame, at='tz', v=float(coords[counter+2]) )
                cmds.setKeyframe( markers[counterMarker], t=frame, at='rx', v=float(coords[counter+3]) )
                cmds.setKeyframe( markers[counterMarker], t=frame, at='ry', v=float(coords[counter+4]) )
                cmds.setKeyframe( markers[counterMarker], t=frame, at='rz', v=float(coords[counter+5]) )
                counter+=6
                counterMarker+=1
            frame+=1
