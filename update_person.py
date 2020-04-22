from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QMessageBox,
                             QLineEdit, QComboBox, QTextEdit)
from PyQt5.QtGui import (QFont, QPixmap)
import database, persons

btn_font = QFont('Arial', 12)
letter_font = QFont('Arail', 12)


class UpdatePerson(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Update Persons')
        self.setFixedSize(self.size())
        self.interface_gui_fn()

    def interface_gui_fn(self):
        header = QLabel('Update Persons', self)
        header.setFont(letter_font)
        header.move(150, 50)

        header_img = QLabel(self)
        header_img.setPixmap(QPixmap('images/update.png'))
        header_img.move(60, 25)

        self.name_line = QLineEdit(self)
        self.name_line.resize(200, 30)
        self.name_line.move(60, 120)
        self.name_line.setFont(letter_font)

        self.age_box = QComboBox(self)
        self.age_box.move(60, 160)
        self.age_box.setFont(letter_font)
        for i in range(18, 65):
            self.age_box.addItem(str(i))

        self.addres_txt = QTextEdit(self)
        self.addres_txt.move(60, 200)
        self.addres_txt.setFont(letter_font)

        add_btn = QPushButton('Save', self)
        add_btn.setFont(btn_font)
        add_btn.move(204, 400)
        add_btn.clicked.connect(self.update_fn),

        try:
            data = database.get_one_fn(persons.per_id_for_fn)

            self.name_line.setText(data[1])
            self.age_box.setCurrentText(data[2])
            self.addres_txt.setText(data[3])

        except Exception as e:
            print(e)

    def update_fn(self):
        name = self.name_line.text()
        age = self.age_box.currentText()
        adres = self.addres_txt.toPlainText()
        if name and age and adres is not None:
            try:
                database.udate_fn(persons.per_id_for_fn, name, age, adres)
                QMessageBox.information(self, 'Info', '{}, has been update!'.format(name.capitalize()))
            except Exception as e:
                QMessageBox.information(self, 'Alert!!!', 'Data could not be update! {}'.format(e))
            finally:
                self.name_line.setText('')
                self.addres_txt.setText('')
                self.age_box.setCurrentIndex(0)
        else:
            QMessageBox.information(self, 'Alert!!!', 'Entered missing data!!!')
