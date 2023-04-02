import bpy
import bmesh
from mathutils.geometry import intersect_point_line, distance_point_to_plane
from mathutils.geometry import intersect_ray_tri
from mathutils import Vector

obj1 = bpy.data.objects['base_link']
obj2 = bpy.data.objects['obj2']

# Get the meshes of the two objects
mesh1 = bpy.data.objects['base_link'].to_mesh()
mesh2 = bpy.data.objects['obj2'].to_mesh()

# # Create a BMesh object for each mesh
# bm1 = bmesh.new()
# bm1.from_mesh(mesh1)
# bm2 = bmesh.new()
# bm2.from_mesh(mesh2)

# # Intersect the two BMesh objects
# intersect = bpy.ops.mesh.intersect_boolean(bm1, bm2, operation='INTERSECT')

# # Calculate the volume of the intersection
# volume = 0.0
# for face in intersect['geom']:
#     if isinstance(face, bmesh.types.BMFace):
#         # Calculate the centroid of the face
#         centroid = Vector((0.0, 0.0, 0.0))
#         for v in face.verts:
#             centroid += v.co
#         centroid /= len(face.verts)

#         # Project the centroid onto the plane of the face
#         normal = face.normal
#         d = -centroid.dot(normal)
#         projected_centroid = intersect_point_line(centroid, Vector((0.0, 0.0, 1.0)), normal)
#         distance_to_plane = distance_point_to_plane(projected_centroid, centroid, normal)

#         # Calculate the volume of the pyramid formed by the face and the projected centroid
#         area = face.calc_area()
#         height = distance_to_plane
#         volume += area * height / 3.0

# # Free the BMesh objects
# bm1.free()
# bm2.free()

# # Print the volume of the intersection
# print("Volume of intersection:", volume)

# # Free the meshes
# bpy.data.meshes.remove(mesh1)
# bpy.data.meshes.remove(mesh2)


# Apply a boolean modifier to intersect the two objects
mod = obj1.modifiers.new("Boolean", type='BOOLEAN')
mod.operation = 'INTERSECT'
mod.object = obj2
bpy.ops.object.modifier_apply(modifier="Boolean")

# Calculate the volume of the resulting mesh
volume = 0
for poly in obj1.data.polygons:
    for i in range(len(poly.vertices)):
        v1 = obj1.data.vertices[poly.vertices[i]].co
        v2 = obj1.data.vertices[poly.vertices[(i+1)%len(poly.vertices)]].co
        v3 = obj1.data.vertices[poly.vertices[(i+2)%len(poly.vertices)]].co
        for poly2 in obj2.data.polygons:
            for j in range(len(poly2.vertices)):
                w1 = obj2.data.vertices[poly2.vertices[j]].co
                w2 = obj2.data.vertices[poly2.vertices[(j+1)%len(poly2.vertices)]].co
                w3 = obj2.data.vertices[poly2.vertices[(j+2)%len(poly2.vertices)]].co
                print(v1, v2-v1, w1, w2-w1)
                result, location = intersect_ray_tri(v1, v2-v1, w1, w2-w1, Vector(0,0,0))
                if result:
                    result, location = intersect_ray_tri(v2, v3-v2, w1, w2-w1, Vector(0,0,0))
                    if result:
                        result, location = intersect_ray_tri(v3, v1-v3, w1, w2-w1, Vector(0,0,0))
                        if result:
                            volume += poly.area * (v1-v2).dot((v3-v2).cross(w1-w2))/6

# Print the volume
print("Intersection volume: ", volume)



import bpy
import bmesh
from mathutils.geometry import intersect_point_line, distance_point_to_plane
from mathutils.geometry import intersect_ray_tri
from mathutils import Vector

def print(*data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")

# Get the objects
obj1 = bpy.data.objects['base_link']
obj2 = bpy.data.objects['obj2']

# Create a BMesh object for each mesh

# bm2 = bmesh.new()
# bm2.from_mesh(mesh2)
bm = bmesh.new()
bm.from_mesh(bpy.data.objects['base_link'].to_mesh())
print("Volume of", obj1.name, "is", bm.calc_volume())

# Intersect the two BMesh objects
mod = obj1.modifiers.new("Boolean", type='BOOLEAN')
mod.operation = 'INTERSECT'
mod.object = obj2
bpy.ops.object.modifier_apply(modifier="Boolean")
# # # Get the resulting BMesh object
# # bm_int = boolean['result']
# volume = 0
# for poly in obj1.data.polygons:
#     for i in range(len(poly.vertices)):
#         v1 = obj1.data.vertices[poly.vertices[i]].co
#         v2 = obj1.data.vertices[poly.vertices[(i+1)%len(poly.vertices)]].co
#         v3 = obj1.data.vertices[poly.vertices[(i+2)%len(poly.vertices)]].co
#         for poly2 in obj2.data.polygons:
#             for j in range(len(poly2.vertices)):
#                 w1 = obj2.data.vertices[poly2.vertices[j]].co
#                 w2 = obj2.data.vertices[poly2.vertices[(j+1)%len(poly2.vertices)]].co
#                 w3 = obj2.data.vertices[poly2.vertices[(j+2)%len(poly2.vertices)]].co
#                 print(v1, v2-v1, w1, w2-w1)
#                 result = intersect_ray_tri(v1, v2-v1, w1, w2-w1, Vector((0,0,0)), True)
#                 if result:
#                     result = intersect_ray_tri(v2, v3-v2, w1, w2-w1, Vector((0,0,0)), True)
#                     if result:
#                         result = intersect_ray_tri(v3, v1-v3, w1, w2-w1, Vector((0,0,0)), True)
#                         if result:
#                             volume += poly.area * (v1-v2).dot((v3-v2).cross(w1-w2))/6

# # Print the volume
# print("Intersection volume: ", volume)

bm1 = bmesh.new()
bm1.from_mesh(bpy.data.objects['base_link'].to_mesh())

# Print the volume of the object
print("Volume of", obj1.name, "is", bm1.calc_volume())