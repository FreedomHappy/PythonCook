from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from random import randint
import sys

from number import Ui_MainWindow


class Action(QMainWindow,Ui_MainWindow):
	def __init__(self, parent=None):
		super(Action, self).__init__(parent)

		self.setupUi(self)

		self.num = randint(1,100)
		self.pushButton.clicked.connect(self.__judge)
		self.show()
	def closeEvent(self, event):

		reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	def __judge(self):
		guessnumber=int(self.lineEdit.text())
		print(self.num)
		if guessnumber>self.num:
			QMessageBox.about(self,'看结果','猜大了！')
			self.lineEdit.setFocus()
		elif guessnumber<self.num:
			QMessageBox.about(self, '看结果','猜小了!')
			self.lineEdit.setFocus()
		else :
			QMessageBox.about(self, '看结果','答对了!进入下一轮!')
			self.num = randint(1,100)
			self.lineEdit.clear()
			self.lineEdit.setFocus()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        self.lab = QLabel('方向',self)

        self.lab.setGeometry(150,100,50,50)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')
if __name__ == "__main__":

	app = QApplication(sys.argv)

	action = Example()

	sys.exit(app.exec_())