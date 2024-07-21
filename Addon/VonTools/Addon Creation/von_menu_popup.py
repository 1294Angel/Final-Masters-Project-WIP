# ------------------------------------------------------------------------
#    Addon Info
# ------------------------------------------------------------------------

bl_info = {
    "name": "Vona's Blender Tools",
    "author": "Vona",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "Where the user can find it",
    "description": "An addon that adds rigging tools for quick and easy custom rigs.",
    "warning": "",
    "wcooliki_url": "",
    "tracker_url": "",
    "category": ""}

import bpy # type: ignore
import sys 
import os
from bpy.types import Operator # type: ignore
from bpy_extras.object_utils import AddObjectHelper # type: ignore
from bpy.types import Operator # type: ignore
from bpy_extras.object_utils import object_data_add # type: ignore
from mathutils import Vector # type: ignore
from math import radians # type: ignore
from pathlib import Path

from bpy.props import (StringProperty, # type: ignore
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel, # type: ignore
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

import von_buttoncontrols, von_createcontrols
import imp
imp.reload(von_buttoncontrols)
imp.reload(von_createcontrols)
#import functions
from von_buttoncontrols import *
from von_createcontrols import *

# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------

class MySettings(PropertyGroup):

    my_bool : BoolProperty(
        name="Enable or Disable",
        description="A bool property",
        default = False
        ) # type: ignore

    my_int : IntProperty(
        name = "Set a value",
        description="A integer property",
        default = 23,
        min = 10,
        max = 100
        ) # type: ignore

    my_float : FloatProperty(
        name = "Set a value",
        description = "A float property",
        default = 23.7,
        min = 0.01,
        max = 30.0
        ) # type: ignore
        
    bonebeingsearched: StringProperty(
        name="String",
        description="",
        default="",
        maxlen=1024,
        ) # type: ignore

# ------------------------------------------------------------------------
#    Popout Submenu's
# ------------------------------------------------------------------------

class VonPanel_RiggingTools__Submenu_BoneSearch(bpy.types.Operator):
    bl_idname = "von.popoutpanelbonesearch"
    bl_label = "Bone Search"
    

    text : bpy.props.StringProperty(
        name="Enter Text", default=""
        ) # type: ignore
    def execute(self, context):
        text = self.text
        armaturename=bpy.context.selected_objects
        for i in armaturename:
            spaceconsole(3)
            print(i.name)
            spaceconsole(3)
            searchforbone(i.name, text)
        return {'FINISHED'}
    def invoke(self, context, event):   
        return context.window_manager.invoke_props_dialog(self)


#Creating Dropdown Menu Popup
class Von_Dropdown_AddCustomBoneshape(bpy.types.Operator):
    bl_label = "Template Operator"
    bl_idname = "von.testinglonglistbitch"

    temp_items = getexistingfilesindirectories(getfolderloc())
    spaceconsole(3)
    print("Total Temp Items")
    print(temp_items)
    #Format
    #[[List of files in Inbuilt Controls],[List of files in Custom Controls]]
    #[['FUCKYEAH.json', 'Suzanne.json'], ['Curious.json']]




    numbertimes = 0
    for i in temp_items[0]:
        numbertimes = numbertimes + 1
        print(numbertimes)
        print("DropdownClass")
        print(i)
    spaceconsole(3)
    
    temp_total = 0
    sendtoenum = []
    for i in temp_items[0]:
            temp_total = temp_total + 1
            temp_total_string = f"'{str(temp_total)}'"
            #idescription = f"Click To Create {i} As An Avalible Boneshape"
            listofstrings = tuple((temp_total_string, i, i))

            """ 
            REALLY This needs to be formatted as 
            
            [
            ('1', 'FUCKYEAH', 'FUCKYEAH'),
            ('2', 'Suzanne', 'Suzanne')
            ]
            
                not 
            
            [
            [1, 'FUCKYEAH', 'FUCKYEAH'],
            [2, 'Suzanne', 'Suzanne']
            ] 
            
            or else blender will refuse to read it and the enum failure will cause blender to crash and the dropdown to fail
            
            """
            
            sendtoenum.append(listofstrings)
            spaceconsole(5)
            print("Send To Enum " + str(temp_total) + "  -->")
            print(sendtoenum)
            spaceconsole(5)

    preset_enum : bpy.props.EnumProperty(
        name = "",
        description = "Select An Option",   
        items = sendtoenum,
    )     # type: ignore
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "preset_enum")
    
    def execute(self, context):
        temp_items = getexistingfilesindirectories(get_path_to_preset_mesh_data())
        create_mesh_from_json_data(False,temp_items[self.preset_enum])
    
        return {'FINISHED'}    

