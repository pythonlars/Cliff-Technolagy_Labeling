import bpy
import os
import sys

def debug_print(message):
    """Print debug messages with line numbers"""
    print(f"[DEBUG] {message}")

def export_model_data():
    try:
        debug_print("Starting export process...")
        
        # Check if we're running in Blender
        if not hasattr(bpy, 'context'):
            debug_print("Error: This script must be run from within Blender")
            return
            
        # Get the active object (should be your model)
        obj = bpy.context.active_object
        debug_print(f"Selected object: {obj.name if obj else 'None'}")
        
        if not obj:
            debug_print("Error: No object selected. Please select your mesh model.")
            return
            
        if obj.type != 'MESH':
            debug_print(f"Error: Selected object is not a mesh. It is a {obj.type}")
            return
        
        # Get the mesh data
        mesh = obj.data
        debug_print(f"Mesh name: {mesh.name}")
        debug_print(f"Total vertices: {len(mesh.vertices)}")
        debug_print(f"Total faces: {len(mesh.polygons)}")
        
        # Use the exact path you specified
        txt_files_dir = r"C:\Users\User\OneDrive\Desktop\Labeling_system_Cliff\txtFiles"
        debug_print(f"Target directory: {txt_files_dir}")
        
        # Check if directory exists and is writable
        if not os.path.exists(txt_files_dir):
            debug_print("Directory does not exist, attempting to create...")
            try:
                os.makedirs(txt_files_dir)
                debug_print("Directory created successfully")
            except Exception as e:
                debug_print(f"Failed to create directory: {str(e)}")
                return
        
        # Check if directory is writable
        test_file = os.path.join(txt_files_dir, "test_write.txt")
        try:
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            debug_print("Directory is writable")
        except Exception as e:
            debug_print(f"Directory is not writable: {str(e)}")
            return
        
        # Export vertices
        vertices_path = os.path.join(txt_files_dir, "vertices.txt")
        debug_print(f"Exporting vertices to: {vertices_path}")
        vertex_count = 0
        try:
            with open(vertices_path, 'w') as f:
                for vertex in mesh.vertices:
                    # Get world coordinates
                    world_co = obj.matrix_world @ vertex.co
                    f.write(f"({world_co.x:.6f},{world_co.y:.6f},{world_co.z:.6f})\n")
                    vertex_count += 1
            debug_print(f"Successfully exported {vertex_count} vertices")
        except Exception as e:
            debug_print(f"Error writing vertices: {str(e)}")
            return
        
        # Export face indices
        faces_path = os.path.join(txt_files_dir, "triangle_indices.txt")
        debug_print(f"Exporting faces to: {faces_path}")
        face_count = 0
        try:
            with open(faces_path, 'w') as f:
                for face in mesh.polygons:
                    # Ensure we're dealing with triangles
                    if len(face.vertices) == 3:
                        f.write(f"{face.vertices[0]} {face.vertices[1]} {face.vertices[2]}\n")
                        face_count += 1
                    elif len(face.vertices) == 4:
                        # Split quad into two triangles
                        f.write(f"{face.vertices[0]} {face.vertices[1]} {face.vertices[2]}\n")
                        f.write(f"{face.vertices[0]} {face.vertices[2]} {face.vertices[3]}\n")
                        face_count += 2
            debug_print(f"Successfully exported {face_count} triangles")
        except Exception as e:
            debug_print(f"Error writing faces: {str(e)}")
            return
        
        print("\nExport successful!")
        print(f"Exported {vertex_count} vertices to: {vertices_path}")
        print(f"Exported {face_count} triangles to: {faces_path}")
        print(f"Total faces in mesh: {len(mesh.polygons)}")
        
    except Exception as e:
        debug_print(f"Unexpected error: {str(e)}")
        import traceback
        debug_print("Traceback:")
        debug_print(traceback.format_exc())
        print("\nPlease check the debug messages above for details.")

if __name__ == "__main__":
    export_model_data() 