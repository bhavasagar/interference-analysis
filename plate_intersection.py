
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

bm1 = bmesh.new()
bm1.from_mesh(obj1.data)

# Removing a object
bpy.data.objects.remove(obj2, do_unlink=True)