# ------------------------------------------------------------------------
#    Button Setup
# ------------------------------------------------------------------------

class VonPanel_RiggingTools__Submenu_CreateControl(bpy.types.Operator):
    bl_idname = "von.loadcustomcontrol"
    bl_label = "Load Custom Control"
    
    text : bpy.props.StringProperty(name="Enter Text", default="") # type: ignore
    def execute(self, context):
        text = self.text
        create_mesh_from_json_data(False,text)
        return {'FINISHED'}
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class VonPanel_RiggingTools__Button_SaveNewControl(bpy.types.Operator):
    bl_idname = "von.savenewcontrol"
    bl_label = "Save Control"
    
    def execute(self, context):
        saveselectedmesh()
        return {'FINISHED'}
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class VonPanel_RiggingTools_Button_TEMP(bpy.types.Operator):
    bl_idname = "von.testbutton"
    bl_label = "Test -- Populate List From Folder"

    def execute(self,context):
        
        print(getexistingfilesindirectories(get_path_to_preset_mesh_data()))
        return {'FINISHED'}
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

"""
class VonPanel_RiggingTools__Button_GeneratePresetBoneshapes(bpy.types.Operator):
    bl_idname = "von.generatepresetboneshapes"
    bl_label = "Generate Preset Boneshapes"
    
    def execute(self, context):
        getexistingfilesindirectories(get_path_to_preset_mesh_data())
        return {'FINISHED'}
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    """

# ------------------------------------------------------------------------
#    Menu Setup
# ------------------------------------------------------------------------

class VonPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'VonTools'
    bl_options = {"DEFAULT_CLOSED"}

class VonPanel_PrimaryPanel(VonPanel, bpy.types.Panel):
    bl_idname = "von.vontools"
    bl_label= "Von Tools"

    def draw(self,context):
        layout = self.layout
        layout.label(text= "Vontools For All Your Rigging Needs")

class VonPanel_RiggingTools(VonPanel, bpy.types.Panel):
    bl_parent_id = "von.vontools"
    bl_label = "Rigging Tools"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        scene = context.scene
        mytool=scene.my_tool

        row.label(text= "Bone Manipulation", icon= 'CUBE')
        #Colorize Rig

        #Bone Search
        layout.operator_context = 'INVOKE_DEFAULT'
        layout.operator("von.popoutpanelbonesearch")
        

        row.label(text= "Bone Shapes", icon= 'CUBE')
        #create object
        layout.operator_context = 'INVOKE_DEFAULT'
        layout.operator("von.testinglonglistbitch")
        layout.operator("von.testbutton")
        layout.operator("von.savenewcontrol")
        #layout.operator("von.generatepresetboneshapes")


        row.label(text= "Weight Painting", icon= 'CUBE')


# ------------------------------------------------------------------------
#    Register Classes
# ------------------------------------------------------------------------

classes = (
    MySettings,
    VonPanel_PrimaryPanel,
    VonPanel_RiggingTools,
    VonPanel_RiggingTools__Submenu_BoneSearch,
    VonPanel_RiggingTools__Submenu_CreateControl,
    VonPanel_RiggingTools__Button_SaveNewControl,
    VonPanel_RiggingTools_Button_TEMP,
    #VonPanel_RiggingTools__Button_GeneratePresetBoneshapes,
    Von_Dropdown_AddCustomBoneshape
)

def register():
    from bpy.utils import register_class # type: ignore
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)

def unregister():
    from bpy.utils import unregister_class # type: ignore
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.my_tool



if __name__ == "__main__":
    register()
    #bpy.ops.von.popoutpanelbonesearch('INVOKE_DEFAULT')