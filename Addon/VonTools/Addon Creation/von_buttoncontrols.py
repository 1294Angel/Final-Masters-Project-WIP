#Import all needed
import bpy # type: ignore
from von_createcontrols import *    
#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________

#setting up vars
tempstr = ""
tempint = 0
tempbool = False

#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________

#for object mode
def poll(compstr):
    active_object = bpy.context.mode
    if active_object == compstr:
        bool = True
        print(active_object + " --- " + "True")
        return bool
    if active_object != compstr:
        bool = False
        print(active_object + " --- " + "False")
        return bool
    else:
        print("Error-1-PollNotEqual")
    

#for pose mode
def setcontrol(temp_controlname):
    if poll("POSE") == True:
        controlname=str(temp_controlname)
        bpy.context.active_pose_bone.custom_shape = bpy.data.objects[controlname]
    
def colorizerig():
    if poll("POSE") == True:
        lst_bonenames = []
        for armature in [ob for ob in bpy.data.objects if ob.type == 'ARMATURE']:
            for bone in armature.bones.values():
                lst_bonenames.append(bone.name)
    else:
        print("Error-3-ColorizeRig-PollNotEqual")
            
def searchforbone(selected_armature, temp_bonetofind):
    spaceconsole(3)
    print(selected_armature)
    spaceconsole(3)
    if poll("POSE") == True:
        bpy.ops.pose.select_all(action='DESELECT')
        bpy.data.objects[str(selected_armature)].data.bones[temp_bonetofind].select=True
    if poll("EDIT_ARMATURE") == True:
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.data.objects[str(selected_armature)].data.bones[temp_bonetofind].select=True
    else:
        print("Error-4-SearchForBone-PollNotEqual")




#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________
