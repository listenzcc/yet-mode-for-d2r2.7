"""
File: main.py
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
from util.files_loop import *


# %% ---- 2023-12-02 ------------------------
# Function and class

# Disable the stupid level sound
disable_path(
    Path(ROOT, 'yte.mpq/Data/hd/global/sfx/cursor/cursor_level_up_1_hd.flac')
)

# Disable all the waypoint portals particles
disable_path(
    Path(ROOT, 'yte.mpq/Data/hd/objects/waypoint_portals')
)

# Disable all the room tails particles
disable_path(
    Path(ROOT, 'yte.mpq/Data/hd/roomtiles')
)

# %%
files = select_by_pattern(
    'data/hd/vfx/particles/overlays/object/horadric_light/FX_Horadric_Light.particles')
print(files)

# Disable all the non-loot particles
df = files.query('nLines > 10').query('not Disabled')
df['Path'].map(disable_path)
print(df)


# %% ---- 2023-12-02 ------------------------
# Play ground


# %% ---- 2023-12-02 ------------------------
# Pending


# %% ---- 2023-12-02 ------------------------
# Pending
