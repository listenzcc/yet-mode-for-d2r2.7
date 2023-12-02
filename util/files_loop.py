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

for path in tqdm(paths):
    content = open(path, 'rb').read()
    lines = [e.strip().split(b'//')[0] for e in content.split(b'\r\n')]
    lines = [e.decode() for e in lines]


# %% ---- 2023-12-02 ------------------------
# Play ground


# %% ---- 2023-12-02 ------------------------
# Pending


# %% ---- 2023-12-02 ------------------------
# Pending
