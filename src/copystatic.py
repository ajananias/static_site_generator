import os
import shutil
def copy_contents(src, dst, log=None):
    if log is None:
        log = []
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
                log.append(f"Creating directory {dst_path}")
            copy_contents(src_path, dst_path, log)
        elif os.path.isfile(src_path):
            if not os.path.exists(os.path.dirname(dst_path)):
                os.mkdir(os.path.dirname(dst_path))
            shutil.copy(src_path, dst_path)
            log.append(f"Copying {src_path} to {dst_path}")
    return log
def clear_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path, ignore_errors=True)
        elif os.path.isfile(item_path):
            os.remove(item_path)
