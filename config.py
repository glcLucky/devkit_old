# -*- coding: utf-8 -*-

"""
config.py

解析配置文件

@author: Jasper Gui
@email: jasper.gui@outlook.com
@date: 2017.05.19
"""

import os


# --------------- MODULE DENPENDENCY ---------------

_DEPENDENCIES = [
    "termcolor",
    "pywintypes",
    "win32com",
]


# --------------- FOLDER PATH ---------------

# ~/<module>
_FOLDER = os.path.split(os.path.realpath(__file__))[0]
