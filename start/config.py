config = {
    "directory": "./.vscode",
    "settings": {
        "files": {
            "windows": "./start/vscode/settings-windows.json",
            "unix": "./start/vscode/settings-unix.json",
        },
        "target": "./.vscode/settings.json",
    },
    "files": {
        "extensions": "./start/vscode/extensions.json",
        "launch": "./start/vscode/launch.json",
        "tasks": "./start/vscode/tasks.json",
        "cspell": "./start/vscode/cspell.json",
        "env": "./.env.example",
    },
    "target": {
        "extensions": "./.vscode/extensions.json",
        "launch": "./.vscode/launch.json",
        "tasks": "./.vscode/tasks.json",
        "cspell": "./.vscode/cspell.json",
        "env": "./.env",
    },
}
