import os
import shutil

def move_file(src: str, dest: str) -> str:
    try:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(src, dest)
        return "File moved successfully."
    except Exception as e:
        return f"Error: {e}"

def delete_file(path: str) -> str:
    try:
        os.remove(path)
        return "File deleted."
    except Exception as e:
        return f"Error: {e}"

def read_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"