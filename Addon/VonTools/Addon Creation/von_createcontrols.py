# ------------------------------------------------------------------------
#    Import Required Controls
# ------------------------------------------------------------------------

import bpy, json, pprint, bmesh, os, sys # type: ignore
from bpy import context # type: ignore
from bpy.types import Operator # type: ignore
from bpy_extras.object_utils import object_data_add # type: ignore
from mathutils import Vector # type: ignore
from math import radians
import pathlib

# ------------------------------------------------------------------------
#    Create Functions
# ------------------------------------------------------------------------

def spaceconsole(temp):
    xx = temp
    while xx > 0:
        xx = xx -1
        print("")


def savenewcontrol(shouldoverride):
    objs = bpy.context.selected_objects
    folderlocation = str(getfolderloc() + "\controls/")


    for x in objs:
        vertexlist = []
        edgeslist = []
        faceslist = []
        spaceconsole(3)
        print(x.name)
        bpy.ops.object.mode_set(mode='EDIT')
        mesh = bpy.context.view_layer.objects.active.data
        bm = bmesh.from_edit_mesh(mesh)
        # get a reference to the active object
        mesh_obj = bpy.context.active_object
        # create a new bmesh
        bm = bmesh.from_edit_mesh(mesh_obj.data)
        selected_verts = [vert for vert in bm.verts if vert.select]


        for vert in bm.verts:
            vl=[]
            for l in vert.link_edges:
                vl.append(l.other_vert(vert).index)
            vertexlist.append(vert.co)
            edgeslist.append(vl)
        print(edgeslist)
        print(vertexlist)

        # clean up/free memory that was allocated for the bmesh
        bm.free()


        #WRITE TO FOLDER
        with open(folderlocation +str(x.name) +'.txt','w') as tfile:
            tfile.write(str(vertexlist)+'\n')
            tfile.write(str(edgeslist)+'\n')
        bpy.ops.object.mode_set(mode='OBJECT')

def getobjectdata(controldata):
    file = open(controldata+'.txt')
    
def getfolderloc():
    dir = os.path.dirname(bpy.data.filepath)
    if not dir in sys.path:
        sys.path.append(dir )
    return(dir)

def createobject(cntrltoimport, context, self):
    mesh = bpy.data.meshes.new(name=cntrltoimport)
    file = open(cntrltoimport+'.txt')
    verts = [Vector((-1.0, -1.0, 1.812609314918518)), Vector((1.0, -1.0, 1.812609314918518)), Vector((-1.0, 1.0, 1.812609314918518)), Vector((1.0, 1.0, 1.812609314918518))]
    edges = [[2, 1], [0, 3], [0, 3], [1, 2]]
    faces = []
    mesh.from_pydata(verts, edges, faces)
    object_data_add(context,mesh,operator=self) # type: ignore
# ------------------------------------------------------------------------
#    Test Controls
# ------------------------------------------------------------------------