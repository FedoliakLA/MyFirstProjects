from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.resize(300, 200)
main_win.setWindowTitle("Визначник переможця")
button = QPushButton("Згенерувати")
text = QLabel("Натисни, щоб дізнатися переможця")
winner = QLabel("?")

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignmentFlag.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignmentFlag.AlignCenter)
line.addWidget(button, alignment = Qt.AlignmentFlag.AlignCenter)
main_win.setLayout(line)
def show_peremoga():
    number = randint(1, 100)
    winner.setText(str(number))
    text.setText("Переможець:")
button.clicked.connect(show_peremoga)
main_win.show()
app.exec()
