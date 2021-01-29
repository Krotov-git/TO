from cx_Freeze import setup, Executable

executables = [Executable('main.py',
targetName='for_Level_Travel.exe',
base='Win32GUI',
icon='L.ico')]

includes = ['PyQt5.QtWidgets', 'PyQt5.QtCore', 'PyQt5.QtGui', 'requests', 'bs4', 'datetime', 'sys', 'GUI', 'DB']

zip_include_packages = ['PyQt5.QtWidgets', 'PyQt5.QtCore', 'PyQt5.QtGui', 'requests', 'bs4', 'datetime', 'sys', 'GUI', 'DB']

include_files = ['L.ico', 'LT.png']

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name='for_Level.Travel',
version='1.0',
description='TO_app',
executables=executables,
options=options)