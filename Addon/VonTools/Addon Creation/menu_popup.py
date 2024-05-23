#Import Python Basics
import bpy


#Import .py classes





class CustomMenu(bpy.types.Menu):
    bl_label = "Custom Menu"
    bl_idname = "OBJECT_MT_custom_menu"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Vona's Rigging Tools", icon='KEYTYPE_EXTREME_VEC')
        layout.operator("mesh.primitive_cylinder_add", text="Intialize Addon")
        layout.label(text="Common Shortcuts", icon='INFO')

        layout.operator("object.shade_smooth", text="Shade Smooth")
        layout.operator("object.shade_flat", text="Shade Flat")
        



        # use an operator enum property to populate a sub-menu
        """layout.operator_menu_enum("object.select_by_type",
                                  property="type",
                                  text="Select All by Type",
                                  )"""

        # call another menu
        #layout.operator("wm.call_menu", text="Unwrap").name = "VIEW3D_MT_uv_map"


def draw_item(self, context):
    layout = self.layout
    layout.menu(CustomMenu.bl_idname)


def register():
    bpy.utils.register_class(CustomMenu)

    # lets add ourselves to the main header
    bpy.types.INFO_HT_header.append(draw_item)


def unregister():
    bpy.utils.unregister_class(CustomMenu)

    bpy.types.INFO_HT_header.remove(draw_item)


if __name__ == "__main__":
    register()

    # The menu can also be called from scripts
    bpy.ops.wm.call_menu(name=CustomMenu.bl_idname)