from cx_Freeze import setup, Executable

executables = [Executable('main.py',
targetName='for_Level_Travel.exe',
base='Win32GUI',
icon='z.ico')]


includes = ['QApplication', 'QMainWindow', 'QGridLayout', 'QLabel', 'QPushButton', 'QCheckBox', 'QLineEdit', 'QCompleter', 'QWidget', 'QApplication', 'sys', 'requests', 'BeautifulSoup', 'datetime', 'GUI', 'DB']

zip_include_packages = ['QApplication', 'QMainWindow', 'QGridLayout', 'QLabel', 'QPushButton', 'QCheckBox', 'QLineEdit', 'QCompleter', 'QWidget', 'QApplication', 'sys', 'requests', 'BeautifulSoup', 'datetime', 'GUI', 'DB']

include_files = ['L.ico']

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name=' main',
version='1.0',
description='TO_app',
executables=executables,
options=options)