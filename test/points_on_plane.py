import bpy
import mathutils

# Set the name of the object and the plane
object_name = "Cone"
plane_origin = mathutils.Vector((0, 0, 0))
plane_normal = mathutils.Vector((0, 0, 1))

# Get the object and its vertices
obj = bpy.data.objects[object_name]
vertices = obj.data.vertices

# Get the points of the object on the plane
points_on_plane = []
for vert in vertices:
    world_vert = obj.matrix_world @ vert.co
    projection = world_vert - plane_normal.dot(world_vert - plane_origin) * plane_normal
    if projection.z == 0:
        points_on_plane.append(projection)

print("###")
# Print the points
for point in points_on_plane:
    print(point)
