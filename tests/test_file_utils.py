# create these files before in a docker container

from tools.file_utils.file_utils_tool import move_file, delete_file, read_file
import os

def test_move_and_read_file():
    with open("temp.txt", "w") as f:
        f.write("hello")

    result = move_file("temp.txt", "testdir/moved.txt")
    assert "successfully" in result

    content = read_file("testdir/moved.txt")
    assert content == "hello"

    delete_result = delete_file("testdir/moved.txt")
    assert "deleted" in delete_result