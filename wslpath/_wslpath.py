import subprocess
from pathlib import Path
from typing import Union


def wslpath(path: Union[str, Path], *,
            force_absolute_path: bool = False,
            from_wsl_path_to_windows_path: bool = False,
            use_forward_slash: bool = False) -> Union[str, Path]:
    """
    Translates Windows path to WSL path

    Expands the user directory (~) and runs the 'wslpath' command
    from the WSL environment with 'path' as it's argument.

    Args:
        path: Path to translate
        force_absolute_path: Force result to absolute path format
        from_wsl_path_to_windows_path: Translate WSL path to a Windows path
        use_forward_slash: Use '/' instead of backslash in Windows path.
            Only used if from_wsl_path_to_windows_path is True.

    Returns:
        A translated path of the same type as 'path' argument.
    """

    if not (isinstance(path, str) or isinstance(path, Path)):
        raise ValueError(
            f"{path} must be 'str' or 'pathlib.Path' instance"
        )

    # for some reason we need to expand user directory ourselves
    expanduser_path = Path(path).expanduser()

    try:
        args = []
        if force_absolute_path:
            args.append('-a')
        if from_wsl_path_to_windows_path:
            args.append('-m' if use_forward_slash else '-w')

        # check = True raises exception if the command did not run successfully
        completed = subprocess.run(
            ['wslpath', *args, str(expanduser_path)],
            text=True, capture_output=True, check=True)
    except FileNotFoundError:
        raise RuntimeError(
            "The 'wslpath' command was not found. "
            "Are you sure you are executing this in the wsl environment?"
        )

    output = completed.stdout.strip()
    if isinstance(path, str):
        return output
    else:
        return Path(output)
