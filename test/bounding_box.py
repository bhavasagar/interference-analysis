import bpy
import bmesh
import mathutils

# Get the active object
obj = bpy.data.objects["Cube"]

# Get the object's world matrix
matrix = obj.matrix_world

# Get the object's vertices in local coordinates
vertices = [matrix @ v.co for v in obj.data.vertices]

# Create a bounding box object from the vertices
bm = bmesh.new()
bm.from_mesh(obj.data)
bbox = mathutils.bvhtree.BVHTree.FromBMesh(bm)

# Calculate the bounding box center and dimensions
center = sum(vertices, mathutils.Vector()) / len(vertices)
size = mathutils.Vector([max(vertices, key=lambda v: v[i])[i] - min(vertices, key=lambda v: v[i])[i] for i in range(3)])

# Get the object's rotation matrix
rotation = matrix.to_3x3()

# Calculate the object's oriented bounding box
obb_center = matrix @ center
obb_dimensions = rotation @ size
obb_rotation = matrix.to_quaternion()

# Print the results
print("OBB center:", obb_center)
print("OBB dimensions:", obb_dimensions)
print("OBB rotation:", obb_rotation)


# Normal bb

import bpy
from mathutils import Vector

obj = bpy.context.object
mesh = obj.data

min_x, min_y, min_z = (float("inf"),) * 3
max_x, max_y, max_z = (-float("inf"),) * 3

for vertex in mesh.vertices:
    v = obj.matrix_world @ vertex.co
    if v.x < min_x:
        min_x = v.x
    if v.x > max_x:
        max_x = v.x
    if v.y < min_y:
        min_y = v.y
    if v.y > max_y:
        max_y = v.y
    if v.z < min_z:
        min_z = v.z
    if v.z > max_z:
        max_z = v.z

bbox_center = Vector((
    (max_x + min_x) / 2,
    (max_y + min_y) / 2,
    (max_z + min_z) / 2,
))

print(bbox_center)
bbox_size = Vector((max_x - min_x, max_y - min_y, max_z - min_z))
print(bbox_size)


bbox = bpy.data.objects.new("BoundingBox", None)
bbox.location = bbox_center
bbox.scale = bbox_size
bpy.context.scene.collection.objects.link(bbox)
