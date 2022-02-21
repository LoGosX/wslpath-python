import subprocess
from pathlib import Path
from typing import Union, Any


def _wslpath(path: Union[str, Path], /,
             force_absolute_path=False,
             from_wsl_path_to_windows_path=False) -> Union[str, Path]:

    return_type: Any
    if isinstance(path, str):
        return_type = str
    elif isinstance(path, Path):
        return_type = Path
    else:
        raise ValueError(
            f"{path} is expected to be of type 'str' or 'pathlib.Path'"
        )

    # for some reason we need to expand user directory ourselves
    path = Path(path).expanduser()

    try:
        args = []
        if force_absolute_path:
            args.append('-a')
        if from_wsl_path_to_windows_path:
            args.append('-w')

        # check = True raises exception if the command did not run successfully
        completed = subprocess.run(
            ['wslpath', *args, str(path)],
            text=True, capture_output=True, check=True)
    except FileNotFoundError:
        raise RuntimeError("The 'wslpath' command was not found. "
              "Are you sure you are executing this in the wsl environment?")

    return return_type(completed.stdout.strip())
