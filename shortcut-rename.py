import maya.cmds as cmds
selected = cmds.ls(sl=True,long=True)
if selected:
    result = cmds.promptDialog(
                    title='Rename Object',
                    message='Enter Name:',
                    button=['OK', 'Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')

    if result == 'OK':
            newName = cmds.promptDialog(query=True, text=True)
            cmds.rename(selected[-1], newName)
