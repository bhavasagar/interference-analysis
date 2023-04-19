import bpy
from mathutils import Vector

# Set the active object to the CAD model
cad_object = bpy.data.objects['Cube']

# Get the vertices of the CAD model
cad_vertices = [Vector(v.co) for v in cad_object.data.vertices]

# Set the active object to the plane you want to project onto
plane_object = bpy.data.objects['Plane']
bpy.context.view_layer.objects.active = plane_object

# Get the normal vector of the plane
plane_normal = plane_object.matrix_world.to_quaternion() @ Vector((0, 0, 1))

# Project the CAD vertices onto the plane
projected_vertices = []
for vertex in cad_vertices:
    projected_vertex = vertex - plane_normal * vertex.dot(plane_normal)
    projected_vertices.append(projected_vertex)

# Create a new mesh for the projected vertices
projected_mesh = bpy.data.meshes.new('Projected Mesh')
projected_mesh.from_pydata(projected_vertices, [], [])

# Create a new object for the projected mesh and link it to the scene
projected_object = bpy.data.objects.new('Projected Object', projected_mesh)
bpy.context.scene.collection.objects.link(projected_object)
