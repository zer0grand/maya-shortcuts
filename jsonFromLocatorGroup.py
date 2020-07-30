import json

exportObj = {"groups":[]}

groups = cmds.listRelatives(children=True)

for group in groups:
    locators = cmds.listRelatives(group, children=True)
    subGroupContainer = []
    for locator in locators:        
        subGroupContainer.append(cmds.xform(locator, q=True, t=True, ws=True))
        
    exportObj["groups"].append({"loop":False, "width":.05, "points":subGroupContainer})
    
print(json.dumps(exportObj, indent=2))