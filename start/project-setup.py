import os
import shutil
from config import config


class Init:
    def __init__(self) -> None:
        self.create_dir(config["directory"])
        if os.name == "nt":
            self.copy_file(
                config["settings"]["files"]["windows"],
                config["settings"]["target"],
            )
        else:
            self.copy_file(
                config["settings"]["files"]["unix"],
                config["settings"]["target"],
            )

        for file in config["files"]:
            self.copy_file(config["files"][file], config["target"][file])

    def create_dir(self, directory: str) -> None:
        try:
            if not os.path.isdir(directory):
                os.mkdir(directory)
                print("Directory '% s' created" % directory)
        except OSError:
            print("Creation of the directory % s failed" % directory)

    def copy_file(self, file: str, target: str) -> None:
        if os.path.isfile(target):
            print("File '% s' found" % target)
            return None
        shutil.copy(file, target)
        print("File '% s' copied" % target)


Init()
