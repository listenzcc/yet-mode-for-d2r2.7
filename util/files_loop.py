"""
File: files_loop.py
Author: Chuncheng Zhang
Date: 2023-12-02
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-12-02 ------------------------
# Requirements and constants
from . import *

mpq = ROOT.joinpath('yte.mpq')

assert mpq.is_dir(), f'Invalid folder: {mpq}'

# %% ---- 2023-12-02 ------------------------
# Function and class

paths = []
for node in tqdm(os.walk(mpq)):
    for e in node[-1]:
        if e.endswith('.json'):
            paths.append(Path(node[0], e))


def select_by_pattern(pattern: str):
    pattern = pattern.lower()
    selects = []

    for path in tqdm(paths):
        raw = open(path, 'rb').read()
        lines1 = [e.strip().decode('utf-8', errors='ignore')
                  for e in raw.split(b'\r\n')]
        lines = [e for e in lines1 if pattern in e.lower()]

        if not lines:
            continue

        disabled = path.name.endswith('-disabled.json')
        selects.append((path, path.name, disabled, len(lines), pattern))

    df = pd.DataFrame(selects, columns=[
                      'Path', 'Name', 'Disabled', 'nLines', 'Pattern'])

    return df


def disable_path(path: Path):
    if not path.exists():
        return

    ext = '' if path.is_dir() else path.suffix

    if path.name.endswith(f'-disabled{ext}'):
        # Only deal with enabled files
        return

    # Rename
    src = path
    dst = Path(
        path.parent,
        path.name.replace(f'{ext}', f'-disabled{ext}')
        if path.is_file() else path.name + '-disabled'
    )
    os.rename(src, dst)
    print(f'{src} -> {dst}')
    return dst


def enable_path(path: Path):
    if not path.exists():
        return

    ext = '' if path.is_dir() else path.suffix

    if not path.name.endswith(f'-disabled{ext}'):
        # Only deal with disabled files
        return

    # Rename
    src = path
    dst = Path(
        path.parent,
        path.name.replace(f'-disabled{ext}', f'{ext}')
    )
    os.rename(src, dst)
    print(f'{src} -> {dst}')
    return dst

# %% ---- 2023-12-02 ------------------------
# Play ground


# %% ---- 2023-12-02 ------------------------
# Pending


# %% ---- 2023-12-02 ------------------------
# Pending
