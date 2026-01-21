from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, \
    QRadioButton

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 300)
main_win.setWindowTitle("Конкурс від Crazy People")

question = QLabel('''Тут є 6 каналів вибраних мною, які розкривають різні тематики у своїх відео. 
У якого з каналів найбільша кількість підписників? (Дані взяті зі сайту Маніфест)''')

button_1 = QRadioButton('Dima Maleev (IT)')  # 137000
button_2 = QRadioButton('Patron The Dog (Анімація)')  # 161000
button_3 = QRadioButton('Хлопці з лісу (Військова справа)')  # 226000
button_4 = QRadioButton('Останній Капіталіст (Гроші та фінанси)')  # 241000
button_5 = QRadioButton('Леви на джипі (Гумор)')  # 984000
button_6 = QRadioButton('Ukranimaua (Для дітей)')  # 203000

main_layout = QVBoxLayout()
line_h_1 = QHBoxLayout()
line_h_2 = QHBoxLayout()
line_h_3 = QHBoxLayout()
line_h_4 = QHBoxLayout()

line_h_1.addWidget(question, alignment=Qt.AlignmentFlag.AlignCenter)
line_h_2.addWidget(button_1, alignment=Qt.AlignmentFlag.AlignCenter)
line_h_2.addWidget(button_2, alignment=Qt.AlignmentFlag.AlignCenter)
line_h_3.addWidget(button_3, alignment=Qt.AlignmentFlag.AlignCenter)
line_h_3.addWidget(button_4, alignment=Qt.AlignmentFlag.AlignCenter)
line_h_4.addWidget(button_5, alignment=Qt.AlignmentFlag.AlignCenter)
line_h_4.addWidget(button_6, alignment=Qt.AlignmentFlag.AlignCenter)

main_layout.addLayout(line_h_1)
main_layout.addLayout(line_h_2)
main_layout.addLayout(line_h_3)
main_layout.addLayout(line_h_4)


def show_victory():
    victory_win = QMessageBox()
    victory_win.setWindowTitle("Повідомлення")
    victory_win.setText('''Правильно! У каналу "Леви на джипі" найбільша кількість підписників!''')
    victory_win.exec()


def show_lose():
    lose_win = QMessageBox()
    lose_win.setWindowTitle("Повідомлення")
    lose_win.setText("Не правильно! Спробуй ще раз!")
    lose_win.exec()


button_1.clicked.connect(show_lose)
button_2.clicked.connect(show_lose)
button_3.clicked.connect(show_lose)
button_4.clicked.connect(show_lose)
button_5.clicked.connect(show_victory)
button_6.clicked.connect(show_lose)


main_win.setLayout(main_layout)
main_win.show()
app.exec()
