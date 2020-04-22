from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QMessageBox,
                             QLineEdit, QComboBox, QTextEdit)
from PyQt5.QtGui import (QFont, QPixmap)
import database

btn_font = QFont('Arial', 12)
letter_font = QFont('Arail', 12)


class AddPerson(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Add Persons')
        self.setFixedSize(self.size())
        self.interface_gui_fn()

    def interface_gui_fn(self):
        header = QLabel('Add Persons', self)
        header.setFont(letter_font)
        header.move(150, 50)

        header_img = QLabel(self)
        header_img.setPixmap(QPixmap('images/add.png'))
        header_img.move(60, 25)

        self.name_line = QLineEdit(self)
        self.name_line.resize(200, 30)
        self.name_line.move(60, 120)
        self.name_line.setPlaceholderText('Name')
        self.name_line.setFont(letter_font)

        self.age_box = QComboBox(self)
        self.age_box.move(60, 160)
        self.age_box.setFont(letter_font)
        for i in range(18, 65):
            self.age_box.addItem(str(i))

        self.addres_txt = QTextEdit(self)
        self.addres_txt.move(60, 200)
        self.addres_txt.setFont(letter_font)
        self.addres_txt.setPlaceholderText('Enter your adress.')

        add_btn = QPushButton('Save', self)
        add_btn.setFont(btn_font)
        add_btn.move(204, 400)
        add_btn.clicked.connect(self.save_fn)

    def save_fn(self):
        name = self.name_line.text()
        age = self.age_box.currentText()
        adres = self.addres_txt.toPlainText()

        if name and age and adres is not None:
            try:
                database.save_fn(name, age, adres)
                QMessageBox.information(self, 'Info', '{}, has been added!'.format(name.capitalize()))
            except Exception as e:
                QMessageBox.information(self, 'Alert!!!', 'Data could not be added! ' + str(e))
            finally:
                self.name_line.setText('')
                self.addres_txt.setText('')
                self.age_box.setCurrentIndex(0)
        else:
            QMessageBox.information(self, 'Alert!!!', 'Entered missing data!!!')
