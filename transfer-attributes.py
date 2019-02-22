import maya.cmds as cmds
selected = cmds.ls(sl=True,long=True)
if len(selected) > 1:
    result = cmds.promptDialog(
                    title='Rename Object',
                    message='Enter Name:',
                    button=['OK', 'Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')

    if result == 'OK':
            input = cmds.promptDialog(query=True, text=True)
            if 'q' in input:
                absolute = True
            else:
                absolute = False
            if 'w' in input:
                cmds.xform(selected[-1], t=cmds.xform(selected[-2], q=True, ws=absolute, t=True), ws=absolute)
            if 'e' in input:
                cmds.xform(selected[-1], ro=cmds.xform(selected[-2], q=True, ws=absolute, ro=True), ws=absolute)
            if 'r' in input:
                cmds.xform(selected[-1], s=cmds.xform(selected[-2], q=True, ws=absolute, s=True), ws=absolute)
