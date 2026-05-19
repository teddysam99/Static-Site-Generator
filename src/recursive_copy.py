import os
import shutil

def copy_source_to_destination(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    recur_copy(source, destination)

def recur_copy(src, dst):
    for item in os.listdir(src):
        src_path = os.path.join(src,item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            print(f" * {src_path} -> {dst_path}")
            shutil.copy(src_path,dst_path)
        else:
            os.mkdir(dst_path)
            recur_copy(src_path,dst_path)
    
