import os
import random
import pathlib 

def gen_id() -> int:
    return random.randrange(1 << 30, 1 << 31)
    
def get_extension(path: str) -> str:
    return pathlib.Path(path).suffix

def get_files_in_path(path: str, ext: str | None = None) -> list[str]:
    files = os.listdir(path)
    out_files = []
    for file in files:
        if os.path.isdir(file):
            continue
        if ext == None:
            out_files.append(file)
        elif get_extension(file) == ext:
            out_files.append(file)

    return out_files

