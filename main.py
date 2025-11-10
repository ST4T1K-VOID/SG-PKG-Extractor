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
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"Err: command could not be run: {e}")
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
            return
        print(f"settings found")
        output_path = Path(settings[0].strip()).absolute()
        return output_path

def get_and_validate_input(message: str, current: Path = None):
    valid = False
    while not valid:
        if current:
            user_input = input(f"{message}{current!r})\n>>> ").strip()
        else:
            user_input = input(f"{message}\n>>> ").strip()

        try:
            user_input = r"{}".format(user_input)
            Path(user_input)
        except Exception as e:
            print("unable to convert input to path")

        if Path(user_input).is_dir():
            valid = True
            return Path(user_input)
        else:
            print("path is not valid")



def main():
    running = True

    output_directory = ""
    packages_directory = ""

    print(output_directory)

    while running:
        if Path("./config.txt").is_file():
            output_directory = read_config(r"./config.txt") or Path("./output").absolute()
        else:
            print("no config file found")

        dirs_valid = False
        while not dirs_valid:
            u_input = input(f"enter output directory? current: {output_directory}\n[y/n] >>> ").lower()
            if u_input == 'y':
                output_directory = None
                while not output_directory:
                    # bandaid fix
                    user_input = input(f"enter an output directory\n(current: {output_directory})\n>>> ")
                    user_input = r"{}".format(user_input)
                    try:
                        user_input = Path(user_input)
                    except:
                        pass

                    if isinstance(user_input, Path):
                        output_directory = user_input

            while not packages_directory:
                packages_directory = get_and_validate_input(r"enter a package directory (e.g. C:....\Program Files (x86)\Steam\steamapps\common\Hades II\Content\Packages", packages_directory)


            # # possibly unneeded
            # if output_directory.is_dir() and packages_directory.is_dir():
            #     dirs_valid = True
            # elif not output_directory.is_dir() and  packages_directory.is_dir():
            #     print("Err: output directory is not valid")
            # elif output_directory.is_dir() and not packages_directory.is_dir():
            #     print("Err: packages directory is not valid")
            # else:
            #     print("Err: output directory and packages directory is not valid")

            file_paths = {}
            file_paths = find_pkgs(file_paths, packages_directory)

            if not file_paths:
                print("Err: no valid (.pkg) files found")
            else:
                for file_tup in file_paths.items():
                    run_command(file_tup, output_directory)

            print("Extraction complete")

            u_input = input(f"extract more packages?\n[y/n] >>> ").lower()
            # NOTE: not  working ???
            if u_input != 'y':
                running = False
    # NOTE: not  working ???
    with open("./config.txt", 'w') as file:
        print("writing output dir to file...")
        file.truncate()
        file.write(str(output_directory))

    print("quitting...")
    quit(0)

if __name__ == "__main__":
    main()
