from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, \
    QPushButton, QCheckBox, QApplication, QComboBox, QLineEdit, QCompleter, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon
import sys


app = QApplication([])
app.setStyle('Windows')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.green)
app.setPalette(palette)



class TravelWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.company_list = data.keys()
        self.data = data
        self.init_gui()

    def init_gui(self):

        button_raschet = QPushButton('Рассчитать')
        button_raschet.clicked.connect(self.calc_cost)

        self.check_usd = QCheckBox()
        self.check_eur = QCheckBox()

        self.cost = QLineEdit()
        self.calc_value = QLineEdit()

        self.company = QLineEdit()
        spisok_operatorov = QCompleter(self.company_list, self.company)
        self.company.setCompleter(spisok_operatorov)

        self.combo = QComboBox()
        for i in self.data.keys():
            self.combo.addItem(str(i))
        self.combo.currentIndexChanged.connect(self.changeText)
        
        grid = QGridLayout()

        grid.addWidget(QLabel('Введите название туроператора:'), 1, 0, 1, 4)
        grid.addWidget(self.company, 2, 0, 1, 4)
        grid.addWidget(QLabel('Выберите туроператора из списка:'), 3, 0, 1, 4)
        grid.addWidget(self.combo, 4, 0, 1, 4)
        grid.addWidget(QLabel('USD'), 5, 0)
        grid.addWidget(self.check_usd, 5, 1)
        grid.addWidget(QLabel('EUR'), 5, 2)
        grid.addWidget(self.check_eur, 5, 3)
        grid.addWidget(QLabel('Введите данные в у.е:'), 6, 0, 1, 4)
        grid.addWidget(self.cost, 7, 0, 1, 4)
        grid.addWidget(QLabel('Сумма в рублях:'), 8, 0, 1, 4)
        grid.addWidget(self.calc_value, 9, 0, 1, 4)
        grid.addWidget(button_raschet, 10, 0)

        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)
        self.setGeometry(300, 300, 300, 320)
        self.setWindowIcon(QIcon('LT.png'))
        self.show()


    def changeText(self, index):
        self.company.setText(self.combo.itemText(index))

    def calc_cost(self):
        value = self.cost.text()
        comp = self.company.text()
        money = 0

        if self.check_usd.checkState() == 2:
            money = self.data[comp][0] #usd
        if self.check_eur.checkState() == 2:
            money = self.data[comp][1] #eur

        value = round(float(value) * float(money), 2)
        self.calc_value.setText(str(value))


if __name__ == '__main__':
    company_list = ['My company 1', 'My company 2', 'Your company 1']
    usd = 75
    eur = 95

    app = QApplication(sys.argv)
    window = TravelWindow(company_list, usd, eur)

    app.exec_()
