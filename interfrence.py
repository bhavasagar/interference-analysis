import bpy
import bmesh
from mathutils.bvhtree import BVHTree

# Treshold volume is used to prevent bad CAD files from being analyzed as overlaps.
TRESHOLD_VOLUME = 10**(-2)


def print(*data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(
                    override, text=str(data), type="OUTPUT")


# Get the objects
obj1 = bpy.data.objects['base_link']
obj2 = bpy.data.objects['obj2']


def CalculateVolumeofOverlap(obj1, obj2):
    # TODO: Copy the object 1 before applying boolean operation
    # Intersect the two BMesh objects
    mod = obj1.modifiers.new("Boolean", type='BOOLEAN')
    mod.operation = 'INTERSECT'
    mod.object = obj2
    bpy.ops.object.modifier_apply({"object": obj1}, modifier=mod.name)

    bm1 = bmesh.new()
    bm1.from_mesh(obj1.data)

    intersection_volume = bm1.calc_volume(signed=True)

    # Print the volume of the object
    print("Volume of", obj1.name, "is", intersection_volume)
    return intersection_volume


def OverlapCheck(obj1, obj2):
    # Get their world matrix
    mat1 = obj1.matrix_world
    mat2 = obj2.matrix_world

    # Get the geometry in world coordinates
    vert1 = [mat1 @ v.co for v in obj1.data.vertices]
    poly1 = [p.vertices for p in obj1.data.polygons]

    vert2 = [mat2 @ v.co for v in obj2.data.vertices]
    poly2 = [p.vertices for p in obj2.data.polygons]

    # Create the BVH trees
    bvh1 = BVHTree.FromPolygons(vert1, poly1)
    bvh2 = BVHTree.FromPolygons(vert2, poly2)

    inter = bvh1.overlap(bvh2)
    print(bvh1)

    # Test if overlap.
    if inter != []:
        intrersection_volume = CalculateVolumeofOverlap(obj1, obj2)
        if intrersection_volume > TRESHOLD_VOLUME:
            print("Overlap")
        else:
            print("Touching")

    else:
        print("No overlap or touching")


if __name__ == "__main__":
    OverlapCheck(obj1, obj2)
