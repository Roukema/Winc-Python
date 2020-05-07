import os
import shutil


def get_dir(path):
    for (filepath, x, file_name) in os.walk(path):
        return file_name


# get_dir(r"C:\Users\matth\Desktop\Winc\python-test-file\files\files")

# 2

files_path = r"C:\Users\matth\Desktop\Winc\python-test-file\files\files"
files = get_dir(files_path)
juf = r"C:\Users\matth\Desktop\Winc\python-test-file\juf"
rest = r"C:\Users\matth\Desktop\Winc\python-test-file\rest"

# test of het een veelvoud van 7 is


def veelvoud_van_7(file):
    file_name = file[: file.find(".")]

    if int(file_name) % 7 == 0:
        return True
    else:
        return False


def move_file_7(files, juf, rest, files_path):
    for file in files:
        if veelvoud_van_7(file) or "7" in file:
            shutil.move(f"{files_path}\\{file}", juf)
            print("move to", (f"{files_path}\\{file}", juf))
        else:
            shutil.move(f"{files_path}\\{file}", rest)
            print("move to", (f"{files_path}\\{file}", rest))


def move_files_back(juf, rest, files_path):
    juf_files = get_dir(juf)
    rest_files = get_dir(rest)
    for file in juf_files:
        shutil.move(f"{juf}\\{file}", files_path)
        print(f"{juf}\\{file}", files_path)
    for file in rest_files:
        shutil.move(f"{rest}\\{file}", files_path)
        print(f"{rest}\\{file}", files_path)


def where_are_the_files():
    if files == []:
        move_files_back(juf, rest, files_path)
        print("files moved back")
    else:
        move_file_7(files, juf, rest, files_path)
        print("files seperated")


where_are_the_files()
