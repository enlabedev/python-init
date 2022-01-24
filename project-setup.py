import os
import shutil


class Init:
    def __init__(self) -> None:
        self.config = {
            "directory": "./.vscode",
            "settings": {
                "files": {
                    "windows": "vscode/settings-windows.json",
                    "unix": "vscode/settings-unix.json",
                },
                "target": ".vscode/settings.json",
            },
            "files": {
                "extensions": "vscode/extensions.json",
                "launch": "vscode/launch.json",
                "tasks": "vscode/tasks.json",
                "cspell": "vscode/cspell.json",
            },
            "target": {
                "extensions": ".vscode/extensions.json",
                "launch": ".vscode/launch.json",
                "tasks": ".vscode/tasks.json",
                "cspell": ".vscode/cspell.json",
            },
        }
        self.create_dir(self.config["directory"])
        if os.name == "nt":
            self.copy_file(
                self.config["settings"]["files"]["windows"],
                self.config["settings"]["target"],
            )
        else:
            self.copy_file(
                self.config["settings"]["files"]["unix"],
                self.config["settings"]["target"],
            )

        for file in self.config["files"]:
            self.copy_file(self.config["files"][file], self.config["target"][file])

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
