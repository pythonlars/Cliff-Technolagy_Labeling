import bpy
from mathutils import Vector


def duplicate_and_move_right(reference_obj, offset=0.1):
    # Duplicate the reference object
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = reference_obj
    reference_obj.select_set(True)
    bpy.ops.object.duplicate()
    duplicated = bpy.context.active_object

    # Calculate width (x-axis) of the reference object
    bbox = [reference_obj.matrix_world @ Vector(corner) for corner in reference_obj.bound_box]
    min_x = min(v.x for v in bbox)
    max_x = max(v.x for v in bbox)
    width = max_x - min_x

    # Move duplicated to the right
    duplicated.location.x += width + offset

    print(f"Duplicated '{reference_obj.name}' -> '{duplicated.name}' and moved right by {width:.2f} units.")
    return duplicated


def slice_horizontally(obj):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Calculate center Z
    bbox = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    min_z = min(v.z for v in bbox)
    max_z = max(v.z for v in bbox)
    center_z = (min_z + max_z) / 2.0

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bisect(
        plane_co=(0, 0, center_z),
        plane_no=(0, 0, 1),
        clear_inner=False,
        clear_outer=True
    )
    bpy.ops.object.mode_set(mode='OBJECT')
    print(f"Sliced '{obj.name}' horizontally at Z={center_z:.2f}")


def slice_vertically(obj):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Calculate center X
    bbox = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    min_x = min(v.x for v in bbox)
    max_x = max(v.x for v in bbox)
    center_x = (min_x + max_x) / 2.0

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    # Slice along vertical plane (cut along X-axis direction)
    bpy.ops.mesh.bisect(
        plane_co=(center_x, 0, 0),
        plane_no=(1, 0, 0),  # Plane facing positive X
        clear_inner=False,
        clear_outer=True
    )
    bpy.ops.object.mode_set(mode='OBJECT')
    print(f"Sliced '{obj.name}' vertically at X={center_x:.2f}")


def main():
    if bpy.context.active_object is None or bpy.context.active_object.type != 'MESH':
        print("Error: Please select a mesh object.")
        return

    original = bpy.context.active_object

    # 1st duplication and horizontal slice
    first_copy = duplicate_and_move_right(original)
    slice_horizontally(first_copy)

    # 2nd duplication from the first copy and horizontal slice
    second_copy = duplicate_and_move_right(first_copy)
    slice_horizontally(second_copy)

    # 3rd duplication from the second copy and vertical slice
    third_copy = duplicate_and_move_right(second_copy)
    slice_vertically(third_copy)


# Run the main function
main()