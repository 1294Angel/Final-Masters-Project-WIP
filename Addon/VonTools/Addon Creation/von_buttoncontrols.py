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
    if poll("POSE") == True:
        bpy.ops.pose.select_all(action='DESELECT')
        bpy.data.objects[str(selected_armature)].data.bones[temp_bonetofind].select=True
    if poll("EDIT_ARMATURE") == True:
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.data.objects[str(selected_armature)].data.bones[temp_bonetofind].select=True
    else:
        print("Error-4-SearchForBone-PollNotEqual")

def getexistingfilesindirectories(basedirectorytosearch):
    
    inbuilt = str(basedirectorytosearch)+"//"+"controls"+"//"+"InbuiltControls//"
    custom = str(basedirectorytosearch)+"//"+"controls"+"//"+"CustomControls//"

    spaceconsole(3)
    print("Inbuilt Filepath")
    print(inbuilt)
    print("Base Directory To Search")
    print(basedirectorytosearch)


    inbuiltlist = os.listdir(inbuilt)
    customlist = os.listdir(custom)
    totallist = []
    totallist.append(inbuiltlist)
    totallist.append(customlist)

    spaceconsole(3)
    print("Get Inbuilt Files In Directory -->")
    print("")
    print("Inbuilt")
    print(totallist[0])
    print("Custom")
    print(totallist[1])
    print("Total")
    print(totallist)
    spaceconsole(3)

    return totallist
    #[['FUCKYEAH.json', 'Suzanne.json'], ['Curious.json']]


#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________
