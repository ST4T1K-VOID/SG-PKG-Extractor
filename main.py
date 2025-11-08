from __future__ import annotations

import os, subprocess, shutil
from pathlib import Path

import PIL
import lz4
import lzf

def find_pkgs(pkg_list: dict[str: Path], directory: Path) -> dict[str:Path]:
    if directory.is_dir():
        for file in os.listdir(directory):
            if file.endswith(".pkg"):
                pkg_list[file[:-4]] = Path(os.path.join(directory, file))
                print(f"Package found: {file}")
            elif Path(directory, file).is_dir():
                # if dir, go into 'sub dir '
                pkg_list = find_pkgs(pkg_list, Path(f"{directory}/{file}"))
        return pkg_list

def run_command(file: tuple[str, Path], output_directory: Path):
    command = f'deppth ex "{file[1]}"'
    subprocess.run(command)
    move_directory(file, output_directory)

def move_directory(file: tuple[str, Path], output_dir: Path = r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\output"):
    extract = str(file[1])
    print(f"moving extracted files: {file[1]} to output directory")
    shutil.move(Path(extract[:-4]), Path(output_dir, file[0]))

output_directory = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\output")
packages_directory = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\pkg_test")


file_paths = find_pkgs({}, packages_directory)

for file_tup in file_paths.items():
    run_command(file_tup)
