import os, subprocess
from pathlib import Path

class Extract:
    def __init__(self, output_dir: Path = "./"):
        self.output_dir = output_dir

    def extract(self, files):
        for pkg in files:
            if not os.path.isfile(pkg):
                print(f"file dir not found: {pkg}")
            else:
                subprocess.run(f"deppth ex {pkg}")

    def append_file_path(self, file_paths):
        for path in file_paths:
            print(path)
            correction_path = Path("./../")
            if os.path.isfile(os.path.join(correction_path, path)):
                print("yes!!")
