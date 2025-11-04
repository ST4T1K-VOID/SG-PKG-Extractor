import os, subprocess, shutil
from pathlib import Path

import PIL
import lz4
import lzf



output_dir = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\output")
packages_dir = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\pkg_test")


file_paths = {}
for file in os.listdir(packages_dir):
    if file.endswith(".pkg"):
        file_paths[file[:-4]] = (Path(os.path.join(packages_dir, file)))

for k,v in file_paths.items():
    print(f"key: {k}, value: {v}")

test_pkg = file_paths["Ares"]

print(test_pkg)

command = f'deppth ex "{test_pkg}"'

print(command)

# subprocess.run(command)

# convert path to string, remove .pkg, convert pack to path
dir = Path(str(test_pkg)[:-4])


print(dir)

path1 = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\pkg_test\Ares")
path2 = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\output\Ares")

print(path1)
print(path2)

command = f'mv "{path1}" "{path2}"'

print(command)

if os.path.isdir(path1):
    print("P1 hello")

if os.path.isdir(path2):
    print("P2 hello")

shutil.move(path1, path2)

# subprocess.run(command)

# for pkg in file_paths:
#     if not os.path.isfile(pkg):
#         print(f"file dir not found: {pkg}")
#     else:
#         subprocess.run(f"deppth ex {pkg} {output_dir}")

# extract = Extract(output_dir)
#
# extract.append_file_path(file_paths)
