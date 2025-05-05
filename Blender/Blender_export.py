import bpy
import bmesh
import os

# Path to save the index file
output_path = r"C:\Users\User\OneDrive\Desktop\txtFiles\triangle_indices.txt"

def save_triangle_indices(obj, file_path):
    if obj.type != 'MESH':
        print("Selected object is not a mesh.")
        return

    # Duplicate the mesh to avoid modifying original
    temp_mesh = obj.data.copy()
    temp_obj = bpy.data.objects.new("TempMesh", temp_mesh)
    bpy.context.collection.objects.link(temp_obj)

    # Enter edit mode on the temporary object
    bpy.context.view_layer.objects.active = temp_obj
    bpy.ops.object.mode_set(mode='EDIT')

    # Use BMesh to triangulate the mesh
    bm = bmesh.from_edit_mesh(temp_mesh)
    bmesh.ops.triangulate(bm, faces=bm.faces[:])
    bmesh.update_edit_mesh(temp_mesh)

    # Switch back to object mode to access triangulated data
    bpy.ops.object.mode_set(mode='OBJECT')

    # Extract face indices
    face_data = []
    for face in temp_mesh.polygons:
        if len(face.vertices) == 3:
            face_data.append(tuple(face.vertices))

    # Clean up temp object
    bpy.data.objects.remove(temp_obj, do_unlink=True)

    # Save to file
    with open(file_path, 'w') as f:
        for face in face_data:
            f.write(f"{face[0]} {face[1]} {face[2]}\n")

    print(f"Saved {len(face_data)} triangle faces to:\n{file_path}")

# Run on selected object
selected = bpy.context.active_object
if selected:
    save_triangle_indices(selected, output_path)
else:
    print("No object selected.")
