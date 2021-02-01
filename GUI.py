# подгружаю необходимые библиотеки
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, \
    QPushButton, QCheckBox, QApplication, QComboBox, QLineEdit, QCompleter, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon
import sys

# устанвливаю стиль графического интерфейса
app = QApplication([])
app.setStyle('Windows')

# устанавливаю цвет текста на кнопочных элементах
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.green)
app.setPalette(palette)

# класс для отображения графического интерфейса и его элементов
class TravelWindow(QMainWindow):

    # атрибуты класса
    def __init__(self, data):
        super().__init__()
        self.company_list = data.keys()
        self.data = data
        self.init_gui()

    # функция с элементами графического интерфейса
    def init_gui(self):

        # элемент позволяющий вводить/выводить текст
        self.cost = QLineEdit()
        self.calc_value = QLineEdit()

        # подключаем к строке список данных туроператоров, при вводе первых букв названия подтягиваются варианты
        self.company = QLineEdit()
        spisok_operatorov = QCompleter(self.company_list, self.company)
        self.company.setCompleter(spisok_operatorov)

        # элемент "выпадающий список" позволяет выбрать название туроператора из всего списка мышкой без ввода текста
        self.combo = QComboBox()
        for i in self.data.keys():
            self.combo.addItem(str(i))
        self.combo.currentIndexChanged.connect(self.changeText)

        # элемент квадратик для галочки выбора валюты usd/eur
        self.check_usd = QCheckBox()
        self.check_eur = QCheckBox()

        # кнопка расчитать
        button_raschet = QPushButton('Рассчитать')
        button_raschet.clicked.connect(self.calc_cost)

        self.msgBox = QMessageBox()

        # сеточный макет отвечающий за расположение элементов внутри графического интерфейса и их отображение
        grid = QGridLayout()

    # сами элементы с их названием и координатами расположения
        # строка ввода названия туроператора
        grid.addWidget(QLabel('Введите название туроператора:'), 1, 0, 1, 4)
        grid.addWidget(self.company, 2, 0, 1, 4)

        # "выпадающий список" с озможностью выбора туроператора без ввода текста
        grid.addWidget(QLabel('Выберите туроператора из списка:'), 3, 0, 1, 4)
        grid.addWidget(self.combo, 4, 0, 1, 4)

        # элемент выбора валюты
        grid.addWidget(QLabel('USD'), 5, 0)
        grid.addWidget(self.check_usd, 5, 1)

        # элемент выбора валюты
        grid.addWidget(QLabel('EUR'), 5, 2)
        grid.addWidget(self.check_eur, 5, 3)

        # строка ввода данных в у.е для пересчета их в рубли
        grid.addWidget(QLabel('Введите данные в у.е:'), 6, 0, 1, 4)
        grid.addWidget(self.cost, 7, 0, 1, 4)

        # строка выводящая значение пересчитанное из у.е в рубли
        grid.addWidget(QLabel('Сумма в рублях:'), 8, 0, 1, 4)
        grid.addWidget(self.calc_value, 9, 0, 1, 4)

        # кнопка при нажатии на которую происходит расчет
        grid.addWidget(button_raschet, 10, 0)

        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)

        # устанавливаем параметры размера окна и его расположения при запуске программы
        self.setGeometry(300, 300, 300, 320)

        # логотип программы в левом верхнем углу
        self.setWindowIcon(QIcon('LT.png'))
        self.show()


    def changeText(self, index):
        self.company.setText(self.combo.itemText(index))

    # функция производящая пересчет значения из у.е в рубли
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

    # функция вызывает окно с вопросом о закрытии программы при попытки звкрыть ее нажав на крестик
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Работа программы будет завершена!', "Вы хотите выйти из программы?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    company_list = ['My company 1', 'My company 2', 'Your company 1']
    usd = 75
    eur = 95

    app = QApplication(sys.argv)
    window = TravelWindow(company_list, usd, eur)

    app.exec_()
