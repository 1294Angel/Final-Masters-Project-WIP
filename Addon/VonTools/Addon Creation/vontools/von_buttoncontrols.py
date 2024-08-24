#Import all needed
import bpy # type: ignore
import os
from . import von_createcontrols
from .von_createcontrols import *    
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
    
    
def colorizerig():
    if poll("POSE") == True:
        lst_bonenames = []
        for armature in [ob for ob in bpy.data.objects if ob.type == 'ARMATURE']:
            for bone in armature.bones.values():
                lst_bonenames.append(bone.name)
    else:
        print("Error-3-ColorizeRig-PollNotEqual")
            
def searchforbone(selected_armature, temp_bonetofind):
    if poll("POSE") == True:
        bpy.ops.pose.select_all(action='DESELECT')
        bpy.data.objects[str(selected_armature)].data.bones[temp_bonetofind].select=True
    if poll("EDIT_ARMATURE") == True:
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.data.objects[str(selected_armature)].data.bones[temp_bonetofind].select=True
    else:
        print("Error-4-SearchForBone-PollNotEqual")

def getexistingfilesindirectories(basedirectorytosearch):
    
    FileDirectory = str(basedirectorytosearch)+"//"+"controls"
    totallist = os.listdir(FileDirectory)
    return totallist
    #[['FUCKYEAH.json', 'Suzanne.json'], ['Curious.json']]


#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________
