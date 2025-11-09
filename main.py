from __future__ import annotations

import os, subprocess, shutil
from pathlib import Path

import PIL
import lz4
import lzf
from pyexpat.errors import messages


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

def read_config(config_file):
    print("reading config...")
    with open(r"./config.txt") as config:
        settings = config.readlines()
        if len(settings) == 0:
            print("No settings found")
        print(f"settings found: \noutput dir = {settings[0]}pkg dir = {settings[1]}")
        return Path(settings[0].strip()), Path(settings[1].strip())

# output_directory = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\output")
# packages_directory = Path(r"C:\Users\Maddie\source\repos\HadesIISpriteExtractor\pkg_test")
#
#
# file_paths = find_pkgs({}, packages_directory)
#
# for file_tup in file_paths.items():
#     run_command(file_tup)

def get_and_validate_input(message: str, current: Path = None):
    valid = False
    while not valid:
        if current:
            user_input = input(f"{message}{current!r})\n>>>").strip()
        else:
            user_input = input(f"{message}\n>>>").strip()
        try:
            Path(user_input)
        except Exception as e:
            print("unable to convert input to path")
        if Path(user_input).is_dir():
            valid = True
            continue
        return Path(user_input)


def main():
    running = True

    output_directory = Path("./output").absolute()
    packages_directory = ""

    print(output_directory)

    while running:
        if Path("./config.txt").is_file():
            output_directory, packages_directory = read_config(r"./config.txt")
        else:
            print("no config file found")

        
        output_directory = get_and_validate_input("enter an output directory\n(current: ", output_directory)

        packages_directory = get_and_validate_input(r"enter a package directory (e.g. C:\Program Files (x86)\Steam\steamapps\common\Hades II\Content\Packages", packages_directory)

        running = False

if __name__ == "__main__":
    main()
