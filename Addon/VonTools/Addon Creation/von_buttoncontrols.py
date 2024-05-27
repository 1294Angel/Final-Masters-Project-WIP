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

import bpy
import sys 
import os

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

import von_buttoncontrols
import imp
imp.reload(von_buttoncontrols)

#import functions
from von_buttoncontrols import *


# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------

class MySettings(PropertyGroup):

    my_bool : BoolProperty(
        name="Enable or Disable",
        description="A bool property",
        default = False
        )

    my_int : IntProperty(
        name = "Set a value",
        description="A integer property",
        default = 23,
        min = 10,
        max = 100
        )

    my_float : FloatProperty(
        name = "Set a value",
        description = "A float property",
        default = 23.7,
        min = 0.01,
        max = 30.0
        )
        
    bonebeingsearched: StringProperty(
        name="String",
        description="",
        default="",
        maxlen=1024,
        )

# ------------------------------------------------------------------------
#    Operators
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

        row.label(text= "Rigging Tools", icon= 'CUBE')
        layout.prop(mytool, "my_bool", text="Didthiswork????")
        layout.operator("von.popoutpanelbonesearch('INVOKE_DEFAULT')")     

class VonPanel_RiggingTools__Submenu_BoneSearch(bpy.types.Operator):
    bl_idname = "von.popoutpanelbonesearch"
    bl_label = "Bone Search"
    
    text : bpy.props.StringProperty(name="Enter Text", default="")
    def execute(self, context):
        text = self.text
        searchforbone(text)
        return {'FINISHED'}
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    MySettings,
    VonPanel_PrimaryPanel,
    VonPanel_RiggingTools,
    VonPanel_RiggingTools__Submenu_BoneSearch
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.my_tool



if __name__ == "__main__":
    register()
    #bpy.ops.von.popoutpanelbonesearch('INVOKE_DEFAULT')