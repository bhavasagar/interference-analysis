# # import bpy
# # from mathutils import Vector, Matrix

# # # Define the dimensions of the cuboid
# # width = 5.0
# # length = 5.0
# # thickness = 0.1

# # # Define the orientation of the cuboid using the given vector
# # normal = Vector((0.3, 0.5, 0.8)).normalized()
# # z_axis = Vector((0.0, 0.0, 1.0))
# # rotation_matrix = normal.rotation_difference(z_axis).to_matrix().to_4x4()

# # # Create the vertices of the cuboid
# # verts = [(0, 0, 0), (0, length, 0), (width, length, 0), (width, 0, 0),
# #          (0, 0, thickness), (0, length, thickness), (width, length, thickness), (width, 0, thickness)]
# # # Create the edges of the cuboid
# # edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
# # # Create the faces of the cuboid
# # faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 7, 3), (1, 5, 4, 0), (2, 6, 5, 1), (3, 7, 6, 2)]
# # # Create the mesh
# # mesh = bpy.data.meshes.new(name='CuboidMesh')
# # mesh.from_pydata(verts, edges, faces)
# # mesh.update()

# # # Create the object
# # obj = bpy.data.objects.new(name='Cuboid', object_data=mesh)
# # bpy.context.scene.collection.objects.link(obj)


# # # Set the rotation of the object
# # obj.matrix_world = rotation_matrix

# # # Align the longest face with the normal vector
# # longest_face_idx = None
# # longest_face_area = 0.0
# # for i, face in enumerate(mesh.polygons):
# #     face_area = face.area
# #     if face_area > longest_face_area:
# #         longest_face_area = face_area
# #         longest_face_idx = i
# # longest_face_normal = mesh.polygons[longest_face_idx].normal
# # angle = longest_face_normal.angle(normal)
# # axis = longest_face_normal.cross(normal)
# # obj.rotation_mode = 'AXIS_ANGLE'
# # obj.rotation_axis_angle = (angle, axis[0], axis[1], axis[2])

# # # Set the location of the object
# # obj.location = (1.0, 1.0, 0.0)


import bpy, bmesh
from mathutils import Matrix, Vector

# Define the dimensions of the plate-like cuboid
length = 4.0
width = 3.0
height = 0.1

# Create a mesh for the plate-like cuboid
mesh = bpy.data.meshes.new(name="PlateCuboid")

# Define the vertices of the plate-like cuboid
verts = [
    (-length/2, -width/2, 0),
    (-length/2, width/2, 0),
    (length/2, width/2, 0),
    (length/2, -width/2, 0),
    (-length/2, -width/2, height),
    (-length/2, width/2, height),
    (length/2, width/2, height),
    (length/2, -width/2, height),
]

# Define the faces of the plate-like cuboid
faces = [
    (0, 1, 2, 3),
    (4, 5, 1, 0),
    (5, 6, 2, 1),
    (6, 7, 3, 2),
    (7, 4, 0, 3),
    (4, 5, 6, 7),
]

# Create the mesh from the vertices and faces
mesh.from_pydata(verts, [], faces)

# Create a new object for the plate-like cuboid
obj = bpy.data.objects.new("PlateCuboid", mesh)

# Link the object to the scene and select it
scene = bpy.context.scene
scene.collection.objects.link(obj)
obj.select_set(True)

mesh = obj.data

# Get the index of the topmost face of the mesh
# Calculate the area of each face in the mesh
face_areas = [face.area for face in mesh.polygons]

# Get the index of the face with the largest area
top_face_idx = face_areas.index(max(face_areas))

# Get the normal vector of the topmost face
normal = mesh.polygons[top_face_idx].normal.copy()

# Define the target vector to which the normal should be rotated
target = Vector((1, 1, 1))  
# Calculate the rotation matrix to align the normal with the target vector
rotation = Matrix.Rotation(normal.angle(target), 4, normal.cross(target))

# Rotate the mesh vertices and normals using the rotation matrix
mesh.transform(rotation)

# Update the mesh and object data to reflect the changes
mesh.update()
obj.data.update()

obj1 = obj
obj2 = bpy.data.objects['Cone']

mod = obj1.modifiers.new("Boolean", type='BOOLEAN')
mod.operation = 'INTERSECT'
mod.object = obj2
bpy.ops.object.modifier_apply({"object": obj1},modifier=mod.name)

bm = bmesh.new()
bm.from_mesh(obj1.data)

# Removing a object
bpy.data.objects.remove(obj2, do_unlink=True)

bm.verts.ensure_lookup_table()
bm.edges.ensure_lookup_table()
bm.faces.ensure_lookup_table()

# Get the face by index
face = bm.faces[top_face_idx]

# Get the normal vector of the face and normalize it
normal = face.normal.normalized()

# Calculate the displacement vector
displacement = normal * 1.5

# Translate the vertices of the face
for vert in face.verts:
    vert.co += displacement

# Update the mesh data and free the BMesh
bm.to_mesh(mesh)
bm.free()