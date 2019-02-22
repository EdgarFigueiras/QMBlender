import bpy
import os

bpy.ops.object.duplicates_make_real()
bpy.ops.object.join()

filename = bpy.path.basename(bpy.context.blend_data.filepath)

blend_file_path = filepath = "/Users/edgarfigueiras/Desktop/models/" + str(filename) + ".obj"
directory = os.path.dirname(blend_file_path)
target_file = os.path.join(directory, str(filename) + ".obj")

bpy.ops.export_scene.obj(filepath=target_file)
