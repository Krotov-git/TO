# подгружаю необходимые библиотеки
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, \
    QPushButton, QCheckBox, QApplication, QComboBox, QLineEdit, QCompleter, QWidget, \
    QMessageBox, QTableWidget, QTableWidgetItem, QTableView, QHeaderView, QHBoxLayout, QFormLayout, QGroupBox, \
    QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon
import sys



# устанвливаю стиль графического интерфейса
app = QApplication([])
app.setStyle('Windows')

# устанавливаю цвет текста на кнопочных элементах
# palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.green)
# app.setPalette(palette)

# класс для отображения графического интерфейса и его элементов
class TravelWindow(QMainWindow):
    # атрибуты класса
    def __init__(self, db_TO):
        super().__init__()
        self.company_list = db_TO.keys()
        self.data = db_TO
        self.init_gui()

    # функция с элементами графического интерфейса
    def init_gui(self):

        # элемент позволяющий вводить/выводить данные
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

        # кнопка вывести данные
        button_table = QPushButton('Вывести данные')
        button_table.clicked.connect(self.spisok_data_to)

        self.msgBox = QMessageBox()

        # таблица данных ТО
        self.table = QTableWidget()
        #self.table.setFixedHeight(250)
        #self.table.setFixedWidth(200)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(self.data))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.setHorizontalHeaderLabels(["Имя ТО", "USD", "EUR", "Дата"])

        # сеточный макет отвечающий за расположение элементов внутри графического интерфейса и их отображение
        grid = QGridLayout()

    # сами элементы с их названием и координатами расположения

        # первая координата, строка в сетке
        # вторая координата, столбец в сетке
        # третья координата, на сколько строк растягивается элемент
        # четвертая координата, на сколько столбцов растягивается элемент

        # строка ввода названия туроператора
        grid.addWidget(QLabel('Введите имя ТО:'), 0, 4, 1, 2)
        grid.addWidget(self.company, 1, 4, 1, 2)

        # "выпадающий список" с озможностью выбора туроператора без ввода текста
        grid.addWidget(QLabel('Выберите имя ТО:'), 2, 4, 1, 2)
        grid.addWidget(self.combo, 3, 4, 1, 2)

        # элемент выбора валюты
        grid.addWidget(QLabel('USD'), 4, 4, 1, 1)
        grid.addWidget(self.check_usd, 5, 4, 1, 1)

        # элемент выбора валюты
        grid.addWidget(QLabel('EUR'), 4, 5, 1, 1)
        grid.addWidget(self.check_eur, 5, 5, 1, 1)

        # строка ввода данных в у.е для пересчета их в рубли
        grid.addWidget(QLabel('Введите данные в у.е:'), 6, 4, 1, 2)
        grid.addWidget(self.cost, 7, 4, 1, 2)

        # строка выводящая значение пересчитанное из у.е в рубли
        grid.addWidget(QLabel('Сумма в рублях:'), 8, 4, 1, 2)
        grid.addWidget(self.calc_value, 9, 4, 1, 2)

        # кнопка при нажатии на которую происходит расчет
        grid.addWidget(button_raschet, 10, 4, 1, 2)

        # кнопка при нажатии на которую происходит вывод данных то в таблицу
        grid.addWidget(button_table, 10, 0, 1, 2)

        # таблица данных ТО
        grid.addWidget(QLabel('Данных курсов ТО с датой (для сверки)'), 0, 0, 1, 2)
        grid.addWidget(self.table, 1, 0, 9, 2)

        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)

        # устанавливаем параметры размера окна и его расположения при запуске программы
        self.setGeometry(300, 300, 470, 350)  # первые два значения расположение окна программы н экране при запуске
                                              # последние два значения ширина и высота окна программы

        # логотип программы в левом верхнем углу
        self.setWindowIcon(QIcon('LT.png'))

        # отлавливает сигналы установки галочек в чекбоксе и позволяет исключать одновременную установку обоих параметров
        self.check_usd.stateChanged.connect(self.state_usd)
        self.check_eur.stateChanged.connect(self.state_eur)

        self.show()

    def state_usd(self):
        if self.check_usd.checkState() == 2:
            self.check_eur.setCheckState(0)

    def state_eur(self):
        if self.check_eur.checkState() == 2:
            self.check_usd.setCheckState(0)

    def changeText(self, index):
        self.company.setText(self.combo.itemText(index))

    # функция производящая пересчет значения из у.е в рубли
    def calc_cost(self):
        value = self.cost.text()
        comp = self.company.text()
        money = 0

        if self.check_usd.checkState() == 2:
            try:
                money = self.data[comp][0] #usd
            except:
                self.calc_value.setText("Введено некорректное имя ТО")

        if self.check_eur.checkState() == 2:
            try:
                money = self.data[comp][1] #eur
            except:
                self.calc_value.setText("Введено некорректное имя ТО")

        try:
            if float(value) >= 0:
                value = round(float(value) * float(money), 2)
                self.calc_value.setText(str(value))
            else:
                self.calc_value.setText("Введено отрицательное число!")
        except:
            self.calc_value.setText("Введены НЕ числовые данные!")

    # функция заполняет таблицу данными ТО
    def spisok_data_to(self):
        indicator_name = 0   # счетчик, участвует в добавление названия ТО каждый раз в новую строку
        indicator_usd = []  # список, выполняет роль счетчика, участвует в добавление курса usd ТО каждый раз в новую строку
        indicator_eur = []  # список, выполняет роль счетчика, участвует в добавление курса eur ТО каждый раз в новую строку
        indicator_date = []  # список, выполняет роль счетчика, участвует в добавление даты курса ТО каждый раз в новую строку
        for i in self.data:
            self.table.setItem(indicator_name, 0, QTableWidgetItem(i))
            indicator_name += 1

            indicator_if = 0  # счетчик, условия добавления данных
            js = []   # список, данных ТО, по индексу выбираем usd, eur, date
            for j in self.data[i]:
                js.append(j)
                if indicator_if == 0:
                    self.table.setItem(len(indicator_usd), 1, QTableWidgetItem(str(js[0])))
                    indicator_usd.append(j)
                if indicator_if == 1:
                    self.table.setItem(len(indicator_eur), 2, QTableWidgetItem(str(js[1])))
                    indicator_eur.append(j)
                if indicator_if == 2:
                    jss = js[2]
                    self.table.setItem(len(indicator_date), 3, QTableWidgetItem(str(jss[2:])))
                    indicator_date.append(j)
                indicator_if += 1


    # функция вызывает окно с вопросом о закрытии программы при попытки звкрыть ее нажав на крестик
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Работа программы будет завершена!', "Вы хотите выйти из программы?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    company_list = {'key': 'My company 1'}
    company_list = {'My company 1': [70, 85]}

    window = TravelWindow(company_list)
    app = QApplication(sys.argv)

    app.exec_()
