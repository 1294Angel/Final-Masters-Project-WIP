# extend Python's functionality to work with JSON files
import json

# extend Python's functionality to work with file paths
import os
import pathlib

# extend Python's functionality to print data in a readable way
import pprint
import sys

# give Python access to Blender's functionality
import bpy # type: ignore

# give Python access to Blender's mesh editing functionality
import bmesh # type: ignore


def delete_all_objects():
    """Removing all of the objects from the scene"""
    # make sure that we are in object mode
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
            bpy.ops.object.mode_set(mode="OBJECT")

    # select all object in the scene
    bpy.ops.object.select_all(action="SELECT")

    # delete all selected objects in the scene
    bpy.ops.object.delete()


def get_mesh_data(mesh_object):


    """Extract the vert indices that make up each face and the vert coordinates"""


    bmesh_obj = bmesh.from_edit_mesh(mesh_object.data)

    # extract the vert indices that make up each face
    face_to_vert = []
    for face in bmesh_obj.faces:
        face_verts = []
        for vert in face.verts:
            face_verts.append(vert.index)
        face_to_vert.append(face_verts)

    # initialize a list with the same size as the vert count
    vert_count = len(bmesh_obj.verts)
    vert_coords = [None] * vert_count
    # extract the vert coordinates
    for vert in bmesh_obj.verts:
        vert_coords[vert.index] = list(vert.co)

    # exit edit mode
    bpy.ops.object.editmode_toggle()

    # create a dictionary with the mesh data
    data = {
        "object_name": mesh_object.name,
        "face_verts": face_to_vert,
        "vert_coordinates": vert_coords,
    }

    pprint.pprint(data)

    return data

def getfolderloc():
    dir = os.path.dirname(bpy.data.filepath)
    if not dir in sys.path:
        sys.path.append(dir )
    return(dir)

def get_path_to_mesh_data():
    return "E:\Masters Wor\FinalMastersProject\Final-Masters-Project-WIP\Addon\VonTools\Addon Creation\controls\TESTSAVE/testfile.json"
#E:\Masters Wor\FinalMastersProject\Final-Masters-Project-WIP\Addon\VonTools\Addon Creation\controls\TESTSAVE


def save_data(data):
    path_to_file = get_path_to_mesh_data()

    # open the json file for writing and dump the data in text form
    with open(path_to_file, "w") as out_file_obj:
        # convert the dictionary into text
        text = json.dumps(data, indent=4)
        # write the text into the file
        out_file_obj.write(text)


def create_json_data_from_mesh():

    # bpy.ops.mesh.primitive_cube_add()
    mesh_object = bpy.context.active_object

    data = get_mesh_data(mesh_object)

    save_data(data)


def load_data():
    path_to_file = get_path_to_mesh_data()

    # @todo: it is best to test that the file exists on disk before doing this
    # open the json file for reading and read the text from it
    with open(path_to_file, "r") as in_file_obj:
        text = in_file_obj.read()
        # convert the text into a dictionary
        data = json.loads(text)

    return data


def create_mesh_from_data(data,shouldskeletonise):

    # using code from this tutorial https://www.youtube.com/watch?v=mN3n9b98HMk
    # to create a mesh from faces and vert coordinates
    faces = data["face_verts"]
    verts = data["vert_coordinates"]
    edges = []

    object_name = data["object_name"]

    # create a mesh from the vert, edge, and face data
    mesh_data = bpy.data.meshes.new(f"{object_name}_data")
    mesh_data.from_pydata(verts, edges, faces)

    # create a object using the mesh data
    mesh_obj = bpy.data.objects.new(object_name, mesh_data)

    bpy.context.collection.objects.link(mesh_obj)
    
    
    
    if shouldskeletonise == True:
        bpy.ops.object.editmode_toggle()
        
        bpy.ops.mesh.select_all(action = 'SELECT')
        bpy.ops.mesh.delete(type='ONLY_FACE')

        bpy.ops.object.editmode_toggle()

def create_mesh_from_json_data(shouldskeletonise):

    mesh_data = load_data()
    create_mesh_from_data(mesh_data,)


def saveselectedmesh():
    bpy.ops.object.editmode_toggle()
    create_json_data_from_mesh()

