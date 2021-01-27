from GUI import TravelWindow
from DB import DataBase
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import sys

paths = QtCore.QCoreApplication.libraryPaths()
paths.append(".")
paths.append("platforms")
QtCore.QCoreApplication.setLibraryPaths(paths)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    data = DataBase()
    window = TravelWindow(data.get_data())

    app.exec_()
