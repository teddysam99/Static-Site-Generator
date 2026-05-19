import os
import shutil
import pathlib
from generate_page import generate_page

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

def generate_pages_recursive(dir_path_content,template_path, dest_dir_path,base_path):
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if not os.path.isfile(from_path):
            generate_pages_recursive(from_path,template_path,dest_path,base_path)
        else:
            if pathlib.Path(from_path).suffix == ".md":
                dest_path = pathlib.Path(dest_path).with_suffix(".html")
                generate_page(from_path,template_path,dest_path,base_path)



