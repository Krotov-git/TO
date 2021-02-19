
# setup.py - файл неучаствующий в логике и процессах программы,
# необходим лишь для компиляцию ее в конечный продукт который можно устанавливать на других компьютерах

# подгружаю необходимые библиотеки
from cx_Freeze import setup, Executable

# устанавливаем параметры
executables = [Executable('main.py',
                           targetName='for_Level_Travel.exe', # название программы отображающееся в левом верхнем углу
                            base='Win32GUI',
                            icon='L.ico')]

# записываем сюда все используемые в коде библиотеки
includes = ['PyQt5.QtWidgets',
            'PyQt5.QtCore',
            'PyQt5.QtGui',
            'requests',
            'bs4',
            'datetime',
            'sys',
            'GUI',
            'DB']

zip_include_packages = ['PyQt5.QtWidgets',
                        'PyQt5.QtCore',
                        'PyQt5.QtGui',
                        'requests',
                        'bs4',
                        'datetime',
                        'sys',
                        'GUI',
                        'DB']

# прописываем название и расширение дополнительных файлов им=спользуемых в программе, расположенные в корне проекта
include_files = ['L.ico', 'LT.png']

options = {'build_exe': {'include_msvcr': True,
                         'includes': includes,
                         'zip_include_packages': zip_include_packages,
                         'build_exe': 'build_windows',
                         'include_files': include_files}}

setup(name='for_Level.Travel',
      version='1.0',
      description='TO_app',
      executables=executables,
      options=options)