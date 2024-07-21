# ------------------------------------------------------------------------
#    Import Required Controls -- NEEDS CLEANUP
# ------------------------------------------------------------------------

import bpy, json, pprint, bmesh, os, sys # type: ignore
from bpy import context # type: ignore
from bpy.types import Operator # type: ignore
from bpy_extras.object_utils import object_data_add # type: ignore
from mathutils import Vector # type: ignore
from math import radians
import pathlib

# ------------------------------------------------------------------------
#    Create General Functions
# ------------------------------------------------------------------------

def spaceconsole(temp):
    xx = temp
    while xx > 0:
        xx = xx -1
        print("")


# ------------------------------------------------------------------------
#    Create Saving Functions
# ------------------------------------------------------------------------
def create_json_data_from_mesh():
    mesh_object = bpy.context.active_object
    data = get_mesh_data(mesh_object)
    save_data(data)


def save_data(data):
    path_to_file = get_path_to_preset_mesh_data()+data["object_name"]+".json"
    with open(path_to_file, "w") as out_file_obj:
        text = json.dumps(data, indent=4)
        out_file_obj.write(text)

def saveselectedmesh():
    bpy.ops.object.editmode_toggle()
    create_json_data_from_mesh()

# ------------------------------------------------------------------------
#    Create Loading Functions
# ------------------------------------------------------------------------


def load_data(nameoffile,ispresetboneshape):
    if ispresetboneshape == True:
        path_to_file = get_path_to_preset_mesh_data()+"//"+"controls"+"//"+"InbuiltControls//"+nameoffile+".json"
    if ispresetboneshape == False:
        path_to_file = get_path_to_preset_mesh_data()+"//"+"controls"+"//"+"CustomControls//"+nameoffile+".json"
    with open(path_to_file, "r") as in_file_obj:
        text = in_file_obj.read()
        data = json.loads(text)

    return data


def get_mesh_data(mesh_object):
    bmesh_obj = bmesh.from_edit_mesh(mesh_object.data)
    face_to_vert = []
    for face in bmesh_obj.faces:
        face_verts = []
        for vert in face.verts:
            face_verts.append(vert.index)
        face_to_vert.append(face_verts)
    vert_count = len(bmesh_obj.verts)
    vert_coords = [None] * vert_count
    for vert in bmesh_obj.verts:
        vert_coords[vert.index] = list(vert.co)
    bpy.ops.object.editmode_toggle()
    data = {
        "object_name": mesh_object.name,
        "face_verts": face_to_vert,
        "vert_coordinates": vert_coords,
    }
    return data

def create_mesh_from_json_data(ispresetboneshape,shouldskeletonise,nameoffile):

    mesh_data = load_data(nameoffile,ispresetboneshape)
    create_mesh_from_data(mesh_data,shouldskeletonise)

def create_mesh_from_data(data,shouldskeletonise):

    faces = data["face_verts"]
    verts = data["vert_coordinates"]
    edges = []
    object_name = data["object_name"]

    mesh_data = bpy.data.meshes.new(f"{object_name}_data")
    mesh_data.from_pydata(verts, edges, faces)
    mesh_obj = bpy.data.objects.new(object_name, mesh_data)
    bpy.context.collection.objects.link(mesh_obj)
    
    
    
    if shouldskeletonise == True:
        bpy.ops.object.editmode_toggle()
        
        bpy.ops.mesh.select_all(action = 'SELECT')
        bpy.ops.mesh.delete(type='ONLY_FACE')

        bpy.ops.object.editmode_toggle()

# ------------------------------------------------------------------------
#    Create Multiuse Functions
# ------------------------------------------------------------------------

def getobjectdata(controldata):
    file = open(controldata+'.txt')
    
def getfolderloc():
    dir = os.path.dirname(bpy.data.filepath)
    if not dir in sys.path:
        sys.path.append(dir)
    return(dir)

def get_path_to_folderloc():
    spaceconsole(10)
    meshdatafile = str(getfolderloc())
    print()
    spaceconsole(10)
    return meshdatafile

def get_path_to_preset_mesh_data():
    meshdatafile = str(getfolderloc())+"//"+"controls"+"//"+"InbuiltControls//" #+"/"+str(controlname)+".json"
    return meshdatafile
#E:\Masters Wor\FinalMastersProject\Final-Masters-Project-WIP\Addon\VonTools\Addon Creation\controls\TESTSAVE

def organisetocontrolscollection(createdobjectname):
    collectiontomoveto = "Controls Collection"
    collectionexists = False


    #Check if the controls collection already exists and add it in (In a way that is visible to the user in the default viewport outliner) if it doesn't
    for collections in bpy.data.collections:
        if collections.name == collectiontomoveto:
            collectionexists = True
            break
    
    if collectionexists == True:
        print("Collection Exists")
    object = bpy.context.active_object
    if collectionexists == False:
        #Create And Link Custom Collection
        collection = bpy.data.collections.new(collectiontomoveto)
        bpy.context.scene.collection.children.link(collection)
    

    collectiontomoveto = bpy.data.collections[collectiontomoveto]

    bpy.context.collection.objects.unlink(object)
    
    collectiontomoveto.objects.link(object)







# ------------------------------------------------------------------------
#    Test Controls
# ------------------------------------------------------------------------

