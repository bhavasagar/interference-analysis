import bpy

# Get references to the objects to intersect
obj1 = bpy.data.objects['Sphere']
obj2 = bpy.data.objects['Cylinder']

# Set the active object to obj1
bpy.context.view_layer.objects.active = obj1

# Enter Edit mode
bpy.ops.object.mode_set(mode='EDIT')

# Select all vertices in obj1
bpy.ops.mesh.select_all(action='SELECT')

# Use the Boolean intersection operator
bpy.ops.mesh.intersect_boolean(operation='INTERSECT', threshold=0.0001, solver='EXACT')

# Exit Edit mode
bpy.ops.object.mode_set(mode='OBJECT')

# Create a new object to hold the intersection
mesh_int = bpy.data.meshes.new("Intersection")
mesh_int.from_pydata(obj1.data.vertices[:], [], obj1.data.polygons[:])
obj_int = bpy.data.objects.new("Intersection", mesh_int)
bpy.context.collection.objects.link(obj_int)

