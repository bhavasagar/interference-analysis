import bpy
import mathutils

# Get a reference to the object to project
obj = bpy.context.object

# Get a reference to the plane to project onto
plane = bpy.data.objects['MyPlane']

# Get the normal and point of the plane
n = plane.data.polygons[0].normal
p = plane.location

# Create a new mesh to store the projected vertices and faces
new_mesh = bpy.data.meshes.new(name='ProjectedMesh')

# Project each vertex of the object onto the plane
projected_verts = []
for v in obj.data.vertices:
    proj_v = v.co - n.dot(v.co - p) * n
    projected_verts.append(proj_v)

# Create new faces from the projected vertices
projected_faces = []
for f in obj.data.polygons:
    verts = f.vertices
    # Use the projected vertices instead of the original vertices
    proj_verts = [projected_verts[i] for i in verts]
    projected_faces.append(proj_verts)

# Set the new mesh's vertices and faces
new_mesh.from_pydata(projected_verts, [], projected_faces)

# Create a new object to represent the projected mesh
projected_obj = bpy.data.objects.new(name='ProjectedObject', object_data=new_mesh)

# Add the new object to the scene
bpy.context.scene.objects.link(projected_obj)
