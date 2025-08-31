from pathlib import Path

def _list_modules():
    mod_dir = Path(__file__).resolve().parent
    return [
        file.stem
        for file in mod_dir.glob("*.py")
        if file.is_file() and file.name != "__init__.py"
    ]

all_modules = frozenset(sorted(_list_modules()))
