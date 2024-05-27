# extend Python's functionality to work with file paths
import pathlib

# give Python access to Blender's functionality
import bpy # type: ignore

#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________


def link_blend_file_objects(blend_file_path, link=False):
    """link the blender file objects into the current blender file"""
    with bpy.data.libraries.load(blend_file_path, link=link) as (data_from, data_to):
        data_to.collections = data_from.collections

    scene = bpy.context.scene

    # link the objects into the scene collection
    for obj in data_to.objects:
        if obj is None:
            continue

        scene.collection.objects.link(obj)


def link_blend_file_scenes(blend_file_path, link=False):
    """link the blender file scenes into the current blender file"""
    with bpy.data.libraries.load(blend_file_path, link=link) as (data_from, data_to):
        data_to.scenes = data_from.scenes


def link_blend_file_materials(blend_file_path, link=False):
    """link the blender file materials into the current blender file"""
    with bpy.data.libraries.load(blend_file_path, link=link) as (data_from, data_to):

        for material_name in data_from.materials:
            if "blue" in material_name:
                data_to.materials.append(material_name)

def place_objects_into_collection(temp_coll_name):
    bpy.data.collections.new(name=temp_coll_name)

#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________


def main():

    # define the path to the blend file
    blend_file_path = "//blend/controls.blend"

    link_blend_file_objects(blend_file_path, link=False)
    
    place_objects_into_collection("Controls")

    #update scene to reflect changes
    bpy.context.view_layer.update()

#____________________________________________________________________________________________
#____________________________________________________________________________________________
#____________________________________________________________________________________________


main()