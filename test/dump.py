# import bpy, bmesh
# from mathutils import Vector
# import mathutils

# #obj1 = bpy.data.objects["PlateCuboid"]
# #obj2 = bpy.data.objects["Cone"]

# #mod = obj1.modifiers.new("Boolean", type='BOOLEAN')
# #mod.operation = 'INTERSECT'
# #mod.object = obj2
# #bpy.ops.object.modifier_apply({"object": obj1},modifier=mod.name)

# #bm1 = bmesh.new()
# #bm1.from_mesh(obj1.data)

# #obj = bpy.data.objects["Cube"]


# ## Define the vector to align the face with
# #vector = mathutils.Vector((0, 0, 10))

# #mesh = obj.data

# ## Find the face nearest to the object origin and whose normal is perpendicular to the z-axis
# #selected_face = None
# #selected_dist = float('inf')
# #for face in mesh.polygons:
# #    normal = face.normal
# #    if normal.dot(vector) < 0.001:
# #        continue  # skip faces that are not perpendicular to the vector
# #    point = face.center
# #    result = mathutils.geometry.intersect_line_plane(
# #        obj.location,obj.location + normal,
# #        point, normal
# #    )
# #    if result is None:
# #        # if there is no intersection point, use the object origin as a default
# #        result = obj.location
# #    dist = (result - obj.location).length
# #    if dist < selected_dist:
# #        selected_face = face
# #        selected_dist = dist

# #print(selected_face)
# ## Extrude the selected face along the vector
# #if selected_face is not None:
# #    bpy.ops.object.mode_set(mode='EDIT') # switch to edit mode
# #    bpy.ops.mesh.select_all(action='DESELECT')
# #    mesh.polygons[selected_face.index].select = True
# #    bpy.ops.mesh.extrude_region_move(
# #        MESH_OT_extrude_region={"mirror":False},
# #        TRANSFORM_OT_translate={
# #            "value": vector,
# #            "constraint_axis": (True, True, True),
# #            "mirror": False,
# #        }
# #    )
# #    bpy.ops.object.mode_set(mode='OBJECT') # switch back to object mode


# ## Define the extrusion distance
# #distance = 5.0

# #mesh = obj.data

# ## Select the face to extrude
# #face_idx = 5  # replace with the index of the face you want to extrude
# #bpy.ops.object.mode_set(mode='EDIT')
# #bpy.ops.mesh.select_all(action='DESELECT')
# #bpy.ops.mesh.select_mode(type ='FACE')
# #mesh.polygons[face_idx].select = True

# ## Extrude the selected face by the given distance
# ##bpy.ops.mesh.extrude_region_move(
# ##    MESH_OT_extrude_region={"mirror":False},
# ##    TRANSFORM_OT_translate={
# ##        "value": (0, 0, distance),
# ##        "constraint_axis": (False, False, True),
# ##        "mirror": False,
# ##        "proportional_size": 1,
# ##        "release_confirm": True,
# ##    }
# ##)
# #print(tuple(d*10 for d in mesh.polygons[face_idx].normal))
# #bpy.ops.mesh.extrude_region_move(
# #    TRANSFORM_OT_translate={"value":tuple(d*10 for d in mesh.polygons[face_idx].normal)}
# #)
# #bpy.ops.mesh.select_all(action='DESELECT')
# #bpy.ops.object.mode_set(mode='OBJECT')

# #print("END")

# import bpy

# # Add a cube to the scene
# bpy.ops.mesh.primitive_cube_add()

# # Get the mesh data of the cube
# obj = bpy.context.active_object
# mesh = obj.data

# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='DESELECT')
# bpy.ops.mesh.select_mode(type ='FACE')

# # Select the top face of the cube
# mesh.polygons[4].select = True

# # Extrude the selected face
# bpy.ops.mesh.extrude_region_move(
#     MESH_OT_extrude_region={"mirror":False},
#     TRANSFORM_OT_translate={"value":(0, 0, 10)}
# )

# # Deselect the face
# mesh.polygons[4].select = False

# # Delete the bottom face and the four side faces
# #for i in [0, 1, 2, 3, 5]:
# #    mesh.polygons[i].select = True
# #bpy.ops.mesh.delete(type='FACE')
