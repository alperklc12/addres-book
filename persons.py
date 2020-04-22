from PyQt5.QtWidgets import (QWidget, QLabel, QListWidget, QPushButton, QMessageBox)
from PyQt5.QtGui import (QFont, QPixmap)

import add_person, update_person, view_person, database

btn_font = QFont('Arial', 12)
letter_font = QFont('Arail', 14)
per_id_for_fn = None


class Persons(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('Persons')
        self.setFixedSize(self.size())
        self.interface_gui_fn()

    def interface_gui_fn(self):
        header = QLabel('Persons', self)
        header.setFont(letter_font)
        header.move(150, 50)

        header_img = QLabel(self)
        header_img.setPixmap(QPixmap('images/person.png'))
        header_img.move(60, 25)

        self.person_lst = QListWidget(self)
        self.person_lst.move(70, 90)

        try:
            person_lst_ = database.get_all_fn()
            for per in person_lst_:
                self.person_lst.addItem('{}-{}'.format(str(per[0]), per[1]))
        except Exception as a:
            print(a)

        add_btn = QPushButton('Add', self)
        add_btn.setFont(btn_font)
        add_btn.move(350, 90)
        add_btn.clicked.connect(self.add_person_fn)

        update_btn = QPushButton('Update', self)
        update_btn.setFont(btn_font)
        update_btn.move(350, 150)
        update_btn.clicked.connect(self.update_person_fn)

        viwe_btn = QPushButton('View', self)
        viwe_btn.setFont(btn_font)
        viwe_btn.move(350, 210)
        viwe_btn.clicked.connect(self.viwe_person_fn)

        delete_btn = QPushButton('Delete', self)
        delete_btn.setFont(btn_font)
        delete_btn.move(350, 270)
        delete_btn.clicked.connect(self.delete_person_fn)

    def add_person_fn(self):
        self.add_person_obj = add_person.AddPerson()
        self.add_person_obj.show()
        self.close()

    def delete_person_fn(self):
        current_person = self.person_lst.currentItem().text()
        person_id, name = current_person.split('-')
        confirm = QMessageBox.question(self, 'Warning!!!', 'Are you sure?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirm == QMessageBox.Yes:

            try:
                database.delete_fn(person_id)
                QMessageBox.information(self, 'Info', '{}, has been deleted!'.format(name.capitalize()))

                person_lst_ = database.get_all_fn()
                self.person_lst.clear()
                for per in person_lst_:
                    self.person_lst.addItem('{}-{}'.format(str(per[0]), per[1]))

            except Exception as e:
                QMessageBox.information(self, 'Alert!!!', 'Data could not be deleted! {}'.format(str(e)))

    def update_person_fn(self):
        global per_id_for_fn
        per_id_for_fn = self.person_lst.currentItem().text().split('-')[0]
        self.update_obj = update_person.UpdatePerson()
        self.update_obj.show()
        self.close()

    def viwe_person_fn(self):
        global per_id_for_fn
        per_id_for_fn = self.person_lst.currentItem().text().split('-')[0]
        self.view_obj = view_person.ViewPerson()
        self.view_obj.show()
        self.close()




