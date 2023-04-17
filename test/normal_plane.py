import bpy
import mathutils

point = mathutils.Vector((0, 0, 0))  # Change the values to your desired point
vector = mathutils.Vector((1, 0, 0))  # Change the values to your desired vector

normal = point.cross(vector).normalized()

mesh = bpy.data.meshes.new("Plane")

verts = [
    point + (normal * -100),
    point + (normal * 100),
    point + vector + (normal * 100),
    point + vector + (normal * -100),
]

edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
faces = [(0, 1, 2, 3)]

mesh.from_pydata(verts, edges, faces)
mesh.update()

obj = bpy.data.objects.new("Plane", mesh)
bpy.context.scene.collection.objects.link(obj)
