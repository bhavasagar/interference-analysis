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
bpy.ops.object.modifier_apply({"object": obj1},modifier=mod.name)

bm1 = bmesh.new()
bm1.from_mesh(bpy.data.objects['base_link'].data)

# Print the volume of the object
print("Volume of", obj1.name, "is", bm1.calc_volume(signed=True))