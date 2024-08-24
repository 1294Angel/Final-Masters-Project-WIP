import bpy # type: ignore

from . import (
    von_createcontrols,
    von_menu_popup,
    von_buttoncontrols
)
 
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

classes = (
    von_menu_popup.MySettings,
    von_menu_popup.VonPanel_PrimaryPanel,
    von_menu_popup.VonPanel_RiggingTools,
    von_menu_popup.VonPanel_RiggingTools__Submenu_BoneSearch,
    von_menu_popup.VonPanel_RiggingTools__Submenu_CreateControl,
    von_menu_popup.VonPanel_RiggingTools__Button_SaveNewControl,
    von_menu_popup.Von_Dropdown_AddCustomBoneshape,
    von_menu_popup.VonPanel
)
    

def menu_func(self, context):
    self.layout.operator(von_menu_popup.VonPanel)

def register():
    from bpy.utils import register_class # type: ignore
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(menu_func)
def unregister():
    from bpy.utils import unregister_class # type: ignore
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()
    #bpy.ops.von.popoutpanelbonesearch('INVOKE_DEFAULT')
