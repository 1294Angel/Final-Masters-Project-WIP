#Import all needed
import bpy

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

#for pose mode
def setcontrol(temp_controlname):
    controlname=str(temp_controlname)
    bpy.context.active_pose_bone.custom_shape = bpy.data.objects[controlname]
    
def colorizerig():
    lst_bonenames = []
    for armature in [ob for ob in bpy.data.objects if ob.type == 'ARMATURE']:
        for bone in armature.bones.values():
            lst_bonenames.append(bone.name)
            
def searchforbone(temp_bonetofind):
    bpy.ops.pose.select_all(action='DESELECT')
    bpy.data.objects["SA-04 Combat Technician Armature"].data.bones[temp_bonetofind].select=True

#for edit mode



#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________


searchforbone("l_clavicle")