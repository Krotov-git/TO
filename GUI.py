from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, \
    QPushButton, QCheckBox, QLineEdit, QCompleter, QWidget, QApplication
import sys


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

        grid = QGridLayout()
        grid.addWidget(QLabel('Выберите Туроператора:'), 0, 0)
        grid.addWidget(self.company, 0, 1)
        grid.addWidget(QLabel('USD'), 0, 2)
        grid.addWidget(self.check_usd, 0, 3)
        grid.addWidget(QLabel('EUR'), 0, 4)
        grid.addWidget(self.check_eur, 0, 5)
        grid.addWidget(QLabel('Введите данные в у.е:'), 0, 6)
        grid.addWidget(self.cost, 0, 7)
        grid.addWidget(button_raschet, 0, 8)
        grid.addWidget(self.check_eur, 0, 9)
        grid.addWidget(self.calc_value, 0, 10)

        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)
        self.show()

    def calc_cost(self):
        value = self.cost.text()
        comp = self.company.text()
        money = 0

        if self.check_usd.checkState() == 2:
            money = self.data[comp][0] #usd
        if self.check_eur.checkState() == 2:
            money = self.data[comp][1] #eur

        value = float(value) * float(money)
        self.calc_value.setText(str(value))


if __name__ == '__main__':
    company_list = ['My company 1', 'My company 2', 'Your company 1']
    usd = 75
    eur = 95

    app = QApplication(sys.argv)
    window = TravelWindow(company_list, usd, eur)

    app.exec_()
