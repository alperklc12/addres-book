import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5.QtGui import QFont, QIcon

import persons, add_person

btn_font = QFont('Arial', 12)
letter_font = QFont('Arial', 14)


class Windows(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Address Book')
        self.setGeometry(50, 50, 400, 400)
        self.setFixedSize(self.size())
        self.interface_gui_fn()

    def interface_gui_fn(self):
        persons_btn = QPushButton('Persons', self)
        persons_btn.resize(135, 30)
        persons_btn.move(145, 70)
        persons_btn.setFont(btn_font)
        persons_btn.setIcon(QIcon('images/person.png'))
        persons_btn.setStyleSheet('background-color: #fff')
        persons_btn.clicked.connect(self.persons_btn_fn)

        add_person_btn = QPushButton('Add', self)
        add_person_btn.resize(135, 30)
        add_person_btn.move(145, 120)
        add_person_btn.setFont(btn_font)
        add_person_btn.setIcon(QIcon('images/add.png'))
        add_person_btn.setStyleSheet('background-color: #fff')
        add_person_btn.clicked.connect(self.add_btn_fn)

        about_btn = QPushButton('About', self)
        about_btn.resize(135, 30)
        about_btn.move(145, 170)
        about_btn.setFont(btn_font)
        about_btn.setIcon(QIcon('images/about.png'))
        about_btn.setStyleSheet('background-color: #fff')

        self.show()

    def persons_btn_fn(self):
        self.persons_obj = persons.Persons()
        self.persons_obj.show()

    def add_btn_fn(self):
        self.add_obj = add_person.AddPerson()
        self.add_obj.show()


def main():
    app_ui = QApplication(sys.argv)
    window = Windows()
    sys.exit(app_ui.exec())


if __name__ == '__main__':
    main()
