import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QRadioButton, QVBoxLayout, QScrollBar, \
    QScrollArea, QFileDialog
import sqlite3

con = sqlite3.connect("MyBase2.sqlite")

cur = con.cursor()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('medicine_ book2_vr3.ui', self)
        self.btn.clicked.connect(self.hello)

        self.m = [self.yes, self.krugit, self.toshnit, self.mental_pain, self.upper, self.downer, self.rash, self.sleep,
                  self.phusikal_pain, self.Heartburn]

    def hello(self):
        self.second_form = SecondForm(self.m)
        self.second_form.show()


class SecondForm(QMainWindow):
    def __init__(self, args):
        super().__init__()
        uic.loadUi('medicine_book3_vr7.ui', self)
        self.m = args
        if self.m[1].isChecked() and self.m[2].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Диагноз LIKE "Солнечный удар" """).fetchall()
            self.label.setText(f'Возможный диагноз: Солнечный удар. {str(self.result[0])[2:-3]}')
        elif self.m[0].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Симптомы LIKE "Наличие аллергической реакции" """).fetchall()
            self.label.setText(f'Возможный диагноз: Аллергия. {str(self.result[0])[2:-3]}')
        elif self.m[3].isChecked() and self.m[4].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Диагноз LIKE "Грипп" """).fetchall()
            self.label.setText(f'Возможный диагноз: Грипп. {str(self.result[0])[2:-3]}')
        elif self.m[3].isChecked() and self.m[5].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Симптомы LIKE "Насморк, жар, головная боль" """).fetchall()
            self.label.setText(f'Возможный диагноз: Простуда. {str(self.result[0])[2:-3]}')
        elif self.m[3].isChecked() and self.m[2].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Симптомы LIKE "Тошнота, повышение температуры, головная боль" """).fetchall()
            self.label.setText(f'Возможный диагноз: Отравление. {str(self.result[0])[2:-3]}')
        elif self.m[-2].isChecked() and self.m[-1].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Симптомы LIKE "Изжога, тошнота, боль в животе" """).fetchall()
            self.label.setText(f'Возможный диагноз: Гастрит. {str(self.result[0])[2:-3]}')
        elif self.m[-4].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Симптомы LIKE "Сыпь, темпетатура" """).fetchall()
            self.label.setText(f'Возможный диагноз: Ветрянка. {str(self.result[0])[2:-3]}')
        elif self.m[-3].isChecked():
            self.result = cur.execute("""SELECT Рекомендации FROM Medicine
                        WHERE Симптомы LIKE "Головокружение, сонливость" """).fetchall()
            self.label.setText(f'Возможный диагноз: Упадок сил. {str(self.result[0])[2:-3]}')
        else:
            self.result = f'!!!Данные симптомы не предполгагют самолечения. Обратитесь к специалистам, берегите себя!!!!'
            self.label.setText(f'Данные симптомы не предполгагют самолечения. Обратитесь к специалистам, '
                               f'берегите себя!')
        self.label.adjustSize()
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidget(self.label)
        self.scrollArea.resize(900, 400)

        self.resultat.clicked.connect(self.final)

    def final(self):
        fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', filter="All (*);;txt (*.txt)",
                                            initialFilter="txt (*.txt)")[0]
        f = open(fname, "w")
        f.write(str(self.result)[3:-4])
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
