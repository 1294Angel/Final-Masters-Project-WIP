# ------------------------------------------------------------------------
#    Import Required Controls
# ------------------------------------------------------------------------

import bpy, bmesh, os, self, context # type: ignore
from bpy.types import Operator # type: ignore
from bpy_extras.object_utils import object_data_add # type: ignore
from mathutils import Vector # type: ignore
from math import radians

# ------------------------------------------------------------------------
#    Create Functions
# ------------------------------------------------------------------------

def spaceconsole(temp):
    xx = temp
    while xx > 0:
        xx = xx -1
        print("")


def createnewcontrol(shouldoverride):
    objs = bpy.context.selected_objects
    for x in objs:
        spaceconsole(3)
        print(x.name)
        bpy.ops.object.mode_set(mode='EDIT')
        mesh = bpy.context.view_layer.objects.active.data
        bm = bmesh.from_edit_mesh(mesh)
        for vert in bm.verts:
            vl=[]
            vertex = []
            edges = []
            for l in vert.link_edges:
                vl.append(l.other_vert(vert).index)
                vertex.append(vert.co)
                edges.append(vl)
        print(os.path.dirname(os.path.abspath(__file__)))
        with open(str(x.name) +'.txt','w') as tfile:
            tfile.write(str(x.name) + '\n')
            tfile.write("verts = "+str(vertex)+'\n')
            tfile.write("edges = "+str(edges)+'\n')
            tfile.write("faces = []")

        bpy.ops.object.mode_set(mode='OBJECT')

def getobjectdata(controldata):
    file = open(controldata+'.txt')
    

def createobject(cntrltoimport):
    mesh = bpy.data.meshes.new(name=cntrltoimport)
    file = open(cntrltoimport+'.txt')
    verts = cntrltoimport[1]
    edges = cntrltoimport[2]
    faces= []
    mesh.from_pydata(verts, edges, faces)
    object.validate(verbose=True)
    object_data_add(context,mesh,operator=self)
# ------------------------------------------------------------------------
#    Test Controls
# ------------------------------------------------------------------------

"""spaceconsole(10)
createnewcontrol(True)"""

#createobject("Cube")

createnewcontrol(True)