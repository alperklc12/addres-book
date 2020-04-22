from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QMessageBox,
                             QLineEdit, QComboBox, QTextEdit)
from PyQt5.QtGui import (QFont, QPixmap)
import database, persons

btn_font = QFont('Arial', 12)
letter_font = QFont('Arail', 12)


class ViewPerson(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('View Persons')
        self.setFixedSize(self.size())
        self.interface_gui_fn()

    def interface_gui_fn(self):
        header = QLabel('View Persons', self)
        header.setFont(letter_font)
        header.move(150, 50)

        header_img = QLabel(self)
        header_img.setPixmap(QPixmap('images/person.png'))
        header_img.move(60, 25)

        self.name_line = QLineEdit(self)
        self.name_line.resize(200, 30)
        self.name_line.move(60, 120)
        self.name_line.setFont(letter_font)
        self.name_line.setReadOnly(True)

        self.age_box = QComboBox(self)
        self.age_box.move(60, 160)
        self.age_box.setFont(letter_font)
        for i in range(18, 65):
            self.age_box.addItem(str(i))
        self.age_box.setDisabled(True)

        self.addres_txt = QTextEdit(self)
        self.addres_txt.move(60, 200)
        self.addres_txt.setFont(letter_font)
        self.addres_txt.setReadOnly(True)

        try:
            data = database.get_one_fn(persons.per_id_for_fn)
            self.name_line.setText(data[1])
            self.age_box.setCurrentText(data[2])
            self.addres_txt.setText(data[3])

        except Exception as e:
            print(e)
